# Generated by Django 4.0.3 on 2022-04-14 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roadservice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carName', models.CharField(max_length=254)),
                ('phoneNumber', models.CharField(max_length=254)),
                ('location', models.CharField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('message', models.TextField()),
                ('customerService', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
