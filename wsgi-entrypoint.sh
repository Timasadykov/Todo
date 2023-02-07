#!/bin/sh


until cd /app/
do
    echo "waiting for server volume..."
done

until ./manage.py migrate --noinput


do 
    echo "Waiting for db to be ready"
    sleep 2
done

./manage.py shell =c "from django.contrib.auth.models import User; print('user is already exests')
if User.objects.filter(username=admin).exists'() else User.objects.create_superuser
'(admin', '', '1')"

./manage.py collectstatic --noinput

gunicorn core.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4 
