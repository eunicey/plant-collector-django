# Generated by Django 4.2.1 on 2023-05-31 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_watering_options_alter_plant_water_needs_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraCare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('R', 'Repot'), ('F', 'Fertilize'), ('P', 'Remove Pests')], default='F', max_length=1)),
            ],
        ),
    ]
