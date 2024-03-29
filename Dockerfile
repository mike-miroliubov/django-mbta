# A Dockerfile that contains gunicorn, a production-ready Pyton web server.
# See https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
FROM python:3.12

RUN addgroup -gid 1000 appuser; \
    adduser --uid 1000 --gid 1000 --disabled-password --home /opt/app appuser; \
    chown -R appuser /opt/app

COPY ./requirements.txt /opt/app

WORKDIR /opt/app
RUN pip install -r requirements.txt

COPY ./config /opt/app/config
COPY ./django_intro_app /opt/app/django_intro_app
COPY ./manage.py /opt/app
COPY ./scripts/run.sh /opt/app

USER appuser
CMD ["bash", "run.sh"]