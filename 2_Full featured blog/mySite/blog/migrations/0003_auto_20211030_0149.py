# Generated by Django 3.2.6 on 2021-10-29 20:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
