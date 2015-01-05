from django.views import generic

from .models import Contract


class ReportView(generic.TemplateView):
    template_name = 'report.html'

    def get_context_data(self):
        ids = self.request.GET.get('ids', None)
        return {'contracts': Contract.objects.filter(id__in=ids.split(','))}
