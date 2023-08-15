from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "role", "created_at", "expiry_date", "paid"]  # Add more fields as needed
    ordering = ["name"]
    list_filter = ['gender', 'role', 'membership_type']  # Enable filtering by these fields
    search_fields = ['name', 'email', 'phone', 'gender']  # Enable search by these fields
    actions = ["make_published","ward","local level", "district level", "province level","central level"]

    def make_published(self,queryset):
        queryset.update(status="p")
    make_published.short_description = "Mark selected members as published"