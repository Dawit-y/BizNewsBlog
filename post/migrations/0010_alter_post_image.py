# Generated by Django 4.2.1 on 2023-05-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/tree.jpg', upload_to='images'),
        ),
    ]
