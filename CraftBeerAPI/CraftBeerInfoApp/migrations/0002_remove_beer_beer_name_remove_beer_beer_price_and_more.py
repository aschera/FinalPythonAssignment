# Generated by Django 4.1.5 on 2023-01-29 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CraftBeerInfoApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beer',
            name='beer_name',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='beer_price',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='company_name',
        ),
        migrations.AddField(
            model_name='beer',
            name='Amount',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='Country',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='Name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='Nr',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='Percentage',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='Price',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='Type',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='beer_quantity',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
