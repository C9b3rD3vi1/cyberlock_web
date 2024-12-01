
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User, Service, BlogPost, Testimonial, ContactMessage, Job, Project, Profile
from .forms import ContactMessageForm, BlogPostForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
import logging
from .utils import save_contact_message
from is_safe_url import is_safe_url
from .forms import CustomUserCreationForm, TestimonialForm, ProfileForm, JobApplicationForm
from colorama import Fore, Style
from django.views.decorators.http import require_POST





def is_staff_or_high_user(user):
    return user.is_staff or user.has_perm('coreapp.can_create_post')



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



# All services offered by our applicationdef service_list(request):
def service_list(request):
    # Get the 'type' query parameter, defaulting to 'all' if not provided
    service_type = request.GET.get('type', 'all')

    # Fetch services based on the type filter
    if service_type == 'custom':
        services = Service.objects.filter(service_type='custom')
    elif service_type == 'cloud':
        services = Service.objects.filter(service_type='cloud')
    elif service_type == 'standard':
        services = Service.objects.filter(service_type='standard')
    else:
        services = Service.objects.all()

    context = {
        'services': services,
        'service_type': service_type,
    }

    return render(request, 'service_list.html', context)


def custom_services(request):
    services = Service.objects.filter(service_type='custom')
    return render(request, 'services_list.html', {'services': services, 'category_name': 'Custom'})

def cloud_services(request):
    services = Service.objects.filter(service_type='cloud')
    return render(request, 'services_list.html', {'services': services, 'category_name': 'Cloud'})



# show service detaila
def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service_details.html', {'service': service})



# render portfolio details project details
def portfolio(request):

    projects = Project.objects.all()

    return render(request, 'portfolio.html', {'projects': projects})


# Retrieve Blog details
def blog_list(request):

    blog_post = BlogPost.objects.all().order_by('-published_date')[:3]  # Get the latest 3 blog posts
    return render(request, 'blog_post.html', {"blog_post":blog_post})


# blog post detail page
def blog_detail(request, slug):
    # Retrieve the blog post by ID
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_post_detail.html', {'post': post})



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



# functions to allow logged in users to apply for available jobs
@login_required
def apply_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('apply_job')
        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        form = JobApplicationForm()

    return render(request, 'apply_job.html', {'form': form})




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


def project_details(request, id):
    # Retrieve the project by ID
    project = get_object_or_404(Project, id=id)
    return render(request, 'project_details.html', {'project': project})



# contant form for contactinfo and sending information to my company
def contact_form(request):
    """
    This function handles the contact form submission and rendering.
    """
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            # Save the message and send an email
            save_contact_message(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            return redirect('contact_success')
    else:
        form = ContactMessageForm()  # No need to change this part

    return render(request, 'contact_form.html', {'form': form})




# Return rresponse after successful contact and information sharing
def contact_success(request):
    return render(request, 'contact_success.html')



# User should be logged in and have all permissions
@login_required
@user_passes_test(is_staff_or_high_user)
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




 # User should be logged in and have all permissions
@login_required
@user_passes_test(is_staff_or_high_user)
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

    Parameters:
    request (django.http.HttpRequest): The HTTP request object containing the necessary information for login.

    Returns:
    django.http.HttpResponse: A Django response object. If the request method is POST and the form is valid, it redirects to the specified next page. Otherwise, it renders the login template with the next page URL.
    """
    # Get the 'next' parameter to redirect back after login
    next_url = request.GET.get('next', 'home')  # Default to 'home' if no next parameter

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        remember_me = request.POST.get('remember_me') == 'on'  # Check if checkbox is checked

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                # Set session expiry based on "Remember Me"
                request.session.set_expiry(0 if not remember_me else 1209600)  # 0 for session-only, 2 weeks for "Remember Me"

                messages.success(request, 'You have successfully logged in.')

                # Validate next_url
                if is_safe_url(next_url, allowed_hosts={request.get_host()}):
                    return redirect(next_url)
                else:
                    return redirect('home')
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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            login(request, user)
            messages.success(request, f"Account created successfully for {username}!")
            return redirect('home')
        else:
            # Provide specific feedback for form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})



# user logout functionality
#@require_POST  # Require POST requests for logout
def user_logout(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Log the user out
        logout(request)

        # Set a success message for logout
        messages.success(request, "You have been logged out successfully.")
    else:
        # Set an info message if the user was not logged in
        messages.info(request, "You were not logged in.")

    # Redirect to the next URL or home
    next_url = request.GET.get('next', 'home')
    if is_safe_url(url=next_url, allowed_hosts={request.get_host()}):
        return redirect(next_url)

    return redirect('home')  # Default fallback



# Allow users to create and submit forms for testimonies only while logged in.
@login_required(login_url='/login/')
def submit_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.save()  # Save the testimonial to the database
            return redirect('testimonial_success')  # Redirect to a success page
    else:
        form = TestimonialForm()
    
    return render(request, 'submit_testimonial.html', {'form': form})




# success when user successfully submitted a testimonial
def testimonial_success(request):
    return render(request, 'success_testimonial.html')


# User profile creation and viewing
@login_required
def user_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'profile.html', {'profile': profile})



# Function to allow users to submit and edit profile only when they are authenticated
@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})



