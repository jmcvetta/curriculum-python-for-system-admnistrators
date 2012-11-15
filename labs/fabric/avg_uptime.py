# This is Free Software, released under the terms of the X11 License.
# See http://directory.fsf.org/wiki/License:X11 for details.

'''
Query servers for uptime and report the average.
'''

import re
from fabric.api import run
from fabric.api import env
from fabric import tasks

env.hosts = ['localhost', 'sunflower.heliotropic.us']
pattern = re.compile(r'up (\d+) days')

# No need to decorate this function with @task
def uptime():
    res = run('uptime')
    match = pattern.search(res)
    if match:
        days = int(match.group(1))
        env['uts'].append(days)

def main():
    env['uts'] = []
    tasks.execute(uptime)
    uts_list = env['uts']
    if not uts_list:
        return # Perhaps we should print a notice here?
    avg = sum(uts_list) / float(len(uts_list))
    print '-' * 80
    print 'Average uptime: %s days' % avg
    print '-' * 80

if __name__ == '__main__':
    main()
