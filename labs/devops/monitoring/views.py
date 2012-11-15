from django.views.generic import TemplateView
from monitoring.models import Uptime
from django.db.models import Avg
from django.db.models import Max


# https://docs.djangoproject.com/en/dev/ref/class-based-views/base/#templateview
class UptimeDashboard(TemplateView):
    
    template_name = 'uptime.html'
    
    def get_context_data(self, **kwargs):
        context = super(UptimeDashboard, self).get_context_data(**kwargs)
        latest_ts = Uptime.objects.aggregate(Max('timestamp'))['timestamp__max']
        curr_avg_ut = Uptime.objects.filter(timestamp=latest_ts).aggregate(Avg('minutes'))['minutes__avg']
        context['curr_avg_ut'] = curr_avg_ut
        context['hist_avg_ut'] = Uptime.objects.aggregate(Avg('minutes'))['minutes__avg']
        context['latest_timestamp'] = latest_ts
        context['latest_uts'] = Uptime.objects.filter(timestamp=latest_ts)
        return context