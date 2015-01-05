from django.db import models


class TimestampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(TimestampedModel):
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.description


class Company(TimestampedModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'companies'

    def __unicode__(self):
        return self.name


class Contract(TimestampedModel):
    PURCHASE_TYPE = 'p'
    SELL_TYPE = 's'

    TYPE_CHOICES = (
        (PURCHASE_TYPE, 'Purchase'),
        (SELL_TYPE, 'Sell'),
    )

    number = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    amount = models.PositiveIntegerField(help_text="The amount in pounds.")
    product = models.ForeignKey(Product)
    company = models.ForeignKey(Company)

    def __unicode__(self):
        return "Contract #{} | {}".format(self.number, self.company)

    def amount_as_metric_tons(self):
        return self.amount * 0.00045359237

    def purchase_order_report(self):
        if self.type == Contract.PURCHASE_TYPE:
            orders = self.purchase_orders.all()
        else:
            orders = self.sell_orders.all()

        remaining = self.amount
        for order in orders:
            remaining = remaining - order.amount
            order.remaining = remaining

        return orders


class PurchaseOrder(TimestampedModel):
    number = models.CharField(max_length=50)
    purchase_contract = models.ForeignKey(Contract, related_name='purchase_orders')
    sell_contract = models.ForeignKey(Contract, related_name='sell_orders')
    amount = models.PositiveIntegerField(help_text="The amount in pounds.")

    def __unicode__(self):
        return "PO #{}, {} -> {}, {}".format(
            self.number,
            self.purchase_contract.company,
            self.purchase_contract.company,
            self.amount
        )
