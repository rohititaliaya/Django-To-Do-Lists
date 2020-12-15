from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.
class UserData(models.Model):
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	fname = models.CharField(max_length=200)
	lname = models.CharField(max_length=200)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	Email = models.EmailField(max_length = 254,primary_key=True)
	password = models.CharField(max_length=10)
		
	def __str__(self):
		return self.Email

class Details(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField()
	user = models.ForeignKey(UserData,default=None, on_delete = models.CASCADE)
	
		# desplying object name
	def __str__(self):
		return self.title


class Taskdet(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(UserData,default=None, on_delete = models.CASCADE)
	
		# desplying object name
	def __str__(self):
		return self.title