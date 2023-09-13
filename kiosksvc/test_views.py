from rest_framework import status
from kiosksvc.views import ParticipantView
from kiosksvc.models import Participant
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from django.urls import reverse



class ParticipantViewTestCase(APITestCase):
    def setUp(self):
        Participant.objects.create(
            name="John Doe",
            email="abc@example.com",
            affilation="Null Inc.",
            role="",
            qrUrl="",
            couponDetail="",
        )
        Participant.objects.create(
            name="Kubernetes",
            email="def@example.com",
            affilation="LFCNCF",
            role="YAML Engineer",
            qrUrl="",
            couponDetail="",
        )

    def test_get(self):
        response = self.client.get("/participants/?keyword=abc", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(Account.objects.count(), 1)
        # self.assertEqual(Account.objects.get().name, 'DabApps')

