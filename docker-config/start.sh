#!/bin/bash

cd /src

# Script to run on docker start up, to initialize the database
printf "==================\n"
printf "RUNNING MIGRATIONS\n"
printf "==================\n"
pipenv run server/manage.py migrate
printf "\n"

printf "==================\n"
printf "ADDING GROUPS & PERMISSIONS\n"
printf "==================\n"
pipenv run server/manage.py create_roles
printf "\n"

printf "==================\n"
printf "LOADING FIXTURES\n"
printf "==================\n"
pipenv run server/manage.py loaddata risk_category.json
pipenv run server/manage.py loaddata student_first.json
printf "\n"

printf "===================\n"
printf "STARTING SUPERVISOR\n"
printf "===================\n"
supervisord -n -c /etc/supervisor/supervisord.conf
