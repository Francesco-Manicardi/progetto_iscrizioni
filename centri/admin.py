from django.contrib import admin
from centri.models import Centro


@admin.register(Centro)
class CentroAdmin(admin.ModelAdmin):
    list_display = ("nome", "indirizzo", "capienza", "capienza_residua")
    list_filter = ("nome", "indirizzo")

    def capienza_residua(self, obj):
        return obj.get_capienza_residua()
