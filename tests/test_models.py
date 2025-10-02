import pytest
from .factories import CompanyFactory, JobFactory

@pytest.mark.django_db
def test_company_str():
    c = CompanyFactory(name="Spassu")
    assert str(c) == "Spassu"

@pytest.mark.django_db
def test_job_str():
    j = JobFactory(title="Pessoa Desenvolvedora Python Sr")
    assert "Pessoa Desenvolvedora Python Sr" in str(j)