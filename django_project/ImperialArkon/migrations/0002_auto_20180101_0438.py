# Generated by Django 2.0 on 2018-01-01 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImperialArkon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='about_applicant',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='why_to_join',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
