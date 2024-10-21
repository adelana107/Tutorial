# Generated by Django 5.1.2 on 2024-10-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tags',
            new_name='tag',
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
