python manage.py makemigrations --settings=config.settings.local
python manage.py migrate --settings=config.settings.local
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'bestheroz@gmail.com', 'admin!@#')" | python manage.py shell
