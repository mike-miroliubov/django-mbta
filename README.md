# Django example - Transport monitoring system
* App allows trains to report their location (at which station they are)
* Only if next station is empty, a train can go
* User can query all current train positions
* Trains can register on the system
* Simulator should send requests with a random frequency

TODO:
* tests +
* more functionality
* Docker and real server deployment +
* real database +
* * connection pool  
* tests w/ Docker and testcontainers
* use https://django-environ.readthedocs.io/en/latest/ +
* Authentication +
* Dependency injection +
* Error handling
* Background tasks

Optional:
* clean architecture https://github.com/sdediego/django-clean-architecture/tree/main

# Run:
```python manage.py runserver```

OR

```gunicorn config.wsgi:application --bind 0.0.0.0:8000```

# Run in Docker
```
docker build . -t mbta
docker compose up -d 
docker-compose exec mbta python manage.py migrate --noinput
```