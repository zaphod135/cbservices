# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='company',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='contract',
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='purchase_contract',
            field=models.ForeignKey(related_name='purchase_orders', default=1, to='contracts.Contract'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='sell_contract',
            field=models.ForeignKey(related_name='sell_orders', default=1, to='contracts.Contract'),
            preserve_default=False,
        ),
    ]
