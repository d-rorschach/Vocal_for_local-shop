# Generated by Django 3.1.2 on 2021-01-04 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20210103_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='shop_name',
            new_name='shop',
        ),
    ]
