*****
Tools
*****


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

``virtualenvwrapper`` is a set of extensions to the ``virtualenv`` tool. The
extensions include wrappers for creating and deleting virtual environments and
otherwise managing your development workflow, making it easier to work on more
than one project at a time without introducing conflicts in their dependencies [#f1]_.


.. code-block:: console

   $ sudo apt-get install virtualenvwrapper
   $ mkvirtualenv sysadmin
   New python executable in sysadmin/bin/python
   Installing distribute.............................................................................................................................................................................................done.
   Installing pip...............done.
   virtualenvwrapper.user_scripts creating /home/jason/.virtualenvs/sysadmin/bin/predeactivate
   virtualenvwrapper.user_scripts creating /home/jason/.virtualenvs/sysadmin/bin/postdeactivate
   virtualenvwrapper.user_scripts creating /home/jason/.virtualenvs/sysadmin/bin/preactivate
   virtualenvwrapper.user_scripts creating /home/jason/.virtualenvs/sysadmin/bin/postactivate
   virtualenvwrapper.user_scripts creating /home/jason/.virtualenvs/sysadmin/bin/get_env_details
   (sysadmin)$ pip freeze # A few packages are installed by default
   argparse==1.2.1
   distribute==0.6.24
   wsgiref==0.1.2
   
Note that when the virtualenv is active, its name (in this case "sysadmin") is
prepended to the shell prompt:

.. code-block:: console

   $ # Ordinary shell prompt
   (sysadmin)$ # Virtualenv "sysadmin" is active


If later you have logged out, and want to activate this virtualenv, you can use
the ``workon`` command:

.. code-block:: console

   $ workon sysadmin
   (sysadmin)$

You can deactivate the virtualenv with the ``deactivate`` command:

.. code-block:: console

   (sysadmin)$ deactivate
   $ # Back to normal shell prompt


Location of Virtualenvs
-----------------------

By default, ``virtualenvwrapper`` stores your virtualenvs in ``~/.virtualenvs``.
However you can control this by setting the ``WORKON_HOME`` environment
variable.  This could potentially be used for shared virtualenvs, perhaps with
group write permission.

.. code-block:: bash

   export WORKON_HOME=/path/to/virtualenvs
   

Virtual Environments for Scripts
================================

There are several ways you can run scripts that rely on a virtualenv:

* Use Fabric's ``prefix()`` `context manager`__ when calling the script remotely:: 

   def task():
       with prefix('workon sysadmin'):
           run('uptime')
           run('uname -a')

__ http://docs.fabfile.org/en/1.4.3/api/core/context_managers.html

* Have whatever is calling your script (``cron`` etc) call ``workon`` first.

* Specify your virtualenv's Python interpreter directly in the script's bangline.  

* Use a bash script as a wrapper.  Ugly, but sometimes convenient.


Eclipse IDE
===========

Eclipse is a powerful IDE - an integrated development environment.  It provides
valuable tools for understanding, browsing, and refactoring your code.  

Out of the box, Eclipse does not support Python.  However Eclipse is a plugin-based system, 
and there are excellent tools available for Python development.


Aptana / PyDev
--------------

The Python plugin for Eclipse, called *PyDev*, is now part of `Aptana Studio`_.
Aptana can be installed as a seperate download, or as an Eclipse plugin.  For
convenience we will download the whole application.

   http://aptana.com/products/studio3/download

.. _`Aptana Studio`: http://aptana.com/


Installing Eclipse Plugins
--------------------------

Each Eclipse plugin has an *Update Site* URL, from which it can be installed.

To install a plugin in Eclipse, choose ``Install New Software...`` from the
``Help`` menu.  Click the ``Add...`` button to add a new plugin repository.  Put
the plugin's *Update Site* URL in the ``Location:`` field.

Once you have added the plugin repository, check the box of the plugin you want
to install.  Click ``Next >``, then click thru until it is installed.  Normally
Eclipse will want to restart itself after a new plugin has been installed.


Vwrapper
--------

Vrapper is an Eclipse plugin providing VI-keys support.  Only install this
plugin if you are *certain* you want it.

Update site:

   ``http://vrapper.sourceforge.net/update-site/stable``


Git - Version Control
=====================

.. todo:: 

   Describe common workflow for Git use with sysadmin scripts.  Local & remote
   repos.
   


.. rubric:: Footnotes


.. [#f1] http://www.doughellmann.com/projects/virtualenvwrapper/