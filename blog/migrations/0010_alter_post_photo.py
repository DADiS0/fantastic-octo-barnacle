# Generated by Django 5.1 on 2024-09-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='django/mysite2/photo/%Y/%m/%d'),
        ),
    ]
