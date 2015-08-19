from django.db import models

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
import django
from colorful.fields import RGBColorField
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Label(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']



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
    color = RGBColorField()
    text = RGBColorField(default='#000000')
    category = models.ManyToManyField(Category)
    #share=models.ManyToManyField(Share)

    def __str__(self):
        return self.note_name











