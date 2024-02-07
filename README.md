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
* tests w/ Docker and testcontainers https://github.com/wonkybream/django-rdtwt
* * Fakes and factories https://www.hacksoft.io/blog/improve-your-tests-django-fakes-and-factories
* * mocks https://realpython.com/python-mock-library/#assertions-and-inspection
* use https://django-environ.readthedocs.io/en/latest/ +
* Authentication +
* Dependency injection +
* * https://medium.com/@snyksec/dependency-injection-in-python-35da876ed7a3
* * https://python-dependency-injector.ets-labs.org/examples/django.html
* * https://pypi.org/project/django-injector/
* Error handling
* Background tasks
* Following these tips: https://github.com/HackSoftware/Django-Styleguide?tab=readme-ov-file#settings
* settings hierarchy https://github.com/HackSoftware/Django-Styleguide-Example/blob/master/config/django/base.py +  

Optional:
* clean architecture https://github.com/sdediego/django-clean-architecture/tree/main
* * https://medium.com/21buttons-tech/clean-architecture-in-django-d326a4ab86a9

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