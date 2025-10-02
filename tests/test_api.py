import pytest
from rest_framework.test import APIClient
from .factories import CompanyFactory, JobFactory

@pytest.mark.django_db
def test_list_jobs():
    JobFactory.create_batch(3)
    client = APIClient()
    res = client.get("/api/jobs/")
    assert res.status_code == 200
    assert res.data["count"] >= 3

@pytest.mark.django_db
def test_filter_jobs_by_company():
    c1 = CompanyFactory(name="Spassu")
    c2 = CompanyFactory(name="Outra")
    JobFactory(company=c1)
    JobFactory(company=c2)
    client = APIClient()
    res = client.get(f"/api/jobs/?company={c1.id}")
    assert res.status_code == 200
    for item in res.data["results"]:
        assert item["company"] == c1.id

@pytest.mark.django_db
def test_create_job_validation_benefits():
    c = CompanyFactory()
    client = APIClient()
    payload = {
        "company": c.id,
        "title": "Dev Senior",
        "employment_type": "PJ",
        "work_mode": "REMOTO",
        "opening_date": "2025-10-02",
        "description": "Teste",
        "benefits": ["Notebook", "Ajuda de custo"],
        "is_active": True
    }
    res = client.post("/api/jobs/", payload, format="json")
    assert res.status_code == 201

    payload["benefits"] = "VR"
    res2 = client.post("/api/jobs/", payload, format="json")
    assert res2.status_code == 400