# Generated by Django 2.0 on 2018-09-14 07:51

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('preinterviewqaapp', '0008_auto_20180914_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='preinterviewmodel',
            name='interview_time',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')], default=('morning', 'Morning'), max_length=25),
        ),
    ]