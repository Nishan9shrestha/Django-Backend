# Generated by Django 5.1.7 on 2025-03-26 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0002_article_image_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image_location',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='medias/Images'),
        ),
    ]
