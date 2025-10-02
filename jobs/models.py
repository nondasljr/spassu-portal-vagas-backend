from django.db import models

class Company(models.Model):
    name = models.CharField("Nome da empresa", max_length=255, unique=True)
    website = models.URLField("Website", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Job(models.Model):
    class EmploymentType(models.TextChoices):
        CLT = "CLT", "Efetivo (CLT)"
        PJ = "PJ", "Pessoa Jurídica (PJ)"

    class WorkMode(models.TextChoices):
        PRESENCIAL = "PRESENCIAL", "Presencial"
        REMOTO = "REMOTO", "Remoto"
        HIBRIDO = "HIBRIDO", "Híbrido"

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")
    title = models.CharField("Título da vaga", max_length=255)
    employment_type = models.CharField("Tipo de emprego", max_length=10, choices=EmploymentType.choices)
    work_mode = models.CharField("Tipo de trabalho", max_length=12, choices=WorkMode.choices)
    opening_date = models.DateField("Data de abertura")
    description = models.TextField("Descrição", blank=True)
    benefits = models.JSONField("Benefícios (lista)", default=list, blank=True)
    is_active = models.BooleanField("Ativa", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-opening_date", "-created_at"]

    def __str__(self):
        return f"{self.title} - {self.company.name}"