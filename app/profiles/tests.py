import json

from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from . serializers import ProfileSerializer
from . models import Photo, Profile

class ProfileTestCases(APITestCase):

    def setUp(self):
        self.username = 'adminAdmin123'
        self.email = 'test@test.com'
        self.password = 'Password123'
        self.user = get_user_model().objects.create_user(
            username=self.username,
			email=self.email,
			password=self.password
		)
        self.token = self.get_token()
        self.profile = {"first_name": "Nora",
                        "last_name": "Renfrow",
                        "bio": "This is a bio"}

    def get_token(self):
        user_credentials = {"username": self.user.email,
                            "password": self.password}
        token = self.client.post("/api-token-auth/", user_credentials)
        return token.data['token']

    def test_profile_registration(self):
        response = self.client.post("/api/profile/", \
                                    self.profile,
                                    HTTP_AUTHORIZATION="Token " + self.token)

        self.profile_id = str(response.data['id'])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], \
                                                    self.profile['first_name'])
        self.assertEqual(response.data['last_name'], self.profile['last_name'])

    def test_profile_bad_token(self):
        response = self.client.post("/api/profile/", \
                                    self.profile,
                                    HTTP_AUTHORIZATION="Token " + "Bad token")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
