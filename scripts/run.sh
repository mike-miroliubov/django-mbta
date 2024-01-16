#!/bin/bash

WEB_CONCURRENCY=$(($(nproc) * 2 + 1)) gunicorn django_intro.wsgi:application --bind 0.0.0.0:8000