# Generated by Django 4.1 on 2022-08-31 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_addproperty_adminuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addproperty',
            name='adminuser',
        ),
    ]
