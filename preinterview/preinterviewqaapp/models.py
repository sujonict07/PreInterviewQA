from django.db import models

# Create your models here.


class WeekDay(models.Model):
    WEEK_DAY_CHOICES = (
        ('sun', 'Sunday'),
        ('mon', 'Monday'),
        ('tus', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
    )
    name = models.CharField(max_length=20,choices=WEEK_DAY_CHOICES, unique=True)

    def __str__(self):
        return self.name


class PreInterviewModel(models.Model):
    name            = models.CharField(max_length=120)
    email           = models.EmailField(max_length=254)
    currentsalary   = models.DecimalField(decimal_places=2, max_digits=10000)
    salaryexpection = models.DecimalField(decimal_places=5, max_digits=100000)
    jointime         = models.CharField(max_length=120)
    whyjoin          = models.TextField(blank=True,null=True)
