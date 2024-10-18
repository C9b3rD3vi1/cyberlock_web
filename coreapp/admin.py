from django.contrib import admin

# Register your models here.

from . models import Project
from . models import Testimonial, Profile, BlogPost
from . models import Service, ContactMessage, Job




# Register my models

admin.site.register(Project)
admin.site.register(Testimonial)
admin.site.register(Profile)
admin.site.register(BlogPost)
admin.site.register(Service)
admin.site.register(ContactMessage)
admin.site.register(Job)

