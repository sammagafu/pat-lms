from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Course(models.Model):
    """ course model """
    name = models.CharField(null=False, max_length=30, default='online course')
    cover = ResizedImageField(upload_to = 'profile/images/%Y/%m/%d',verbose_name=_("Profile Image"),size=[600, 400], crop=['middle', 'center'],default='default.jpg')
    description = models.CharField(max_length=1000)
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Course Author'
    )


class Lesson(models.Model):
    """ lesson model """
    title = models.CharField(max_length=200, default="title")
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()

class CourseVideo(models.Model):
    """ lesson model """
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=200, default="title")
    video = models.URLField()




class CourseEnrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name="enrolledcourse")
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='student',verbose_name='Course Author')

    class Meta:
        unique_together = ('course', 'author',)
