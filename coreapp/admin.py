from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

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

# Admin actions, Mark selected stories as published or unpublished
@admin.action(description='Mark selected stories as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


@admin.action(description='Mark selected stories as unpublished')
def make_unpublished(modeladmin, request, queryset):
    queryset.update(status='d')


# Admin actions, Mark selected users as active or inactive
@admin.action(description='Mark user as active')
def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)

@admin.action(description='Mark user as inactive')
def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)



class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    actions = [make_active, make_inactive]

# Register my models

admin.site.register(Project)
admin.site.register(Testimonial)
admin.site.register(Profile)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Service)
admin.site.register(ContactMessage)
admin.site.register(Job)
admin.site.register(JobApplication)
# Register the User model with the UserAdmin class to customize the admin interface.
admin.site.unregister(User)  # Unregister the default User admin
admin.site.register(User, UserAdmin)



