# Generated by Django 5.0.2 on 2024-02-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
    ]
