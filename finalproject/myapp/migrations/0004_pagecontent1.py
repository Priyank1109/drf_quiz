# Generated by Django 4.1 on 2022-08-29 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_addproperty_listingprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageContent1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
                ('image', models.FileField(blank=True, upload_to='blog_images')),
            ],
        ),
    ]
