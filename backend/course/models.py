from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.utils import timezone
import datetime

# Create your models here.
class Course(models.Model):
    """ course model """
    name = models.CharField(null=False, max_length=30, default='online course')
    cover = ResizedImageField(upload_to = 'profile/images/%Y/%m/%d',verbose_name=_("Course Cover Image"),size=[600, 400], crop=['middle', 'center'],default='default.jpg')
    description = models.CharField(max_length=1000)
    slug = models.SlugField(_("Slug"),editable=False,unique=True)
    is_published = models.BooleanField(_("published"),default=False)
    courseprice = models.DecimalField(_("Course Price"), max_digits=10, decimal_places=2,default=10000)
    pub_date = models.DateField(default=datetime.date.today)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Course Author'
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        return super().save()


class Lesson(models.Model):
    """ lesson model """
    title = models.CharField(max_length=200, default="title")
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name="lesson")
    content = models.TextField(_("What will they learn"))

    def __str__(self):
        return self.title

class CourseVideo(models.Model):
    """ lesson model """
    lesson = models.OneToOneField(Lesson, verbose_name=_("Course Lesson"), on_delete=models.CASCADE,related_name="courseVideo")
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=200, default="title")
    video = models.URLField()


class CourseDocuments(models.Model):
    lesson = models.OneToOneField(Lesson, verbose_name=_("Course Lesson"), on_delete=models.CASCADE,related_name="courseDocument")
    document = models.FileField(_("Supportind Document"), upload_to=None, max_length=100)


class CourseEnrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name="enrolledcourse")
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='student',verbose_name='Course Author')
    is_paid = models.BooleanField(_("Paid Course"),default=False)

    class Meta:
        unique_together = ('course', 'author',)
