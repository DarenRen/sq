# Generated by Django 3.0 on 2019-12-07 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0008_auto_20191207_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sq',
            name='Age',
            field=models.CharField(choices=[('adult', 'Adult'), ('juvenile', 'Juvenile'), ('', '')], default='', max_length=15),
        ),
    ]
