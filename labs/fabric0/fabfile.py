# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.


from fabric.api import run

def host_type():
    run('uname -s')
