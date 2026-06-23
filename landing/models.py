from django.core.validators import RegexValidator
from django.db import models

phone_validator = RegexValidator(
    regex=r"^05\d{8}$",
    message="يرجى إدخال رقم جوال سعودي صحيح يبدأ بـ 05 ويتكون من 10 أرقام.",
)

iqama_validator = RegexValidator(
    regex=r"^\d{10}$",
    message="يرجى إدخال رقم إقامة صحيح يتكون من 10 أرقام.",
)


class Registration(models.Model):
    full_name = models.CharField("الاسم الكامل", max_length=150)
    iqama_number = models.CharField(
        "رقم الإقامة", max_length=10, validators=[iqama_validator]
    )
    phone_number = models.CharField(
        "رقم التواصل", max_length=10, validators=[phone_validator]
    )
    created_at = models.DateTimeField("تاريخ التسجيل", auto_now_add=True)

    class Meta:
        verbose_name = "طلب انضمام"
        verbose_name_plural = "طلبات الانضمام"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.phone_number}"
