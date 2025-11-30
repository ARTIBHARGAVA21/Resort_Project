#!/usr/bin/env bash
gunicorn resort.wsgi:application --bind 0.0.0.0:8000
