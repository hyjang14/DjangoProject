# Generated by Django 5.0.6 on 2024-05-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='blog_photo', verbose_name='이미지'),
        ),
    ]
