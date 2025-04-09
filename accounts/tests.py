import os
import uuid

import django


os.environ['DJANGO_SETTINGS_MODULE'] = 'online_shop.settings'

# Initialize Django
django.setup()

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase


class UserViewsTests(TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.user = None

    def setUp(self):
        self.user_data = {
            'email': 'user_1@example.com',
            'full_name': 'Test User',
            'password': 'testpassword123',
        }
        self.manager_data = {
            'email': 'manager@example.com',
            'full_name': 'Test Manager',
            'password': 'managerpass1234',
        }
        self.create_user(self.user_data)
        self.create_user(self.manager_data, is_manager=True)

    def create_user(self, data, is_manager=False):
        user = get_user_model().objects.create_user(
            email=data['email'],
            full_name=data['full_name'],
            password=data['password'],
        )
        user.is_manager = is_manager
        user.save()

    def test_user_registration(self): # видали
        self.user_data['email'] = f"user_{uuid.uuid4().hex[:6]}@example.com"  # Unique email for each test run
        response = self.client.post(reverse('accounts:user_register'), self.user_data)

        # Check if the response status code is 302 (redirection)
        self.assertEqual(response.status_code, 302)

    def test_user_login_success(self):
        response = self.client.post(reverse('accounts:user_login'), {
            'email': self.user_data['email'],
            'password': self.user_data['password'],
        })
        self.assertEqual(response.status_code, 302)  # Очікуємо редирект на головну сторінку
        self.assertRedirects(response, reverse('shop:home_page'))

    def test_user_login_failure(self):
        response = self.client.post(reverse('accounts:user_login'), {
            'email': self.user_data['email'],
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:user_login'))
        # Перевіряємо, чи виведено повідомлення про помилку
        messages = list(response.wsgi_request._messages)
        self.assertEqual(str(messages[0]), 'Username or password is incorrect')

    def test_manager_login_success(self):
        response = self.client.post(reverse('accounts:manager_login'), {
            'email': self.manager_data['email'],
            'password': self.manager_data['password'],
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard:products'))

    def test_manager_login_failure(self):
        response = self.client.post(reverse('accounts:manager_login'), {
            'email': self.manager_data['email'],
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:manager_login'))
        messages = list(response.wsgi_request._messages)
        self.assertEqual(str(messages[0]), 'Username or password is incorrect')

    def test_user_logout(self):
        self.client.login(email=self.user_data['email'], password=self.user_data['password'])
        response = self.client.get(reverse('accounts:user_logout'))
        self.assertEqual(response.status_code, 302)  # Очікуємо редирект на сторінку входу
        self.assertRedirects(response, reverse('accounts:user_login'))

    def test_create_manager_if_not_exists(self):
        # Перевіряємо, чи менеджер був створений в базі даних
        manager = get_user_model().objects.filter(email="manager@example.com").first()
        self.assertIsNotNone(manager)
        self.assertTrue(manager.is_manager)
