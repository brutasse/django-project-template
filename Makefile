django = python manage.py

run:
	foreman start

test:
	$(django) test --failfast --noinput

syncdb:
	$(django) syncdb --noinput

user:
	$(django) createsuperuser
