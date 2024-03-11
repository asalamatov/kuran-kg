from django.contrib import admin
from .models import Surah, SurahText, SurahExplanation
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#Surah
class SurahResource(resources.ModelResource):
    class Meta:
        model = Surah

class SurahAdmin(ImportExportModelAdmin):
    resource_class = SurahResource

#SurahText
class SurahTextResource(resources.ModelResource):
    class Meta:
        model = SurahText

class SurahTextAdmin(ImportExportModelAdmin):
    resource_class = SurahTextResource

#SurahExplanation
class SurahExplanationResource(resources.ModelResource):
    class Meta:
        model = SurahExplanation

class SurahExplanationAdmin(ImportExportModelAdmin):
    resource_class = SurahExplanationResource


# Register your models here.
admin.site.register(Surah, SurahAdmin)
admin.site.register(SurahText, SurahTextAdmin)
admin.site.register(SurahExplanation, SurahExplanationAdmin)
