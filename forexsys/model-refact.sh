#!/bin/sh

#rbackup
# python ./manage.py dumpdata > data/initial-all.json
# sleep 10

#rm -f forexsys.db
echo "dropdb and create forexsys"
/home/tops/pgsql-9.1/bin/dropdb   -U forexsys forexsys
/home/tops/pgsql-9.1/bin/createdb -U forexsys forexsys

python ./manage.py syncdb --noinput
#python ./manage.py loaddata data/initial-all.json
python ./manage.py runserver


