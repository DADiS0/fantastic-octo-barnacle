# Generated by Django 5.1 on 2024-09-05 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='django/mysite2/photo/%Y/%m/%d'),
        ),
    ]
