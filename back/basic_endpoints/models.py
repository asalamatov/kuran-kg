from django.db import models

# Create your models here.
class Surah(models.Model):
    id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    meaning = models.CharField(max_length=255)
    no = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name


class SurahText(models.Model):
    text_number = models.IntegerField()
    surah_name = models.CharField(max_length=100)
    ayah_number = models.IntegerField()
    ayah_text = models.TextField()
    controlled = models.BooleanField(default=False)

    def __str__(self):
        return "Text of ayah #" + str(self.ayah_number) + " from " + self.surah_name


class SurahExplanation(models.Model):
    expl_number = models.IntegerField()
    surah_name = models.CharField(max_length=100)
    explanation = models.TextField()
    controlled = models.BooleanField(default=False)

    def __str__(self):
        return "Expl #" + str(self.expl_number) + " from " + self.surah_name

