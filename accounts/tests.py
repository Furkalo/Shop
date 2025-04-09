import os
import uuid
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'online_shop.settings'
django.setup()

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase


class UserViewsTests(TestCase):

    def setUp(self):
        """
        Method that runs before each test.
        Creates test users (regular and manager) with unique emails.
        """
        self.user_data = {
            'email': f'user_{uuid.uuid4().hex[:6]}@example.com',
            'full_name': 'Test User',
            'password': 'testpassword123',
        }
        self.manager_data = {
            'email': f'manager_{uuid.uuid4().hex[:6]}@example.com',
            'full_name': 'Test Manager',
            'password': 'managerpass1234',
        }
        # Create users
        self.create_user(self.user_data)
        self.create_user(self.manager_data, is_manager=True)

    def create_user(self, data, is_manager=False):
        """
        Creates a new user with the provided data.
        If the user is a manager, sets the appropriate status.
        """
        user = get_user_model().objects.create_user(
            email=data['email'],
            full_name=data['full_name'],
            password=data['password'],
        )
        user.is_manager = is_manager
        user.save()

    def test_user_registration(self):
        """
        Tests the registration of a new user with a unique email.
        Checks if the redirection occurs after successful registration.
        """
        registration_data = {
            'email': f"user_{uuid.uuid4().hex[:6]}@example.com",
            'full_name': 'New Test User',
            'password': 'newuserpass123',
        }
        response = self.client.post(reverse('accounts:user_register'), registration_data)
        self.assertEqual(response.status_code, 302)

    def test_user_login_success(self):
        """
        Tests successful login of a user with correct credentials.
        Verifies if a redirect occurs to the homepage after login.
        """
        response = self.client.post(reverse('accounts:user_login'), {
            'email': self.user_data['email'],
            'password': self.user_data['password'],
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('shop:home_page'))

    def test_user_login_failure(self):
        """
        Tests failed login attempt with incorrect password.
        Verifies if the error message is displayed.
        """
        response = self.client.post(reverse('accounts:user_login'), {
            'email': self.user_data['email'],
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:user_login'))
        # Check if the error message is shown
        messages = list(response.wsgi_request._messages)
        self.assertEqual(str(messages[0]), 'Username or password is incorrect')

    def test_manager_login_success(self):
        """
        Tests successful login of a manager with correct credentials.
        Verifies if a redirect occurs to the dashboard after login.
        """
        response = self.client.post(reverse('accounts:manager_login'), {
            'email': self.manager_data['email'],
            'password': self.manager_data['password'],
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard:products'))

    def test_manager_login_failure(self):
        """
        Tests failed login attempt for a manager with incorrect password.
        Verifies if the error message is displayed.
        """
        response = self.client.post(reverse('accounts:manager_login'), {
            'email': self.manager_data['email'],
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:manager_login'))
        messages = list(response.wsgi_request._messages)
        self.assertEqual(str(messages[0]), 'Username or password is incorrect')

    def test_user_logout(self):
        """
        Tests logging out a user.
        Verifies if the user is redirected to the login page after logout.
        """
        self.client.login(email=self.user_data['email'], password=self.user_data['password'])
        response = self.client.get(reverse('accounts:user_logout'))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect to the login page
        self.assertRedirects(response, reverse('accounts:user_login'))

    def test_create_manager_if_not_exists(self):
        """
        Checks if a manager was created in the database.
        Verifies if the 'is_manager' field is set to True.
        """
        manager = get_user_model().objects.filter(email=self.manager_data['email']).first()
        self.assertIsNotNone(manager)
        self.assertTrue(manager.is_manager)
