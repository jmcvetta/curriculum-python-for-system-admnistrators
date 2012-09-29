.. highlight:: bash

***************************
Using Third-Party Libraries
***************************

PyPI
====

PyPI_ is the *Python Package Index*.  It provides a central index of Python
packages, any of which can be installed with a single command.

Not to be confused with PyPy_, an alternative Python interpreter.

.. _PyPI: http://pypi.python.org/
.. _PyPy: http://pypy.org/


Installation
============

Use the ``pip`` command to install libraries into a virtual environment.

For example:

.. todo::

   Show virtualenv activation

::

   $ pip install ipython

If you really must install a library system-wide, *please* first look and see if
a reasonable version of the library is available from your system's package
manager.


Finding Packages
================

Google (Bing, etc) is your friend.  So is Pip:

::

   $ pip search mysql
   sqlbean                   - A auto maping ORM for MYSQL and can bind with memcached
   chartio                   - Setup wizard and connection client for connecting MySQL/PostgreSQL databases to Chartio
   tiddlywebplugins.mysql2   - MySQL-based store for tiddlyweb
   MySQL-python              - Python interface to MySQL
   lovely.testlayers         - mysql, postgres nginx, memcached cassandra test layers for use with zope.testrunner
   zest.recipe.mysql         - A Buildout recipe to setup a MySQL database.
   ...
   

Popular Packages
================

Here are some popular, useful packages:

==========================   =======================================================
Package                      Description
==========================   =======================================================
boto                         Python interface to Amazon Web Services
django                       Web application framework
fabric                       SSH library and command line tool
flask                        Lightweight web framework
gevent                       High speed event handling library
gunicorn                     Production webserver
ipython                      Interactive Python shell
psycopg2                     PostgreSQL driver
python-ldap                  Object-oriented API to access LDAP directory servers
requests                     HTTP for humans
restkit                      HTTP resource kit
sphinx                       Documentation tool
==========================   =======================================================


Django Plugins
--------------

These packages extend/enhance the Django framework:

==========================   =======================================================
Package                      Description
==========================   =======================================================
docutils                     Documentation utilities
django-bootstrap-form        Format Django forms to look nice with Twitter Bootstrap 
django-celery                Distributed task queue
django-debug-toolbar         In-browser debugging utility
django-heroku-memcacheify    Automatic Django memcached configuration on Heroku.
django-heroku-postgresify    Automatic Django database configuration on Heroku.
django-social-auth           Authenticate using social account
django-sslify                Require SSL site-wide
django-storages              S3 storage for file attachments
django-templated-email       Template-based email
newrelic                     Cloud-based monitoring service
pillow                       Heroku-compatible imaging library
py-bcrypt                    More secure password hashing
south                        Database migration service
==========================   =======================================================
 
