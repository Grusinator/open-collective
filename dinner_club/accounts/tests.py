from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class LoginViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_correct_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Check if the user is authenticated and the response redirects to the default profile URL
        self.assertRedirects(response, '/accounts/profile/')
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_incorrect_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })

        # Check if the user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)
