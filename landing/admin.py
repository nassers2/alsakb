from django.contrib import admin

from .models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "iqama_number", "phone_number", "created_at")
    list_filter = ("created_at",)
    search_fields = ("full_name", "iqama_number", "phone_number")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
