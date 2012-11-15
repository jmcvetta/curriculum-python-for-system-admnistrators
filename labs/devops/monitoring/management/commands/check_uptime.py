from django.core.management.base import BaseCommand, CommandError
from monitoring.models import Host
from monitoring.models import Uptime

import re
from django.utils import timezone
from django.db.models import Avg
from fabric import tasks
from fabric.api import run
from fabric.api import env
from fabric.api import parallel
from fabric.network import disconnect_all


pattern = re.compile(r'up\s+(?:(\d+) days, \s+)?(\d+):(\d+)')

#env.hosts = [
#    'newyork',
#    'seattle',
#    'localhost',
#    'ebay@sunflower.heliotropic.us',
#    ]


@parallel
def uptime(timestamp):
    host, created = Host.objects.get_or_create(hostname=env.host)
    ut = Uptime(host=host, timestamp=timestamp)
    res = run('uptime')
    match = pattern.search(res)
    if match:
        if match.group(1):
            days = int(match.group(1))
        else:
            days = 0
        hours = int(match.group(2))
        minutes = int(match.group(3))
        minutes += hours * 60
        minutes += days * 24 * 60
        ut.minutes = minutes
    else:
        ut.error = 'Could not parse response: "%s"' % res
    ut.save()


class Command(BaseCommand):
    args = 'Check uptime on all hosts'

    def handle(self, *args, **options):
        timestamp = timezone.now()
        host_list = Host.objects.values_list('hostname', flat=True)
        env.hosts.extend(host_list)
        tasks.execute(uptime, timestamp)
        disconnect_all()
        this_avg_ut = Uptime.objects.filter(timestamp=timestamp).aggregate(Avg('minutes'))['minutes__avg']
        hist_avg_ut = Uptime.objects.aggregate(Avg('minutes'))['minutes__avg']
        print 'Current Average Uptime: %s minutes' % this_avg_ut
        print 'Historical Average Uptime: %s minutes' % hist_avg_ut
