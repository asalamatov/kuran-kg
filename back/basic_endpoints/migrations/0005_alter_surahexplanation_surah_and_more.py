# Generated by Django 5.0.2 on 2024-03-10 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_endpoints', '0004_rename_text_surahtext_ayah_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surahexplanation',
            name='surah',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='surahtext',
            name='surah_name',
            field=models.CharField(max_length=100),
        ),
    ]
