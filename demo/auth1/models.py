from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.

@python_2_unicode_compatible
class Department(models.Model):
    department_name = models.CharField(max_length=200)
    no_of_employees = models.IntegerField(default=0)
    def __str__(self):
        return self.department_name
    


@python_2_unicode_compatible    
class Employees(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    department_name = models.CharField(max_length=200)
    join_date = models.DateTimeField('date joined')
    def __str__(self):
        return self.user_name
    def has_joined_recently(self):
        return self.join_date >= timezone.now() - datetime.timedelta(days=1)




