from django.contrib import admin

# import my models
from django.db import models
from . models import Project
from . models import Testimonial, Profile, BlogPost
from . models import Service, ContactMessage, Job, JobApplication
from ckeditor.widgets import CKEditorWidget


class BlogPostAdmin(admin.ModelAdmin):  # Use the regular ModelAdmin
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }




# Register my models

admin.site.register(Project)
admin.site.register(Testimonial)
admin.site.register(Profile)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Service)
admin.site.register(ContactMessage)
admin.site.register(Job)
admin.site.register(JobApplication)


