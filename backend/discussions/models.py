from django.db import models
from quiz.models import Category
from django.conf import settings

# Create your models here.
class Topic(models.Model):
    topic = models.CharField(max_length=250,blank=False)
    content = models.TextField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="course_category")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="topic_starter")

    def __str__(self):
        return self.topic

class Reply(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,related_name="reply_topic")
    repy = models.TextField(blank=False)
    answered = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="repying")
