# Generated by Django 4.0.6 on 2024-06-04 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0006_alter_disciplina_curso_alter_disciplina_projeto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curso', to='curso.curso'),
        ),
    ]
