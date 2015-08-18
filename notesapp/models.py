from django.db import models

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from datetime import datetime
import django

# Create your models here.


class Label(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user=models.OneToOneField(User)

    birthday=models.DateField()
    phone_regex= RegexValidator(regex=r'^[0-9]{3}-? ?[0-9]{7}$' , message="Phone number must be entered in the format: '999-9999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11)
    image= models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

#class Share(models.Model):
#   user = models.CharField(max_length=100)

class Note(models.Model):
    note_name = models.CharField(max_length=200)
    note_body = models.TextField()
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(editable=False, default=django.utils.timezone.now())
    labels=models.ManyToManyField(Label)
    permissions=(('Y', 'Yes'),('N', 'No'),)
    permit=models.CharField(max_length=3, choices=permissions, default='N')
    #share=models.ManyToManyField(Share)

    def __str__(self):
        return self.note_name








