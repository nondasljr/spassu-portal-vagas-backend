from django.core.management.base import BaseCommand
from jobs.models import Company, Job
from datetime import date

class Command(BaseCommand):
    help = "Cria dados de exemplo"

    def handle(self, *args, **options):
        spassu, _ = Company.objects.get_or_create(name="Spassu", defaults={"website": "https://www.spassu.com.br"})
        acme, _ = Company.objects.get_or_create(name="ACME Tech")

        Job.objects.get_or_create(
            company=spassu, title="Pessoa Desenvolvedora Python Sr",
            employment_type="PJ", work_mode="REMOTO",
            opening_date=date.today(),
            defaults={"description": "Projeto incrível, stack Python/Django/React.",
                      "benefits": ["Home office", "Auxílio tecnologia"], "is_active": True}
        )
        Job.objects.get_or_create(
            company=acme, title="Fullstack Engineer",
            employment_type="CLT", work_mode="HIBRIDO",
            opening_date=date.today(),
            defaults={"description": "Atuação em produto web.",
                      "benefits": ["VR", "Plano de saúde"], "is_active": True}
        )
        self.stdout.write(self.style.SUCCESS("Seed criado com sucesso!"))