********************************
Remote control of hosts over SSH
********************************


.. todo::

   Customize (hosts etc) all examples to match student VM setup


subprocess.Popen()
==================

It is possible to control a local ssh session using ``subprocess.Popen()`` if no
libraries are available.  This is a super primative way to do things, and not
recommended if you can avoid it.

Here is an example: [#f1]_

.. literalinclude:: examples/ssh/popen_example.py
   :linenos:
   :lines: 8-


Fabric
======

Fabric is a library and command-line tool for streamlining the use of SSH for
application deployment or systems administration tasks.
Fabric is available for Python 2.5 through 2.7, but not Python 3.x (as of July 2016).

It provides a basic suite of operations for executing local or remote shell
commands (normally or via sudo) and uploading/downloading files, as well as
auxiliary functionality such as prompting the running user for input, or
aborting execution.


Basic Usage
-----------

Typical use involves creating a Python file named ``fabfile.py``, containing one
or more functions, then executing them via the fab command-line tool. Below is a
small but complete ``fabfile.py`` containing a single task:

.. literalinclude:: labs/fabric/fabfile.py
   :lines: 5-


Once a task is defined, it may be run on one or more servers, like so:

.. code-block:: console

   (sysadmin)$ fab -H applebox,linuxbox host_type
   [applebox] run: uname -s
   [applebox] out: Darwin
   [linuxbox] run: uname -s
   [linuxbox] out: Linux
   
   Done.
   Disconnecting from localhost... done.
   Disconnecting from linuxbox... done.


Task arguments
==============

It's often useful to pass runtime parameters into your tasks, just as you might
during regular Python programming. Fabric has basic support for this using a
shell-compatible notation: ``<task name>:<arg>,<kwarg>=<value>,...``. It's
contrived, but let's extend the above example to say hello to you personally:
[#f2]_

::

   def hello(name="world"):
      print("Hello %s!" % name)


By default, calling ``fab hello`` will still behave as it did before; but now
we can personalize it:

.. code-block:: console

   (sysadmin)$ fab hello:name=Jeff
   Hello Jeff!
   
   Done.

Those already used to programming in Python might have guessed that this
invocation behaves exactly the same way:


.. code-block:: console

   (sysadmin)$ fab hello:Jeff
   Hello Jeff!
   
   Done.


For the time being, your argument values will always show up in Python as
strings and may require a bit of string manipulation for complex types such
as lists. Future versions may add a typecasting system to make this easier.


Library Usage
-------------

In addition to use via the fab tool, Fabric’s components may be imported into
other Python code, providing a Pythonic interface to the SSH protocol suite at a
higher level than that provided by e.g. the ssh library (which Fabric itself
uses.) [#f3]_

Consider the case where we want to collect average uptime from a list of hosts:

.. literalinclude:: labs/fabric/avg_uptime.py
   :linenos:
   :lines: 11-
   :emphasize-lines: 18


.. rubric:: Footnotes

.. [#f1] https://gist.github.com/1284249
.. [#f2] http://docs.fabfile.org/en/1.4.2/tutorial.html#task-arguments
.. [#f3] http://stackoverflow.com/a/8166050
