# Generated by Django 4.1 on 2022-08-31 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_addproperty_adminuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproperty',
            name='createdby',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
