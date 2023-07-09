# Generated by Django 4.0.3 on 2022-04-15 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadservice', '0002_customerservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarEngineers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_number', models.CharField(max_length=255)),
                ('garage_location', models.CharField(choices=[('location', 'location'), ('GreaterAccraRegion', 'GreaterAccraRegion'), ('CenterRegion', 'CenterRegion'), ('AhafoRegion', 'AhafoRegion'), ('AshantiRegion', 'AshantiRegion'), ('BonoEastRegion', 'BonoEastRegion'), ('BrongAhafoRegion', 'BrongAhafoRegion'), ('VoltaRegion', 'VoltaRegion'), ('OtiRegion', 'OtiRegion'), ('SavannahRegion', 'SavannahRegion'), ('UpperEastRegion', 'UpperEastRegion'), ('WesternRegion', 'WesternRegion'), ('NorthernRegion', 'NorthernRegion')], default='location', max_length=40)),
            ],
        ),
    ]
