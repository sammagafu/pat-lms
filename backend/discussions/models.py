from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


# Create your models here.
class Topic(models.Model):
    course = models.ForeignKey("course.Course", verbose_name=_("Course"), on_delete=models.CASCADE,related_name="course_topic")
    topic = models.CharField(max_length=250,blank=False)
    content = models.TextField(blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="topic_starter")
    slug = models.SlugField(_("URL slug"), unique=True,editable=False)

    def __str__(self):
        return self.topic

    def save(self):
        if not self.id:
            self.slug = slugify(self.topic)
        return super().save()

class Reply(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,related_name="replies")
    repy = models.TextField(blank=False)
    answered = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="repying")
