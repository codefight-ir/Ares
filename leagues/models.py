# -*- coding: utf-8 -*-
from celery.result import AsyncResult
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


def validate_even(value):
    """
    Validate a number to be even
    """
    if value % 2 != 0:
        raise ValidationError('%(value)s is not an even number',
                              params={'value': value})


class League(models.Model):
    """
    Leagues for robots
    """
    title = models.CharField(
        'title',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer.',
        error_messages={
            'unique': 'A league with that name already exists.',
        },
    )
    description = models.CharField(max_length=1000, blank=True, null=True)
    finished = models.BooleanField('finished', default=False)
    registration_start = models.DateTimeField('registration start time')
    registration_end = models.DateTimeField('registration end time')
    start = models.DateField('league start date')
    # Times to schedule matches within a day
    match_start_time = models.TimeField('matches start time')
    match_end_time = models.TimeField('matches end time')
    num_robots = models.PositiveSmallIntegerField('number of robots',
                                                  validators=[validate_even])
    game = models.ForeignKey('games.Game', related_name='leagues')
    robots = models.ManyToManyField('robots.Robot', blank=True,
                                    related_name='leagues')
    _match_scheduler_id = models.CharField('match scheduler id',
                                           max_length=36, null=True)

    def __init__(self, *args, **kwargs):
        super(League, self).__init__(*args, **kwargs)
        self.__original_registration_end = self.registration_end

    @property
    def match_scheduler(self):
        """
        Match scheduler task
        """
        if self._match_scheduler_id:
            return AsyncResult(self._match_scheduler_id)
        return None

    @match_scheduler.setter
    def match_scheduler(self, scheduler):
        if isinstance(scheduler, AsyncResult):
            self._match_scheduler_id = scheduler.id

    @match_scheduler.deleter
    def match_scheduler(self):
        self._match_scheduler_id = None

    def has_schedule_changed(self):
        """
        Check if the league schedule has changed or not
        """
        return self.registration_end != self.__original_registration_end

    def clean(self):
        """
        Validate the the values
        """
        now = timezone.now()
        if self.registration_start <= now:
            raise ValidationError(
                u'Registration starting time must be after now')

        if self.registration_end <= self.registration_start:
            raise ValidationError(
                u'Registration ending time must be after its starting')

        if self.start <= self.registration_end.date():
            raise ValidationError(
                u'League starting time must be after registration ending time')

        if self.match_end_time <= self.match_start_time:
            raise ValidationError(
                u'Match ending time must be after its starting time')

    def __str__(self):
        return '{} ({})'.format(self.title, self.game)
