# Generated by Django 4.0.6 on 2024-06-07 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0011_remove_disciplina_projeto_projeto_disciplina'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='nome',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
