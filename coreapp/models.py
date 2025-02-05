
# my database models and backend code
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.urls import reverse
from django.utils.timezone import now
from django.utils.text import slugify
from django.core.validators import URLValidator
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# 1. User Profile (Team members or clients)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = RichTextUploadingField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    # validation rules for the profile urls and website
    website = models.URLField(blank=True, validators=[URLValidator()])
    github = models.URLField(blank=True, validators=[URLValidator()])
    linkedin = models.URLField(blank=True, validators=[URLValidator()])

    def __str__(self):
        return self.user.username

    def is_complete(self):
        return all([self.bio, self.profile_picture, self.website, self.github, self.linkedin])



# Blog Post, This will contain blogs and information about my company
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(null=True, blank=False)
    #content = models.TextField()
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
        permissions = [
            ("can_create_post", "Can create blog post"),
            ("can_update_post", "Can update blog post"),
            ("can_delete_post", "Can delete blog post"),
        ]


    def __str__(self):
        return self.title
    

# Allow users to comment on blog posts content
class Comment(models.Model):
    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'


# Products or Services
# Contains services and price and availability of th services
class Service(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('custom', 'Custom Services'),# Custom Services
        ('cloud', 'Cloud Services'),
        ('standard', 'Standard Services'),  # All other services not classified should be treated as standard
    ]
    
    name = models.CharField(max_length=200)
    description = RichTextUploadingField(blank=False, null=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    service_image = models.ImageField(upload_to='service_images/', blank=True)
   # slug = models.SlugField(unique=True, max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    service_type = models.CharField(max_length=10, choices=SERVICE_TYPE_CHOICES, default='standard')

    class Meta:
        verbose_name_plural = "Services"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - ${self.price if self.price is not None else 'N/A'}"



# Portfolio/Projects (Case studies)
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextUploadingField(null=True, blank=True)
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
    description = RichTextUploadingField(blank=False, null=False)
    requirements = RichTextUploadingField(blank=False, null=False)
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
    name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    subject = models.CharField(max_length=200, verbose_name="Subject")
    message = models.TextField(verbose_name="Message")

    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"

    class Meta:
        ordering = ['-sent_at']  # Order messages by most recent first
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def clean(self):
        # Custom validation for message length
        if len(self.message) < 10:
            raise ValidationError("Message must be at least 10 characters long.")


# Save job application  and allowing user to make job application
class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user applying
    job = models.ForeignKey(Job, on_delete=models.CASCADE, default=1)  # Link to the job being applied for
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    resume = models.FileField(upload_to='resumes/', blank=False)
    cover_letter = models.TextField(blank=False)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job.title + " - " + self.user.username
    
'''

#  Ticketing system for user to create and report issues or enquiry issues
# Define categories for tickets (optional)
class TicketCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Define the priority levels for tickets (optional)
class TicketPriority(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Define the ticket model
class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(TicketCategory, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.ForeignKey(TicketPriority, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

# Define comments on tickets
class TicketComment(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.ticket.subject}"

'''