# Generated by Django 5.1.2 on 2024-10-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank='True', to='projects.tag'),
        ),
    ]
