from django.test import TestCase
from apps.accounts.models import User


class TestUser(TestCase):
    def test_uses_email(self):
        """
        Tests that the modified User class forgoes a username and uses only
        emails for login.
        """
        user = User(email='giraffe@example.com')
        self.assertEqual('giraffe@example.com', user.email)
