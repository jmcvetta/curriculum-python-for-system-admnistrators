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

   $ pip install django

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
