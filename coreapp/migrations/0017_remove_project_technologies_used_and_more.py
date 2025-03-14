# Generated by Django 4.2.19 on 2025-03-01 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0016_service_tech_stacks_remove_project_technologies_used_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='technologies_used',
        ),
        migrations.RemoveField(
            model_name='service',
            name='tech_stacks',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tech_stack',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='coreapp.techstack'),
        ),
        migrations.AddField(
            model_name='project',
            name='tech_stack',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='coreapp.techstack'),
        ),
        migrations.AddField(
            model_name='service',
            name='tech_stack',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='coreapp.techstack'),
        ),
    ]
