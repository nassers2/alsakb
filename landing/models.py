from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r"^05\d{8}$",
    message="يرجى إدخال رقم جوال سعودي صحيح يبدأ بـ 05 ويتكون من 10 أرقام.",
)

iqama_validator = RegexValidator(
    regex=r"^\d{10}$",
    message="يرجى إدخال رقم إقامة صحيح يتكون من 10 أرقام.",
)
