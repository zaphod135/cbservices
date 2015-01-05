from django.conf.urls import patterns, url

from .views import ReportView


urlpatterns = patterns(
    '',
    url(r'report/', ReportView.as_view(), name='contracts_contract_report')
)
