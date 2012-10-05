# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.
#
#-------------------------------------------------------------------------------
#
# Query servers for uptime, and maintain a running average.
#
#-------------------------------------------------------------------------------


import re
from fabric.api import run


uptimes = []
pattern = re.compile(r'up (\d+) days')

def uptime():
    res = run('uptime')
    match = pattern.search(res)
    if match:
        days = int(match.group(1))
        uptimes.append(days)
    avg = sum(uptimes) / float(len(uptimes))
    print 'Average uptime: %s days' % avg

