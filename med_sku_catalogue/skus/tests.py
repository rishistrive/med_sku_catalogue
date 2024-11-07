from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import MedicationSKU

class MedicationSKUViewSetTests(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.sku1 = MedicationSKU.objects.create(name="Amoxicillin", presentation="Tablet", dose=50.00, unit="mg")
        cls.sku2 = MedicationSKU.objects.create(name="Ibuprofen", presentation="Capsule", dose=100.00, unit="mg")
        cls.sku3 = MedicationSKU.objects.create(name="Paracetamol", presentation="Syrup", dose=250.00, unit="ml")
        cls.list_url = reverse('medicationsku-list')
        cls.bulk_create_url = reverse('medicationsku-bulk-create')

    def test_list_medication_skus(self):
        """Test listing medication SKUs with optional filters, search, and ordering."""

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_medication_sku(self):
        """Test retrieving a single medication SKU."""

        response = self.client.get(reverse('medicationsku-detail', args=[self.sku1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.sku1.name)

    def test_create_medication_sku(self):
        """Test creating a new medication SKU."""

        data = {
            "name": "Aspirin",
            "presentation": "Tablet",
            "dose": "100.00",
            "unit": "mg"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MedicationSKU.objects.count(), 4)

    def test_bulk_create_medication_skus(self):
        """Test bulk creating medication SKUs."""

        data = [
            {
                "name": "Penicillin",
                "presentation": "Tablet",
                "dose": "200.00",
                "unit": "mg"
            },
            {
                "name": "Cetirizine",
                "presentation": "Syrup",
                "dose": "5.00",
                "unit": "mg"
            }
        ]
        print(self.bulk_create_url,data)
        response = self.client.post(self.bulk_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MedicationSKU.objects.count(), 5)

    def test_update_medication_sku(self):
        """Test updating an existing medication SKU."""

        data = {
            "name": "Amoxicillin Updated",
            "presentation": "Tablet",
            "dose": "50.00",
            "unit": "mg"
        }
        response = self.client.put(reverse('medicationsku-detail', args=[self.sku1.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sku1.refresh_from_db()
        self.assertEqual(self.sku1.name, "Amoxicillin Updated")

    def test_delete_medication_sku(self):
        """Test deleting a medication SKU."""

        response = self.client.delete(reverse('medicationsku-detail', args=[self.sku1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MedicationSKU.objects.count(), 2)

    def test_search_medication_skus(self):
        """Test searching medication SKUs by name."""

        response = self.client.get(f"{self.list_url}?search=Amoxicillin")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_medication_skus(self):

        """Test filtering medication SKUs by dose."""
        response = self.client.get(f"{self.list_url}?dose=100.00")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_medication_skus(self):
        """Test ordering medication SKUs by name in descending order."""

        response = self.client.get(f"{self.list_url}?ordering=-name")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], "Paracetamol")

