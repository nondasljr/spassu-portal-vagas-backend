from rest_framework import serializers
from .models import Company, Job

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "website", "created_at"]


class JobSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source="company.name", read_only=True)

    class Meta:
        model = Job
        fields = [
            "id", "company", "company_name", "title", "employment_type",
            "work_mode", "opening_date", "description", "benefits",
            "is_active", "created_at"
        ]

    def validate_benefits(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Benefícios deve ser uma lista de strings.")
        if not all(isinstance(b, str) for b in value):
            raise serializers.ValidationError("Cada benefício deve ser uma string.")
        return value