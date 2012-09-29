.. highlight:: bash

********
Toolbelt
********


Using the right tools can give a big boost to a programmer's productivity. 

The tools described in this section are available in most development
environments.  Installation instructions for Ubuntu 12.04 are shown.


Virtual Environments
====================

A virtual environment is a local Python environment isolated from the
system-wide environment.


virtualenv
----------

The term "virtualenv" can refer to the command ``virtualenv``, used to create a 
virtual environment, or to the virutal environment itself.

::
  
  $ sudo apt-get install python-virtualenv
  

virtualenvwrapper
-----------------

.. todo::

   Is ``virtualenvwrapper`` appropriate for system administration scripts?
   

``virtualenvwrapper`` is a set of extensions to the ``virtualenv`` tool. The
extensions include wrappers for creating and deleting virtual environments and
otherwise managing your development workflow, making it easier to work on more
than one project at a time without introducing conflicts in their dependencies [#]_.

.. [#] http://www.doughellmann.com/projects/virtualenvwrapper/

::

   $ sudo apt-get install virtualenvwrapper


Eclipse IDE
===========

Eclipse is a powerful IDE - an integrated development environment.  It provides
valuable tools for understanding, browsing, and refactoring your code.  

Out of the box, Eclipse does not support Python.  However Eclipse is a plugin-based system, 
and there is an excellent plugin available for Python development.

::

   $ sudo apt-get install eclipse


Aptana / PyDev
--------------

The Python plugin for Eclipse, called *PyDev*, is now part of `Aptana
Studio`_.
It can be installed as a seperate download, or as
an Eclipse plugin.  We will use the Eclipse plugin so the package manager
handles the many Eclipse dependencies for us.

Update site: 

   ``http://download.aptana.com/studio3/plugin/install``
   
.. _`Aptana Studio`: http://aptana.com/

vwrapper
--------

Vrapper is an Eclipse plugin providing VI-keys support.  Only install this
plugin if you are *certain* you want it.

Update site:

   ``http://vrapper.sourceforge.net/update-site/stable``


Working with Virtual Environments
---------------------------------


Git - Version Control
=====================
