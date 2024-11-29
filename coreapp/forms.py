
# import and create django form for contact page and conversation

from django import forms
from.models import ContactMessage, BlogPost, Testimonial, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import JobApplication, Comment
from ckeditor.widgets import CKEditorWidget


# Contact form for sending messages to the company

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        #content = forms.CharField(widget=CKEditorWidget())
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }


# blog post form
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }



# Create the user logins form using CustomUser
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user


# Testimonial form from admin and different users based on their expectations and experience
class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'company', 'feedback', 'rating', 'profile_picture']



# profile form  fields to allow user to enter and update their profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture', 'website', 'github', 'linkedin']


# job application form  
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'cover_letter', 'resume']

# User blog comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }