# Generated by Django 4.1 on 2022-08-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_adminuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminuser',
            name='terms_confirmed',
            field=models.BooleanField(null=True),
        ),
    ]