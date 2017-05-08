import os

from django.core.files.base import ContentFile
from django.conf import settings

from test_plus.test import TestCase
import factory

from league.tests import factories


def get_full_path(media_relative_path):
    return os.path.join(settings.MEDIA_ROOT, media_relative_path)


class TestModels(TestCase):
    user_factory = factories.UserFactory

    # def setUp(self):
    #     self.user = self.make_user()

    def test__delete_code_after_team_delete(self):
        team = factories.TeamFactory()
        code_file_path = get_full_path(team.code.__str__())
        self.assertEqual(os.path.isfile(code_file_path), True)
        team.delete()
        self.assertEqual(os.path.isfile(code_file_path), False)

    def test__overwrite_code_after_team_change(self):
        team = factories.TeamFactory()
        old_code_file_path = get_full_path(team.code.__str__())
        with open(old_code_file_path, 'rb') as old_file:
            old_code_file_content = old_file.read()
        team.code.save(
            name=factory.Faker('file_name', extension='py').generate(dict()),
            content=ContentFile(factory.Faker('binary', length=10485).generate(dict()))
        )
        new_code_file_path = get_full_path(team.code.__str__())
        with open(new_code_file_path, 'rb') as new_file:
            new_code_file_content = new_file.read()
        self.assertTrue(os.path.isfile(new_code_file_path), True)
        self.assertEqual(old_code_file_path, new_code_file_path)
        self.assertNotEqual(old_code_file_content, new_code_file_content)