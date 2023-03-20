from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase
from django.urls import reverse

CustomUser = get_user_model()


class UserRegistrationTests(TestCase):

    def test_user_registration(self):
        self.client.post(reverse('signup'), {
            'username': 'testuser',
            'name': 'Test User',
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertEqual(CustomUser.objects.count(), 1)
        user = CustomUser.objects.first()
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'testuser@example.com')


class LoginViewTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com',
            name='Test User'
        )
        self.user.backend = 'django.contrib.auth.backends.ModelBackend'

    def test_correct_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_incorrect_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })

        self.assertFalse(response.wsgi_request.user.is_authenticated)

class ProfileViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com',
            name='Test User'
        )
        self.user.backend = 'django.contrib.auth.backends.ModelBackend'

    def test_profile_view(self):
        # Log in the user with the specified backend
        self.client.login(username='testuser', password='testpassword',
                          backend='django.contrib.auth.backends.ModelBackend')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test User')
        self.assertContains(response, 'testuser@example.com')

    def test_profile_update(self):
        self.client.post(reverse('profile'), {
            'name': 'Updated Name',
            'email': 'updated@example.com'
        })
        updated_user = CustomUser.objects.get(pk=self.user.pk)
        self.assertEqual(updated_user.name, 'Updated Name')
        self.assertEqual(updated_user.email, 'updated@example.com')
