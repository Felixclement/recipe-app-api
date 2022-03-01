from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """testing a new user create"""
        email = "test@test.com"
        password = "Testpass123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test email"""
        email = "test@TEST.com"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test if email is none"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'user123')

    def test_super_user(self):
        """test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            "test@test.com",
            "Testpass123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
