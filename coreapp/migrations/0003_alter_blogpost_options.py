# Generated by Django 4.2.14 on 2024-10-19 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0002_alter_blogpost_options_alter_testimonial_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-published_date'], 'permissions': [('can_create_post', 'Can create blog post'), ('can_update_post', 'Can update blog post'), ('can_delete_post', 'Can delete blog post')]},
        ),
    ]
