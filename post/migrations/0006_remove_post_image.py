# Generated by Django 4.0.6 on 2023-04-04 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
