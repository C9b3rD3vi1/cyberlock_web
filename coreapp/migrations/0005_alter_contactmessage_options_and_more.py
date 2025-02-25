# Generated by Django 4.2.14 on 2024-10-20 14:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0004_alter_service_options_service_service_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactmessage',
            options={'ordering': ['-sent_at'], 'verbose_name': 'Contact Message', 'verbose_name_plural': 'Contact Messages'},
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='message',
            field=models.TextField(verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='subject',
            field=models.CharField(max_length=200, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github',
            field=models.URLField(blank=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(blank=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]
