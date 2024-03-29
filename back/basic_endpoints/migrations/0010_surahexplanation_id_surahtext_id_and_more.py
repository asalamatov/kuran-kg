# Generated by Django 5.0.2 on 2024-03-10 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_endpoints', '0009_rename_id_surahexplanation_expl_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='surahexplanation',
            name='id',
            field=models.BigAutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surahtext',
            name='id',
            field=models.BigAutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='surahexplanation',
            name='expl_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='surahtext',
            name='text_number',
            field=models.IntegerField(),
        ),
    ]
