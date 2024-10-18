
# from django.shortcuts import render
from django.urls import path
from . import views


# url patterns for app

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.service_list, name='service_list'),
    path('blog/', views.blog_list, name='blog_list'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('careers/', views.job_list, name='job_list'),
    path('testimonials/', views.testimonial_list, name='testimonial_list'),
    path('contact/', views.contact_form, name='contact_form'),
    path('success/', views.contact_success, name='contact_success'),

    path('post/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
    path('post/new/', views.blog_post_create, name='blog_post_create'),
    path('post/<int:pk>/edit/', views.blog_post_update, name='blog_post_update'),
]
