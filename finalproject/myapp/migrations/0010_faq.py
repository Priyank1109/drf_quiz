# Generated by Django 4.1 on 2022-08-30 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_aboutus_alter_adminuser_terms_confirmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=50)),
            ],
        ),
    ]
