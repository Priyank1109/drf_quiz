# Generated by Django 4.1 on 2022-08-29 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproperty',
            name='image',
            field=models.FileField(blank=True, upload_to='blog_images'),
        ),
    ]
