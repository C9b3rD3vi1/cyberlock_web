
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User, Service, BlogPost, Testimonial, ContactMessage, Job, Project
from .forms import ContactMessageForm, BlogPostForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
import logging

from .forms import CustomUserCreationForm






# Home page view functions
def home(request):
    """
    This function renders the home page of the website.

    :param request: The HTTP request object containing the necessary information for rendering the page.
    :type request: django.http.HttpRequest

    The function retrieves the latest 3 active services, the latest 3 projects, the latest 3 blog posts, and the latest 3 testimonials from the database. It then passes these objects to the template context for display. Finally, it renders the 'home.html' template with the context variables.

    :return: A Django response object. The function returns a rendered HTTP response containing the 'home.html' template with the services, projects, blog posts, and testimonials as context variables.
    :rtype: django.http.HttpResponse
    """
    services = Service.objects.filter(is_active=True)[:3]  # Get the latest 3 services
    projects = Project.objects.all()[:3]  # Get the latest 3 projects
    blog_posts = BlogPost.objects.all().order_by('-published_date')[:3]  # Get the latest 3 blog posts
    testimonials = Testimonial.objects.all()[:3]  # Get the latest 3 testimonials

    context = {
        'services': services,
        'projects': projects,
        'blog_posts': blog_posts,
        'testimonials': testimonials,
    }

    return render(request, 'home.html', context)




def service_list(request):
    """
    This function renders the service list page.

    :param request: The HTTP request object containing the necessary information for rendering the page.
    :type request: django.http.HttpRequest

    The function retrieves the latest 3 active services from the database and passes them to the template context for display. It then renders the 'service_list.html' template with the services as a context variable.

    :return: A Django response object. The function returns a rendered HTTP response containing the 'service_list.html' template with the services as a context variable.
    :rtype: django.http.HttpResponse
    """
    services = Service.objects.filter(is_active=True)  # Get the latest 3 services


    # Fetch the service based on its slug
    return render(request, 'service_list.html', {"services": services})




def portfolio(request):

    projects = Project.objects.all()

    return render(request, 'portfolio.html', {'projects': projects})




def blog_list(request):

    blog_post = BlogPost.objects.all()
    return render(request, 'blog_post.html', {"blog_post":blog_post})




def job_list(request):
    """
    This function renders the job list page.

    :param request: The HTTP request object containing the necessary information for rendering the page.
    :type request: django.http.HttpRequest

    The function retrieves all job listings from the database and orders them by their 'is_open' field in descending order. It then fetches the first 15 job listings and passes them to the template context for display. Finally, it renders the 'job_list.html' template with the job listings as a context variable.

    :return: A Django response object. The function returns a rendered HTTP response containing the 'job_list.html' template with the job listings as a context variable.
    :rtype: django.http.HttpResponse
    """
    jobs = Job.objects.all().order_by('-is_open')
    return render(request, 'job_list.html',{"jobs": jobs})




def about(request):

    return render(request, 'about.html')



def testimonial_list(request):
    """
    This function renders the testimonial list page.

    :param request: The HTTP request object containing the necessary information for rendering the page.
    :type request: django.http.HttpRequest

    The function retrieves all testimonials from the database and passes them to the template context for display. It then renders the 'testimonial_list.html' template with the testimonials as a context variable.

    :return: A Django response object. The function returns a rendered HTTP response containing the 'testimonial_list.html' template with the testimonials as a context variable.
    :rtype: django.http.HttpResponse
    """
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonial_list.html', {'testimonials': testimonials})




def blog_post_list(request):
    posts = BlogPost.objects.all().order_by('-published_date')
    return render(request, 'blog_post_list.html', {'posts': posts})

def blog_post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_post_detail.html', {'post': post})




# contant form for contactinfo and sending information to my company
def contact_form(request):
    """
    This function handles the contact form submission and rendering.

    :param request: The HTTP request object containing the form data.
    :type request: django.http.HttpRequest

    If the request method is POST, the function validates the form data, saves the form if valid, and redirects to the success page.
    If the request method is not POST, the function creates an empty form and renders the contact form template with the form.

    :return: A Django response object. If the request method is POST and the form is valid, it redirects to the success page. Otherwise, it renders the contact form template with the form.
    :rtype: django.http.HttpResponse
    """
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactMessageForm()
    
    return render(request, 'contact_form.html', {'form': form})





# Return rresponse after successful contact and information sharing
def contact_success(request):
    return render(request, 'contact_success.html')


@login_required
def blog_post_create(request):
    """
    This function handles the creation of a new blog post.

    :param request: The HTTP request object containing the form data.
    :type request: django.http.HttpRequest

    If the request method is POST, the function checks if the user is authenticated. If the user is authenticated, it creates a form with the existing blog post data, validates the form data, saves the form if valid, and redirects to the blog post detail page. If the request method is not POST, it creates an empty form and renders the blog post form template with the form.

    :return: A Django response object. If the request method is POST and the form is valid, it redirects to the blog post detail page. Otherwise, it renders the blog post form template with the form.
    :rtype: django.http.HttpResponse
    """
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = BlogPostForm(request.POST)
            if form.is_valid():
                blog_post = form.save(commit=False)
                blog_post.author = request.user
                blog_post.save()
                logging.info(f"Blog post created by {request.user.username}: {blog_post.title}")
            
                # Redirect or render as necessary
        else:
            return redirect('login')  # Redirect to login page if not authenticated
    else:       
        form = BlogPostForm()
    return render(request, 'blog_post_form.html', {'form': form})




@login_required
def blog_post_update(request, pk):
    """
    This function handles the update of a blog post.

    :param request: The HTTP request object containing the form data.
    :type request: django.http.HttpRequest
    :param pk: The primary key of the blog post to be updated.
    :type pk: int

    The function retrieves the blog post with the given primary key. If the request method is POST, it creates a form with the existing blog post data, validates the form data, saves the form if valid, and redirects to the blog post detail page. If the request method is not POST, it creates an empty form with the existing blog post data and renders the blog post form template with the form.

    :return: A Django response object. If the request method is POST and the form is valid, it redirects to the blog post detail page. Otherwise, it renders the blog post form template with the form.
    :rtype: django.http.HttpResponse
    """
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_post_detail', pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog_post_form.html', {'form': form})




# user login with remember me form function
def user_login(request):
    """
    Handles user login with optional "Remember Me" functionality and redirects to the previous page after login.
    """
    # Get the 'next' parameter to redirect back after login
    next_url = request.GET.get('next', 'home')  # Default to 'home' if no next parameter

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        remember_me = request.POST.get('remember_me', False)  # Get the 'Remember Me' checkbox value

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                
                # Set session expiry based on "Remember Me"
                if not remember_me:
                    request.session.set_expiry(0)  # Session expires when the browser is closed
                else:
                    request.session.set_expiry(1209600)  # 2 weeks

                messages.success(request, 'You have successfully logged in.')
                
                # Redirect to the next URL or home
                return HttpResponseRedirect(next_url)
            else:
                messages.error(request, 'Your account is inactive. Please contact support.')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html', {'next': next_url})



# user creation and registration forms
def user_register(request):

    """
    Handles user registration.
    """
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        # custom user form
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            username = form.cleaned_data.get('username')
            
            # Automatically log in the new user
            login(request, user)
            messages.success(request, f"Account created successfully for {username}!")
            
            # Redirect to a welcome or home page
            return redirect('home')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})
    