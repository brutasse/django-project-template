.. {% comment %}

Django project template
=======================

This is the template I use for my projects.

Stack
-----

* Django

* Postgresql

* Redis

* Daemontools

Features
--------

* ``setup.py`` for deployment using real packages

* Local development with Foreman

* Configuration entirely based on evnironment variables (**no code changes**
  when your deploy)

* SCSS/compass with simplified Frameless by @idan for layout management,
  responsive-ready

* Integrated apps:

  * django-discover-runner

  * django-floppyforms

  * django-ratelimit-backend

  * django-redis-cache

  * django-sekizai

  * raven

Usage
-----

To create a project using this template::

    mkvirtualenv -p python2 project_name
    workon project_name
    pip install Django
    django-admin.py startproject --template=https://github.com/brutasse/django-project-template/tarball/master --extension=py,rst,template project_name
    cd project_name
    find . -iname "*.template" -exec rename -v ".template" "" {} \;
    pip install -r requirements.txt && pip freeze -l > requirements.txt

Then follow the instructions in the README file.


What follows is the README for projects created using this template.

-----

.. {% endcomment %}
{{ project_name|title }}
========================

Setting up
----------

::

    cd /path/to/project
    add2virtualenv .
    gem install bundle
    bundle install
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    createdb -U postgres project_name
    make syncdb
    make test

Development
-----------

* Running the development server & compass::

      foreman start

  If you need more processes (queue workers, stub mail servers or other
  things), add them to the ``Procfile``.

* Running the tests::

      make test

  Tests are located in the ``tests/`` directory. Create files at will, the
  test runner will auto-detect tests if the file names begin with ``test``.

Deployment
----------

Do **not** use ``foreman`` to deploy apps created this way. Run ``setup.py
sdist``, export the distribution to your own PyPI server and use ``pip`` to
install it on your production machines.

Use ``daemontools``'s ``envdir`` program to manage application secrets.

Use a process watcher such as ``supervisor`` to run the web server. Example::

    /path/to/env/bin/gunicorn {{ project_name }}.wsgi -k gevent -b 127.0.0.1:8000 -w 2

The combination of ``envdir`` and a pip-installable package makes it extremely
simple to automate your deployments.
