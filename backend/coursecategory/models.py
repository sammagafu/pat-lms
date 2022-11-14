from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class ProuctCategory(models.Model):
    categoryname = models.CharField(max_length=160)
    slug = models.SlugField(_("slug"),editable=False,unique=True,null=False,blank=False)
    created_at = models.DateTimeField(editable=False,auto_now_add=True)
    modified_at = models.DateTimeField(blank=True,null=True,editable=False)

    class Meta:
        verbose_name = 'Course Category'
        verbose_name_plural = 'Courses Categories'

    def __str__(self):
        return self.categoryname

    def save(self):
        if not self.id:
            self.created = timezone.now()
        self.modified_at = timezone.now()
        self.slug = slugify(self.categoryname)
        return super().save()

        # if not self.slug:
        #     self.slug = slugify(self.categoryname)
        # return super().save()

    def get_absolute_url(self):
        """Return absolute url for Category."""
        return ('')

class ProductSubCategory(models.Model):
    category = models.ForeignKey(ProuctCategory, verbose_name=_("category"), on_delete=models.CASCADE,related_name="subcategory")
    subcategoryname = models.CharField(max_length=160)
    slug = models.SlugField(_("slug"),editable=False,unique=True)
    created_at = models.DateTimeField(editable=False,auto_now_add=True)
    modified_at = models.DateTimeField(blank=True,null=True,editable=False)

    class Meta:
        verbose_name = _("Course Sub-Category")
        verbose_name_plural = _("Courses Sub-Categories")

    def __str__(self):
        return self.subcategoryname

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified_at = timezone.now()
        if not self.slug:
            self.slug = slugify(self.subcategoryname)
        self.slug = slugify(self.subcategoryname)
        return super(ProductSubCategory,self).save(*args, **kwargs)
        

    def get_absolute_url(self):
        return reverse("SubCategory_detail", kwargs={"pk": self.pk})