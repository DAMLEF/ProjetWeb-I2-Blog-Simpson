# Generated by Django 5.1.3 on 2024-11-16 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_equipement_character_delete_billet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Equipement',
            new_name='Place',
        ),
        migrations.RenameModel(
            old_name='Character',
            new_name='Simpson',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='id_equip',
            new_name='id_place',
        ),
    ]
