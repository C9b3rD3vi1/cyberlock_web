
# import and create django form for contact page and conversation

from django import forms
from.models import ContactMessage, BlogPost, Testimonial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Contact form for sending messages to the company

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
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