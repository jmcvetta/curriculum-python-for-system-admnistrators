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

Here are a few popular, useful packages:

==========================   =======================================================
Package                      Description
==========================   =======================================================
django                       Web application framework
psycopg2                     PostgreSQL driver
ipython                      Interactive Python shell
gunicorn                     Production webserver
gevent                       High speed event handling library
py-bcrypt                    More secure password hashing
docutils                     Documentation utilities
boto                         Python interface to Amazon Web Services
==========================   =======================================================

.. todo::

   Add some more sysadmin-focused packages


Django Plugins
--------------

These packages extend/enhance the Django framework.

==========================   =======================================================
Package                      Description
==========================   =======================================================
south                        Database migration service
dj_database_url              Get database URL from Heroku environment variables
pillow                       Heroku-compatible imaging library
django-social-auth           Authenticate using social account
py-bcrypt                    More secure password hashing
django-bootstrap-form        Format Django forms to look nice with Twitter Bootstrap 
django-storages              S3 storage for file attachments
boto                         Python interface to Amazon Web Services
newrelic                     Cloud-based monitoring service
django-celery                Distributed task queue
django-templated-email       Template-based email
django-debug-toolbar         In-browser debugging utility
django-sslify                Require SSL site-wide
django-heroku-memcacheify    Automatic Django memcached configuration on Heroku.
django-heroku-postgresify    Automatic Django database configuration on Heroku.
==========================   =======================================================
 

.. todo::

   Add links to popular packages.