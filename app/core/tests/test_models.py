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
            email = email,
            password = password
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