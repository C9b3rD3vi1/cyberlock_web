from django.conf import settings
from django.conf.urls.static import static
from django.urls import include




from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coreapp.urls')),  # Include app's urls.py
    path('ckeditor/', include('ckeditor_uploader.urls')),
]



# Only add this in development (when DEBUG is True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)