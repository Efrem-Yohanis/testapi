from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Dealer1

class Dealer1APITest(APITestCase):

    def setUp(self):
        self.valid_dealer = {
            "event": "insert",
            "name": "John Doe",
            "number": "123456789",
            "first_name": "John",
            "last_name": "Doe",
            "status": True
        }

        self.invalid_dealer = {
            "event": "",
            "name": "",
            "number": "123456789",
            "first_name": "",
            "last_name": "",
            "status": True
        }

        self.dealer = Dealer1.objects.create(**self.valid_dealer)

    def test_add_valid_dealer(self):
        response = self.client.post(reverse('add_dealer'), self.valid_dealer)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_invalid_dealer(self):
        response = self.client.post(reverse('add_dealer'), self.invalid_dealer)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_dealers(self):
        response = self.client.get(reverse('get_dealers'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_dealer(self):
        updated_data = {"name": "Updated Name"}
        url = reverse('update_dealer', args=[self.dealer.id])
        response = self.client.put(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Name")

    def test_delete_all_dealers(self):
        response = self.client.delete(reverse('delete_all_dealers'))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Dealer1.objects.count(), 0)

# Create your tests here.
