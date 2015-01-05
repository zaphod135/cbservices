# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('number', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=1, choices=[(b'p', b'Purchase'), (b's', b'Sell')])),
                ('amount', models.PositiveIntegerField(help_text=b'The amount in metric tons.')),
                ('company', models.ForeignKey(to='contracts.Company')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('number', models.CharField(max_length=50)),
                ('amount', models.PositiveIntegerField(help_text=b'The amount in metric tons.')),
                ('company', models.ForeignKey(to='contracts.Company')),
                ('contract', models.ForeignKey(to='contracts.Contract')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contract',
            name='product',
            field=models.ForeignKey(to='contracts.Product'),
            preserve_default=True,
        ),
    ]
