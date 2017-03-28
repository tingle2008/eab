1. Checkout the code from this repository
2. Move into the source tree
3. run `pip install -r requirements' to install all depends.
4. run `python ./manage.py syncdb --noinput' to create your development database
5. run `python ./manage.py loaddata data/initial-auth.json' to create your development database
6. run `python ./manage.py loaddata data/initial-tradesys.json' to create your development database
7. run `python ./manage.py runserver' to start server

The admin username and password will be admin/admin.

