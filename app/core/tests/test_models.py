from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email(self):
        """
        Test creating a new user with an email is successfull
        """
        email = "test@gmail.com"
        password = "Test12345@"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
            )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        """
        Test the email of new user is normalized
        """
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'test12345')

        self.assertEqual(user.email, email.lower())

    def test_user_invalid_email(self):
        """
        Test creating user with no email raises error
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test12345')

    def test_create_superuser(self):
        """
        Test Creating new superuser
        """
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test12345'
            )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
