# Generated by Django 4.1 on 2022-08-31 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_aboutus_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproperty',
            name='adminuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='myapp.adminuser'),
        ),
    ]
