from django.contrib import admin

# import my models
from django.db import models
from . models import Project
from django import forms
from . models import Testimonial, Profile, BlogPost
from . models import Service, ContactMessage, Job, JobApplication
from ckeditor.widgets import CKEditorWidget


class BlogPostAdmin(admin.ModelAdmin):  # Use the regular ModelAdmin
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = BlogPost
        fields = '__all__'




# Register my models

admin.site.register(Project)
admin.site.register(Testimonial)
admin.site.register(Profile)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Service)
admin.site.register(ContactMessage)
admin.site.register(Job)
admin.site.register(JobApplication)


