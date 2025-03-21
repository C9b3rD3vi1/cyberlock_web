from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, re_path
from django.views.generic.base import TemplateView

from django.contrib import admin
from django.urls import path


# Define the main URL patterns for the project.
urlpatterns = [
    path('custom-dashboard/', admin.site.urls),
    path('', include('coreapp.urls')),  # Include app's urls.py
    #path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), # The CKEditor path
    path('accounts/', include('allauth.urls')),  # Include allauth urls

]


# Debug mode enabled
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)