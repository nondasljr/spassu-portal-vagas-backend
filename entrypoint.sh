#!/bin/sh

# Executa migrações
python manage.py migrate --noinput

# Cria usuário padrão se não existir
echo "Verificando usuário padrão..."
python manage.py shell << END
from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username="spassu-a").exists():
    User.objects.create_superuser(
        username="spassu-a",
        email="spassu@spassu.com",
        password="aprovar"
    )
    print("Usuário padrão criado: spassu-a / aprovar")
else:
    print("Usuário padrão já existe.")
END

echo "Executando seeds de dados..."
python manage.py seed

exec "$@"