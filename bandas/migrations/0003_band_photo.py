# Generated by Django 4.0.6 on 2024-06-03 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0002_album_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
