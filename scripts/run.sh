#!/bin/bash

WEB_CONCURRENCY=$(($(nproc) * 2 + 1)) gunicorn config.wsgi:application --bind 0.0.0.0:8000