from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_filter = ['gender', 'role', 'membership_type']  # Enable filtering by these fields
    search_fields = ['name', 'email', 'phone', 'gender']  # Enable search by these fields
    list_display = ['name', 'email', 'phone', 'gender', 'paid','role']

admin.site.register(Member, MemberAdmin)
