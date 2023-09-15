#!/bin/bash

python manage.py migrate
python manage.py collectstatic
# and add this at the end
exec "$@"