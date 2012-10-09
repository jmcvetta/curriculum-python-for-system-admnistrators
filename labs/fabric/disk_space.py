#!/usr/bin/env python
'''
Lab - Disk Space

* Use Fabric to query a set of "remote" hosts (actually 
  they'll be aliases to localhost, but...)
* Query the host for disk space on the root partition
* If disk space is below a configurable threshold, say 1GB, 
  then print a warning.
* When all hosts have been queried, print average disk space
  available.
'''

THRESHOLD = 1048576000 # 1GB in KB


import sys
from fabric import tasks
from fabric.api import env
from fabric.api import run
from fabric.network import disconnect_all
from fabric.exceptions import NetworkError

env.hosts = ['newyork', 'seattle', 'localhost', 'foobar']

def get_disk_space(host_list, error_list):
    #result = run('df -k / | grep dev')
    try:
        result = run('df -k / | grep dev')
    except NetworkError as err:
        print "NETWORK ERROR: %s" % err
        return
    try:
        free_space_str = result.rsplit()[3]
        free_space = int(free_space_str)
    except (ValueError, IndexError) as err:
        msg = 'Bad server response: "%s"\n' % result
        sys.stderr.write(msg)
        err_tuple = (env.host_string, result, err)
        error_list.append(err_tuple)
        return
    host_tuple = (env.host_string, free_space)
    host_list.append(host_tuple)

def main():
    host_list = []
    error_list = []
    tasks.execute(get_disk_space, host_list, error_list)
    if error_list:
        print '-' * 80
        print 'ERRORS:'
        print
        for item in error_list:
            print '%s %s %s' % item
        print
    if not host_list:
        print 'ERROR: something bad happened, no host data'
        return
    low_space_list = []
    total_space = 0
    for host, freespace in host_list:
        total_space += freespace
        if freespace <= THRESHOLD:
            low_space_list.append((host, freespace))
    avg_free_space = total_space / len(host_list)
    if low_space_list:
        print '-' * 80
        print 'LOW DISK SPACE:'
        for item in low_space_list:
            print '%-32s %s' % item
    print
    print 'AVERAGE FREE DISK SPACE: %s' % avg_free_space
    disconnect_all()
    
    
    

if __name__ == '__main__':
    main()