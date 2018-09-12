# Generated by Django 2.0 on 2018-09-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PreInterviewModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('currentsalary', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('salaryexpection', models.DecimalField(decimal_places=5, max_digits=100000)),
                ('jointime', models.CharField(max_length=120)),
                ('whyjoin', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeekDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('sun', 'Sunday'), ('mon', 'Monday'), ('tus', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday')], max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='preinterviewmodel',
            name='weekday',
            field=models.ManyToManyField(to='preinterviewqaapp.WeekDay'),
        ),
    ]
