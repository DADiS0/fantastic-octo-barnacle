# Generated by Django 5.1 on 2024-09-05 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
