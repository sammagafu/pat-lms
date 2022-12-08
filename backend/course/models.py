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
    name = models.CharField(null=False, max_length=180, default='online course')
    cover = ResizedImageField(upload_to = 'profile/images/%Y/%m/%d',verbose_name=_("Course Cover Image"),size=[600, 400], crop=['middle', 'center'],default='default.jpg')
    description = models.TextField()
    slug = models.SlugField(_("Slug"),editable=False,unique=True)
    is_published = models.BooleanField(_("published"),default=False)
    courseprice = models.DecimalField(_("Course Price"), max_digits=10, decimal_places=2,default=10000)
    points = models.IntegerField(_("GPD Points"),default=5)
    pub_date = models.DateField(default=datetime.date.today)
    introvideo = models.TextField(default='<iframe width="560" height="315" src="https://www.youtube.com/embed/ddsebipcm7M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',null=True,blank=True)
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
    video = models.TextField("Embed video Url")

    def __str__(self):
        return self.lesson.title


class CourseDocuments(models.Model):
    title = models.CharField(max_length=200, default="document name")
    lesson = models.OneToOneField(Lesson, verbose_name=_("Course Lesson"), on_delete=models.CASCADE,related_name="courseDocument")
    document = models.FileField(_("Supportind Document"), upload_to=None, max_length=100)

    def __str__(self):
        return self.title


class CourseEnrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name="enrolledcourse")
    student = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='student',verbose_name='Course Author')
    is_paid = models.BooleanField(_("Paid Course"),default=False)

    class Meta:
        unique_together = ('course', 'student',)

    def __str__(self):
        return self.course.name


class PaymentDetails(models.Model):
    pass
