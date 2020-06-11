from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from locations.models import Country, Symbol


class UserTests(APITestCase):

    def setUp(self):
        self.u = User.objects.create_user(username='user', email='user@gmail.com', password='pass')
        self.u.is_active = True
        self.u.save()

    def test_user_get(self):
        url_token = reverse('token_obtain_pair')

        resp = self.client.post(url_token, {'username': 'user', 'password': 'pass'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data)
        token = resp.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        resp = self.client.get('http://127.0.0.1:8000/locations_api/users/', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)


class CountryTests(APITestCase):

    def setUp(self):
        self.u = User.objects.create_user(username='test', email='test@gmail.com', password='test')
        self.u.is_active = True
        self.u.save()

    def test_country_get(self):
        url_token = reverse('token_obtain_pair')

        resp = self.client.post(url_token, {'username': 'test', 'password': 'test'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data)
        token = resp.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        resp = self.client.get('http://127.0.0.1:8000/locations_api/countries/', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)


class CityTests(APITestCase):

    def setUp(self):
        self.u = User.objects.create_user(username='test', email='test@gmail.com', password='test')
        self.u.is_active = True
        self.u.save()

    def test_city_get(self):
        url_token = reverse('token_obtain_pair')

        resp = self.client.post(url_token, {'username': 'test', 'password': 'test'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data)
        token = resp.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        resp = self.client.get('http://127.0.0.1:8000/locations_api/cities/', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_city_post(self):
        url_token = reverse('token_obtain_pair')

        resp = self.client.post(url_token, {'username': 'test', 'password': 'test'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data)
        token = resp.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.post('http://127.0.0.1:8000/locations_api/cities/', {'name': 'City'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)