# Generated by Django 3.0.1 on 2020-01-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='images/bg01.jpg', upload_to=''),
        ),
    ]