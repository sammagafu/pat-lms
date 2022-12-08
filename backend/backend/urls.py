
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/',include('accounts.urls')),
    path('api/v1/course/',include('course.urls')),
    path('api/v1/category/',include('coursecategory.urls')),
    path('api/v1/discussion/',include('discussions.urls')),
    path('api/v1/quiz/',include('quiz.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
