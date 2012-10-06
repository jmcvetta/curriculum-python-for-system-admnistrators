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
from fabric.api import env
from fabric.api import task
from fabric import tasks


pattern = re.compile(r'up (\d+) days')

#env.hosts = ['localhost', 'sunflower.heliotropic.us']
env.hosts = ['sunflower.heliotropic.us']

@task
def avg_uptime(uts_list):
        res = run('uptime')
        print res
        match = pattern.search(res)
        if match:
            days = int(match.group(1))
            uts_list.append(days)

def main():
    uts_list = []
    tasks.execute(avg_uptime, uts_list)
    if uts_list:
        avg = sum(uts_list) / float(len(uts_list))
        print 'Average uptime: %s days' % avg

if __name__ == '__main__':
    main()
