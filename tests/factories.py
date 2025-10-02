import factory
from jobs.models import Company, Job
from datetime import date

class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company
    name = factory.Sequence(lambda n: f"Company {n}")
    website = "https://example.com"

class JobFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Job
    company = factory.SubFactory(CompanyFactory)
    title = factory.Sequence(lambda n: f"Dev Python {n}")
    employment_type = "CLT"
    work_mode = "REMOTO"
    opening_date = factory.LazyFunction(date.today)
    description = "Descrição padrão"
    benefits = ["VR", "Saúde"]
    is_active = True