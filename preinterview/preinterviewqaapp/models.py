from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

WEEK_DAY_CHOICES = (
    ('sun', 'Sunday'),
    ('mon', 'Monday'),
    ('tus', 'Tuesday'),
    ('wed', 'Wednesday'),
    ('thu', 'Thursday'),
    ('fri', 'Friday'),
    ('sat', 'Saturday'),
)

DAY_TIME_CHOICES = (
    ('morning', 'Morning'),
    ('afternoon', 'Afternoon'),
    ('evening', 'Evening'),
)


JOB_CHOICES = (
   ('android', 'Android app developer'),
   ('php', 'PHP Expert (CakePHP/CodeIgniter)'),
   ('python','Python Expert'),
   ('react','React Native Expert'),
   ('web','Web Designer (Photoshop/HTML/CSS/Flash)'),
   ('iphone','iPhone app developer'),
)


class PreInterviewModel(models.Model):
    name                = models.CharField(max_length=120)
    email               = models.EmailField(max_length=254)
    current_salary      = models.DecimalField(decimal_places=2, max_digits=10000)
    salary_expection    = models.DecimalField(decimal_places=5, max_digits=100000)
    join_time           = models.CharField(max_length=120)
    why_join            = models.TextField(blank=True,null=True)
    week_day            = MultiSelectField(choices=WEEK_DAY_CHOICES, default=WEEK_DAY_CHOICES[0])
    interview_time      = MultiSelectField(choices=DAY_TIME_CHOICES, default=DAY_TIME_CHOICES[0])
    interested_job      = models.CharField(choices=JOB_CHOICES, max_length=128)


