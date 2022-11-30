from django.contrib import admin
from .models import Lesson,Course,CourseDocuments,CourseVideo

# Register your models here.
class CourseVideoInline(admin.StackedInline):
    model = CourseVideo

class CourseDocumentsInline(admin.StackedInline):
    model = CourseDocuments
@admin.register(Lesson)
class Lesson(admin.ModelAdmin):
    inlines = [CourseDocumentsInline,CourseVideoInline]

admin.site.register(Course)