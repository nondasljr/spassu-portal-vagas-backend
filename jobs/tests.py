import pytest
from rest_framework.test import APIClient
from datetime import date
from .models import Job, Company


@pytest.mark.django_db
def test_create_job_success():
    """Cria uma vaga válida e verifica campos essenciais no retorno."""
    company = Company.objects.create(name="Spassu", website="https://spassu.com.br")
    client = APIClient()

    payload = {
        "company": company.id,
        "title": "Pessoa Desenvolvedora Python Sr",
        "employment_type": "PJ",
        "work_mode": "REMOTO",
        "opening_date": date.today().isoformat(),
        "description": "Desenvolvimento de APIs com Django REST.",
        "benefits": ["Home office", "Auxílio tecnologia"],
        "is_active": True,
    }

    res = client.post("/api/jobs/", payload, format="json")
    assert res.status_code == 201
    data = res.json()
    assert data["title"] == payload["title"]
    assert data["employment_type"] == "PJ"
    assert data["work_mode"] == "REMOTO"
    assert data["benefits"] == ["Home office", "Auxílio tecnologia"]


@pytest.mark.django_db
def test_create_job_invalid_employment_type():
    """Garante validação de choices: employment_type inválido -> 400."""
    company = Company.objects.create(name="Spassu", website="https://spassu.com.br")
    client = APIClient()

    payload = {
        "company": company.id,
        "title": "Dev Python",
        "employment_type": "ESTAGIO",  # inválido
        "work_mode": "REMOTO",
        "opening_date": date.today().isoformat(),
        "description": "Teste",
        "benefits": ["VR"],
        "is_active": True,
    }

    res = client.post("/api/jobs/", payload, format="json")
    assert res.status_code == 400
    assert "employment_type" in res.json()