#!/bin/sh
source venv/bin/activate
export PYTHONPATH=$(pwd)
python app/init_data.py
exec gunicorn -b :5000 --access-logfile - --error-logfile - order_counter:app