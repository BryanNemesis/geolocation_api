from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient

from .models import GeoData


User = get_user_model()


class GeolocationApiTestCase(APITestCase):
    def setUp(self):
        User.objects.create_user(username='someuser', password='somepassword')
        token = self.obtain_access_token()
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        GeoData.objects.create(ip='0.0.0.0')
        GeoData.objects.create(ip='0.0.0.1')


    def obtain_access_token(self):
        token_obtain_url = reverse('api:token_obtain_pair')
        data = {
            'username': 'someuser',
            'password': 'somepassword',
        }
        token_obtain_response = self.client.post(token_obtain_url, data)
        access_token = token_obtain_response.data['access']
        return access_token


    def test_list_view(self):
        url = reverse('api:list-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)


    def test_detail_view(self):
        url = reverse('api:detail-view', args=['0.0.0.0'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_detail_view_wrong_ip(self):
        url = reverse('api:detail-view', args=['1.1.1.1'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


    def test_delete_view(self):
        url = reverse('api:delete-view', args=['0.0.0.0'])
        response = self.client.delete(url)
        geodata_objects_count = GeoData.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(geodata_objects_count, 1)


    def test_delete_view_wrong_ip(self):
        url = reverse('api:delete-view', args=['1.2.3.4'])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 404)


    def test_store_view(self):
        url = reverse('api:store-view', args=['1.2.3.4'])
        response = self.client.post(url)
        geodata_objects_count = GeoData.objects.count()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(geodata_objects_count, 3)
        for value in response.data.values():
            self.assertNotEqual(value, '')


    def test_store_view_duplicate(self):
        url = reverse('api:store-view', args=['1.2.3.4'])
        _ = self.client.post(url)
        response = self.client.post(url)
        geodata_objects_count = GeoData.objects.count()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(geodata_objects_count, 3)


    def test_bad_token(self):
        token = self.obtain_access_token() + 'x'
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        url = reverse('api:list-view')
        response1 = self.client.get(url)

        url = reverse('api:detail-view', args=['0.0.0.0'])
        response2 = self.client.get(url)

        url = reverse('api:delete-view', args=['0.0.0.0'])
        response3 = self.client.delete(url)

        url = reverse('api:store-view', args=['1.2.3.4'])
        response4 = self.client.post(url)

        self.assertEqual(response1.status_code, 401)
        self.assertEqual(response2.status_code, 401)
        self.assertEqual(response3.status_code, 401)
        self.assertEqual(response4.status_code, 401)
