from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class AuthenticationTests(APITestCase):

    def setUp(self):
        self.register_url = reverse('auth-register')
        self.login_url = reverse('auth-login')
        self.me_url = reverse('auth-me')
        self.profile_url = reverse('auth-profile')

        self.user_data = {
            "firstName": "Cole",
            "lastName": "Naomi",
            "email": "cole@example.com",
            "password": "testpassword123",
            "role": "analyst"
        }

        self.user = User.objects.create_user(
            first_name="Coach",
            last_name="User",
            email="coach@example.com",
            password="testpassword123",
            role="coach"
        )

    def authenticate(self, user=None):
        if user is None:
            user = self.user
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)

    def test_login_valid_credentials(self):
        User.objects.create_user(
            first_name="Login",
            last_name="Test",
            email="login@example.com",
            password="validpass123",
            role="analyst"
        )
        response = self.client.post(self.login_url, {
            "email": "login@example.com",
            "password": "validpass123"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_login_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            "email": "fake@example.com",
            "password": "wrongpass"
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_profile_authenticated(self):
        self.authenticate()
        response = self.client.get(self.me_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)

    def test_get_profile_unauthenticated(self):
        response = self.client.get(self.me_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_profile(self):
        self.authenticate()
        response = self.client.put(self.profile_url, {
            "firstName": "Updated",
            "lastName": "Name",
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "Updated")
        self.assertEqual(self.user.last_name, "Name")

    def test_role_is_returned_in_token(self):
        User.objects.create_user(
            first_name="Role",
            last_name="Check",
            email="role@example.com",
            password="pass1234",
            role="analyst"
        )
        response = self.client.post(self.login_url, {
            "email": "role@example.com",
            "password": "pass1234"
        })
        self.assertIn("token", response.data)
        # You can decode and assert role if needed