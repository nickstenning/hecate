from django.test import TestCase
from django_webtest import TestCase as WebTestCase
from django.core.urlresolvers import reverse
from django.core import mail

from apps.accounts.models import User


class TestUser(TestCase):
    def test_uses_email(self):
        """
        Tests that the modified User class forgoes a username and uses only
        emails for login.
        """
        user = User(email='giraffe@example.com')
        self.assertEqual('giraffe@example.com', user.email)


class PasswordChangeTest(WebTestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='someone@example.com',
                                             password='12345',
                                             is_active=True)
        self.client.login(email=self.user.email, password='12345')

    def test_successful_password_change(self):
        response = self.client.post(reverse('password_change'), {
            'old_password': '12345',
            'new_password1': '54321',
            'new_password2': '54321',
        })
        self.assertRedirects(response, reverse('password_change_done'))

        self.assertEqual(1, len(mail.outbox))
        email = mail.outbox[0]
        self.assertEqual('Your password has been changed', email.subject)

    def test_failing_password_change(self):
        self.client.post(reverse('password_change'))
        self.assertEqual(0, len(mail.outbox))

    def test_change_password_form(self):
        self.client.get(reverse('password_change'))
        self.assertEqual(0, len(mail.outbox))

