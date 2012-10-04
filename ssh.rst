********************************
Remote control of hosts over SSH
********************************


``subprocess.Popen()``
======================

It is possible to control a local ssh session using ``subprocess.Popen()`` if no
libraries are available.  This is a super primative way to do things, and not
recommended if you can avoid it.

Here is an example: [1]_

.. literalinclude:: examples/ssh/popen_example.py
   :linenos:
   :lines: 8-
   
.. todo::

   Customize example to match student VM setup



Fabric
======

Fabric is a library and command-line tool for streamlining the use of SSH for
application deployment or systems administration tasks.

It provides a basic suite of operations for executing local or remote shell
commands (normally or via sudo) and uploading/downloading files, as well as
auxiliary functionality such as prompting the running user for input, or
aborting execution.

Typical use involves creating a Python module containing one or more functions,
then executing them via the fab command-line tool. Below is a small but complete
“fabfile” containing a single task:

::

   from fabric.api import run
   
   def host_type():
       run('uname -s')


Once a task is defined, it may be run on one or more servers, like so:

.. code-block:: console

   $ fab -H localhost,linuxbox host_type
   [localhost] run: uname -s
   [localhost] out: Darwin
   [linuxbox] run: uname -s
   [linuxbox] out: Linux
   
   Done.
   Disconnecting from localhost... done.
   Disconnecting from linuxbox... done.

In addition to use via the fab tool, Fabric’s components may be imported into
other Python code, providing a Pythonic interface to the SSH protocol suite at a
higher level than that provided by e.g. the ssh library (which Fabric itself
uses.) [2]_

.. todo::

   Another, perhaps more complicated, Fabric example.


.. rubric:: Footnotes

.. [1] https://gist.github.com/1284249
.. [2] http://docs.fabfile.org/en/1.4.3/index.html