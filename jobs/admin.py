from django.contrib import admin
from .models import Company, Job

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "website", "created_at")
    search_fields = ("name",)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "employment_type", "work_mode", "opening_date", "is_active")
    list_filter = ("employment_type", "work_mode", "is_active")
    search_fields = ("title", "description", "company__name")