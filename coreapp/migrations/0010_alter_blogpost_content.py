# Generated by Django 4.2.16 on 2024-12-04 08:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
