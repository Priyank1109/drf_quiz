# Generated by Django 4.1 on 2022-08-26 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mlsnumber', models.CharField(max_length=50)),
                ('listingprice', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('streetaddress1', models.CharField(max_length=50, null=True)),
                ('streetaddress2', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('postalcode', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]