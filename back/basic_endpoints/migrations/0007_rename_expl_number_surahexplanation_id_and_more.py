# Generated by Django 5.0.2 on 2024-03-10 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_endpoints', '0006_rename_surah_surahexplanation_surah_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surahexplanation',
            old_name='expl_number',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='surahtext',
            old_name='text_number',
            new_name='id',
        ),
    ]
