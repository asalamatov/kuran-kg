# Generated by Django 5.0.2 on 2024-03-10 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_endpoints', '0011_surahexplanation_controlled_surahtext_controlled'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurahTextText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
