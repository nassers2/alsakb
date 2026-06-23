from django.conf import settings


def site_settings(request):
    return {
        "SITE_NAME": settings.SITE_NAME,
        "SITE_DOMAIN": settings.SITE_DOMAIN,
        "CONTACT_PHONE": settings.CONTACT_PHONE,
        "WHATSAPP_NUMBER": settings.WHATSAPP_NUMBER,
    }
