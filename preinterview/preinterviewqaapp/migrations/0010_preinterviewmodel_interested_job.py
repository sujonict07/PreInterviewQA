# Generated by Django 2.0 on 2018-09-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preinterviewqaapp', '0009_preinterviewmodel_interview_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='preinterviewmodel',
            name='interested_job',
            field=models.CharField(choices=[('select1', 'select 1'), ('select2', 'select 2')], default=('select1', 'select 1'), max_length=5),
        ),
    ]