from django import forms

from .models import iqama_validator, phone_validator


class RegistrationForm(forms.Form):
    full_name = forms.CharField(
        label="الاسم الكامل",
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "اكتب اسمك الكامل"}
        ),
    )
    iqama_number = forms.CharField(
        label="رقم الإقامة",
        max_length=10,
        validators=[iqama_validator],
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "رقم الإقامة (10 أرقام)",
                "inputmode": "numeric",
                "maxlength": "10",
            }
        ),
    )
    phone_number = forms.CharField(
        label="رقم التواصل",
        max_length=10,
        validators=[phone_validator],
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "05XXXXXXXX",
                "inputmode": "numeric",
                "maxlength": "10",
            }
        ),
    )
