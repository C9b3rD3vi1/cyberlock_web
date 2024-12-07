from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, re_path




from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coreapp.urls')),  # Include app's urls.py
    #path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), # The CKEditor path
]



# Only add this in development (when DEBUG is True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)