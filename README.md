# Spassu • Portal de Vagas — Backend (Django + DRF)

API para cadastro e consulta de vagas, construída com **Django 5**, **Django REST Framework**, **SQLite** e **Docker**.

- Documentação automática (Swagger): `/api/docs/`  
- Schema OpenAPI: `/api/schema/`  
- Admin do Django: `/admin/`

---

## Requisitos

- Docker e Docker Compose  
- Porta **8000** livre na máquina  
- (Opcional) VSCode para debug

---

## Variáveis de ambiente

Arquivo `.env` (já incluído no projeto):

```env
DJANGO_DEBUG=1
DJANGO_SECRET_KEY=dev-secret-key-change-me
DJANGO_ALLOWED_HOSTS=*
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

---

## Subindo a API com Docker

Dentro da pasta `backend/`:

```bash
# build da imagem
docker compose build

# subir em background
docker compose up -d

# ver logs
docker compose logs -f api
```

A API deve ficar disponível em:  
http://localhost:8000/api/

---

## Migrações e usuário admin

```bash
# criar/migrar banco
docker compose exec api bash -lc "python manage.py makemigrations"
docker compose exec api bash -lc "python manage.py migrate"

# criar usuário admin
docker compose exec api bash -lc "python manage.py createsuperuser --username admin --email admin@example.com"
```

Acesse o admin em http://localhost:8000/admin/

---

## Dados de exemplo (seed)

O projeto inclui um comando de management `seed` que cria empresas e vagas de exemplo.

```bash
docker compose exec api bash -lc "python manage.py seed"
```

Isso cria, por exemplo:
- Empresa **Spassu** com uma vaga “Pessoa Desenvolvedora Python Sr (PJ/REMOTO)”
- Empresa **ACME Tech** com uma vaga “Fullstack Engineer (CLT/HÍBRIDO)”

Você pode conferir em:
- Lista de vagas: `GET http://localhost:8000/api/jobs/`
- Lista de empresas: `GET http://localhost:8000/api/companies/`

---


## Makefile (atalhos)

Na raiz do projeto (pasta `backend/`) há um `Makefile` com alvos úteis:

```makefile
up:
	docker compose up -d

logs:
	docker compose logs -f api

migrate:
	docker compose exec api bash -lc "python manage.py migrate"

shell:
	docker compose exec api bash -lc "python manage.py shell_plus || python manage.py shell"

seed:
	docker compose exec api bash -lc "python manage.py seed"

test:
	docker compose exec api bash -lc "pytest -q"
```

Uso:

```bash
make up
make migrate
make seed
make test
make logs
```

---


## Estrutura

```
backend/
├── config/                 # projeto Django
├── jobs/                   # app de vagas
├── sqlite_data/            # banco SQLite (volume)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── manage.py
├── Makefile
└── tests/                  # testes (pytest)
```
