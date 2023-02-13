# Generated by Django 4.1.5 on 2023-02-12 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CraftBeerInfoApp', '0005_rename_brewery_beer_beerbrewery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='beerBrewery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beers', to='CraftBeerInfoApp.brewery'),
        ),
        migrations.AlterField(
            model_name='brewery',
            name='breweryName',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]