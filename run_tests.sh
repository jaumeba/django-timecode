#!/bin/sh

django-admin.py test --pythonpath=. --settings=django_timecode.test.settings
