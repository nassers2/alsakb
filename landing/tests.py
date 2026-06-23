from django.test import TestCase
from django.urls import reverse


class RegistrationFlowTests(TestCase):
    def test_index_loads(self):
        response = self.client.get(reverse("landing:index"))
        self.assertEqual(response.status_code, 200)

    def test_submit_valid_registration_redirects_to_thank_you(self):
        response = self.client.post(
            reverse("landing:index"),
            {
                "full_name": "محمد أحمد",
                "iqama_number": "1234567890",
                "phone_number": "0501234567",
            },
        )
        self.assertRedirects(response, reverse("landing:thank_you"))

    def test_submit_invalid_phone_shows_form_errors(self):
        response = self.client.post(
            reverse("landing:index"),
            {
                "full_name": "محمد أحمد",
                "iqama_number": "1234567890",
                "phone_number": "123",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response.context["form"], "phone_number", [
            "يرجى إدخال رقم جوال سعودي صحيح يبدأ بـ 05 ويتكون من 10 أرقام."
        ])
