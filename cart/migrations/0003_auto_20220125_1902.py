# Generated by Django 2.2 on 2022-01-25 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='product',
            new_name='prodt',
        ),
        migrations.RenameField(
            model_name='items',
            old_name='quantity',
            new_name='quan',
        ),
    ]
