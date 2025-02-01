
# from django.shortcuts import render
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


# url patterns for app

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.service_list, name='service_list'),
    path('services/', views.custom_services, name='custom_services'),
    path('services/', views.cloud_services, name='cloud_services'),
    path('blog/', views.blog_list, name='blog_list'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('careers/', views.job_list, name='job_list'),
    path('apply/<int:id>/', views.apply_job, name='apply_job'),
    path('job/<int:id>/', views.job_details, name='job_details'),

    path('testimonials/', views.testimonial_list, name='testimonial_list'),
    path('contact/', views.contact_form, name='contact_form'),
    path('success/', views.contact_success, name='contact_success'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('submit-testimonial/', views.submit_testimonial, name='submit_testimonial'),
    path('testimonial-success/', views.testimonial_success, name='testimonial_success'),
    path('profile/', views.user_profile, name='user_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    

    #path('accounts/logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_register, name='user_register'),
    #path('accounts/profile/<int:pk>/', views.user_profile, name='user_profile'),
    #path('accounts/password_change/', views.password_change, name='password_change

    path('post/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
    path('post/<int:pk>/', views.blog_post_list, name='blog_post_list'),
    path('posts/', views.blog_post_list, name='blog_post_list'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),

    path('post/new/', views.blog_post_create, name='blog_post_create'),
    path('post/<int:pk>/edit/', views.blog_post_update, name='blog_post_update'),

    # password reset url
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # project in details
    path('project/<int:id>/', views.project_details, name='project_detail'),

    # blog in details
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]

