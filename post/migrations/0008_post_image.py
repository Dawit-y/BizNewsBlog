# Generated by Django 4.2.1 on 2023-05-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_comment_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='tree.jpg', upload_to='images'),
        ),
    ]
