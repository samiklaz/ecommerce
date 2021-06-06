# Generated by Django 3.1.4 on 2020-12-10 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='quantity_type',
            field=models.CharField(choices=[('Cups', 'Cups'), ('Bags', 'Bags'), ('Bottle', 'Bottle'), ('Rubber', 'Rubber'), ('undefined', 'undefined')], default='Cups', max_length=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]