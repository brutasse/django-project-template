django = envdir env django-admin.py
testdjango = envdir tests/env django-admin.py

run:
	foreman start

test:
	$(testdjango) test --failfast --noinput

syncdb:
	$(django) syncdb --noinput

user:
	$(django) createsuperuser
