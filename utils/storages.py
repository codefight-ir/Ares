# -*- coding: utf-8 -*-
from django.core.files.storage import FileSystemStorage


class CustomStorage(FileSystemStorage):
    """
    A storage that generate a new filename if already exists.
    """

    def __init__(self, location=None, base_url=None,
                 file_permissions_mode=None, directory_permissions_mode=None):
        super(CustomStorage, self).__init__(location, base_url,
                                            file_permissions_mode,
                                            directory_permissions_mode)
        self._counter = 0

    def get_available_name(self, name, max_length=None):
        """
        Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        If the filename already exists, appends an integer and checks 
        again until it finds a free one.
        """
        new_name = name
        while self.exists(new_name):
            self._counter += 1
            filename, ext = name.rsplit('.', 1)
            new_name = filename + '_{}.{}'.format(self._counter, ext)
            return self.get_available_name(new_name, max_length)
        return new_name
