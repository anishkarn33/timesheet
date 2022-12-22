from django.db import models
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth import get_user_model
# from django.conf import settings
from django.contrib.auth.models import AbstractUser
# from activity.models import Activitie

# Create your models here.

class User(AbstractUser):

    class meta:
        ordering = ['id']
        name = ('user')
        name_plural = ('users')


    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text= ('Required 150 characters or fewer. Letters and digits only'),
        error_messages={'unique': _("A user with that username already exists."),},)

class UserProfile(models.Model):
    
    email= models.EmailField(
        _('email address'),
        max_length=300, 
        blank=False,
        null=False, 
        error_messages={'unique':("Email already exists"),},),
    user = models.OneToOneField( User, on_delete=models.CASCADE, null=True, related_name='profile'),
    avatar = models.URLField(blank=True, null=True),    
    first_name = models.CharField(max_length=255, blank=True, null=True),
    last_name = models.CharField(max_length=255, blank=True, null=True),
    address = models.CharField(max_length=255, blank=True, null=True),
    nationality = models.CharField(max_length=255, blank=True, null=True)
    

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
        



       

