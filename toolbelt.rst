.. highlight:: bash

********
Toolbelt
********


Using the right tools can give a big boost to a programmer's productivity. 

The tools described in this section are available on most platforms.
Installation instructions for `Ubuntu Linux`_ 12.04 are shown.

.. _`Ubuntu Linux`: http://ubuntu.com/


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


Installing Eclipse Plugins
--------------------------

Each Eclipse plugin has an *Update Site* URL, from which it can be installed.

To install a plugin in Eclipse, choose ``Install New Software...`` from the
``Help`` menu.  Click the ``Add...`` button to add a new plugin repository.  Put
the plugin's *Update Site* URL in the ``Location:`` field.

Once you have added the plugin repository, check the box of the plugin you want
to install.  Click ``Next >``, then click thru until it is installed.  Normally
Eclipse will want to restart itself after a new plugin has been installed.


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

Vwrapper
--------

Vrapper is an Eclipse plugin providing VI-keys support.  Only install this
plugin if you are *certain* you want it.

Update site:

   ``http://vrapper.sourceforge.net/update-site/stable``


Working with Virtual Environments
---------------------------------

.. todo:: 

   Research best way for sysadmins, rather than developers, to work with virtualenvs.


Git - Version Control
=====================



.. todo:: 

   Describe common workflow for Git use with sysadmin scripts.  Local & remote
   repos.
   
   Some parts of eBay use private Github - do sysadmins?