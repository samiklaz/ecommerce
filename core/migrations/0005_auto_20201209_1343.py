# Generated by Django 3.1.4 on 2020-12-09 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.CharField(choices=[('Cups', 'Cups'), ('Bags', 'Bags'), ('Bottle', 'Bottle'), ('Rubber', 'Rubber'), ('undefined', 'undefined')], default='Cups', max_length=10),
        ),
    ]
