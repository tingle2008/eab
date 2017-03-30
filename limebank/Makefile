.PHONY: clean-pyc clean-db cleanall
syncdb:
	@python manage.py syncdb

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-db:
	@rm -f db.sqlite3

cleanall: clean-pyc clean-db
