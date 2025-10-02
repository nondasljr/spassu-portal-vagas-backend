from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import FilterSet, filters
from .models import Company, Job
from .serializers import CompanySerializer, JobSerializer

class JobFilter(FilterSet):
    company = filters.NumberFilter(field_name="company_id")
    employment_type = filters.CharFilter(lookup_expr="iexact")
    work_mode = filters.CharFilter(lookup_expr="iexact")
    opened_from = filters.DateFilter(field_name="opening_date", lookup_expr="gte")
    opened_to = filters.DateFilter(field_name="opening_date", lookup_expr="lte")
    is_active = filters.BooleanFilter()

    class Meta:
        model = Job
        fields = ["company", "employment_type", "work_mode", "is_active", "opened_from", "opened_to"]


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ["name"]
    search_fields = ["name"]


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.select_related("company").all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = JobFilter
    search_fields = ["title", "description", "company__name"]
    ordering_fields = ["opening_date", "created_at", "title"]