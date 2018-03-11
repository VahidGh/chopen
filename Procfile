release: yes "yes" | python manage.py migrate
web: gunicorn web_app.wsgi --log-file -
