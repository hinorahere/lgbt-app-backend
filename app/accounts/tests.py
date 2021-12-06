from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test new user creation with an email is successful
        """
        username = 'adminAdmin123'
        email = 'test@gmail.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
            username=username,
			email=email,
			password=password
		)

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
