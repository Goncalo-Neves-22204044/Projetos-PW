# Generated by Django 4.0.6 on 2024-06-06 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0010_alter_disciplina_linguagensprogramacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='projeto',
        ),
        migrations.AddField(
            model_name='projeto',
            name='disciplina',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projeto', to='curso.disciplina'),
        ),
    ]
