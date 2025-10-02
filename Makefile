up:
\tdocker compose up -d

logs:
\tdocker compose logs -f api

migrate:
\tdocker compose exec api bash -lc "python manage.py migrate"

shell:
\tdocker compose exec api bash -lc "python manage.py shell_plus || python manage.py shell"

seed:
\tdocker compose exec api bash -lc "python manage.py seed"

test:
\tdocker compose exec api bash -lc "pytest -q"