release: yes "yes" | python manage.py migrate
web: uwsgi --http-socket=:$PORT --master --workers=2 --threads=8 --die-on-term --wsgi-file=web_app/wsgi_production.py
  --static-map /media/=web_app/media/ --offload-threads 1
