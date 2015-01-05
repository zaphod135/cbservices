from django import http
from django.core.urlresolvers import reverse
from django.contrib import admin

from .models import (
    Company,
    Contract,
    Product,
    PurchaseOrder
)


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'purchase_contract', 'sell_contract', 'amount', )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('description', )


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ContractAdmin(admin.ModelAdmin):
    actions = ['generate_reports', ]
    list_display = ('number', 'type', 'amount', 'product', 'company', )

    def generate_reports(self, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        return http.HttpResponseRedirect('{}?ids={}'.format(
            reverse('contracts_contract_report'),
            ','.join(selected)
        ))
    generate_reports.short_description = "Generate reports for the selected contracts."


admin.site.register(Contract, ContractAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
