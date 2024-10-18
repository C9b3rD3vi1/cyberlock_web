

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify





# 1. User Profile (Team members or clients)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    website = models.URLField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.user.username



# Blog Post, This will contain blogs and information about my company
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True, max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it's empty
            self.slug = slugify(self.title)
            unique_slug = self.slug
            num = 1
            # Ensure slug uniqueness by appending a number if it already exists
            while BlogPost.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1
            self.slug = unique_slug
        super(BlogPost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[str(self.pk)])

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title



# Products or Services
# Contains servers and price and availability of th services

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    service_image = models.ImageField(upload_to='service_images/', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



# Portfolio/Projects (Case studies)
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    client = models.CharField(max_length=200)
    project_image = models.ImageField(upload_to='project_images/', blank=True)
    completion_date = models.DateField()
    link = models.URLField(blank=True)
    technologies_used = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title




# Job Listings
# Lists all jobs and opening available at the company

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    



# Testimonials and company reviews


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    feedback = models.TextField()
    rating = models.PositiveIntegerField()  # Rating from 1 to 5
    profile_picture = models.ImageField(upload_to='testimonial_pictures/', blank=True)
    published_date = models.DateField(auto_now_add=True)

    def clean(self):
        if not (1 <= self.rating <= 5):
            raise ValidationError('Rating must be between 1 and 5.')

    def __str__(self):
        return f"{self.name} - {self.company}"

    class Meta:
        ordering = ['-published_date']
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"




# Contact Information and how to reach us directly
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
