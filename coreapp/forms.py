
# import and create django form for contact page and conversation

from django import forms
from.models import ContactMessage, BlogPost

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