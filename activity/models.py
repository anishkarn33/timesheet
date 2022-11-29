from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Activitie(models.Model):
    CHOICES =(
        ("Todo", "To Do"),
        ("proress", "In Progress"),
        ("review", "Review"),
        ("done", "Done"),
    )
    title =  models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    estimation= models.TextField (max_length=100)
    asignee= models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    status= models.TextField(choices=CHOICES)

    def __str__ (self):
        return f'{self.title} {self.description}  by {self.estimation} to {self.asignee} {self.status}'