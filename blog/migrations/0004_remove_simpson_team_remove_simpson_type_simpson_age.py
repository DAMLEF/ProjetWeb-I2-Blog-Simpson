# Generated by Django 5.1.3 on 2024-11-16 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_equipement_place_rename_character_simpson_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simpson',
            name='team',
        ),
        migrations.RemoveField(
            model_name='simpson',
            name='type',
        ),
        migrations.AddField(
            model_name='simpson',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
