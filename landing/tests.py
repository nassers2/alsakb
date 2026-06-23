from django.test import TestCase
from django.urls import reverse

from .models import Registration


class RegistrationFlowTests(TestCase):
    def test_index_loads(self):
        response = self.client.get(reverse("landing:index"))
        self.assertEqual(response.status_code, 200)

    def test_submit_registration_saves_and_redirects(self):
        response = self.client.post(
            reverse("landing:index"),
            {
                "full_name": "محمد أحمد",
                "iqama_number": "1234567890",
                "phone_number": "0501234567",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Registration.objects.count(), 1)
