from django import forms

from .models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ["full_name", "iqama_number", "phone_number"]
        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "اكتب اسمك الكامل",
                }
            ),
            "iqama_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "رقم الإقامة (10 أرقام)",
                    "inputmode": "numeric",
                    "maxlength": "10",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "05XXXXXXXX",
                    "inputmode": "numeric",
                    "maxlength": "10",
                }
            ),
        }
