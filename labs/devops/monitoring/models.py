from django.db import models

class Host(models.Model):
    '''
    An internet host
    '''
    hostname = models.CharField(max_length=255, primary_key=True)


class Uptime(models.Model):
    '''
    An uptime reading
    '''
    host = models.ForeignKey(Host)
    timestamp = models.DateTimeField()
    minutes = models.IntegerField(blank=True, null=True)
    error = models.CharField(max_length=512, blank=True, null=True)