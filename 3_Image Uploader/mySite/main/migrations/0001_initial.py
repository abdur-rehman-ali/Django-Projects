# Generated by Django 3.2.6 on 2021-09-05 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='siteImages')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]