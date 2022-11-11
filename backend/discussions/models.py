from django.db import models
from quiz.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    topic = models.CharField(max_length=250,blank=False)
    content = models.TextField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic

class Reply(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    repy = models.TextField(blank=False)
    answered = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
