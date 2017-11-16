#!/bin/bash

# Django 1.11 compatible

# mdcNo = ('1','2','3','4','5','6','7','8','9','10','11','12','13','15','16')

find $(pwd) -iname \*.pyc -exec rm -rfv {} \; #to delete all .pyc files

DIR="$( cd "$( dirname "$0" )" && pwd )"
cd $DIR
killall streamer
rm production_static_files/img/webcam/*.jpeg
source venv/bin/activate
#source ./bin/activate
python switch_onn.py 
python sbhs_server/scan_machines.py
#python offline_reconnect.py
python create_db.py
python manage.py makemigrations
python manage.py makemigrations tables
python manage.py makemigrations account
python manage.py makemigrations experiment
python manage.py makemigrations slot
python manage.py migrate
python manage.py initialize_machines
python manage.py generate_checksum
touch index.wsgi
python manage.py log_generator
python check_future_slots.py

#python log_generator.py
date > date.txt
sleep 2
# python sbhs_server/switch_off.py 1
