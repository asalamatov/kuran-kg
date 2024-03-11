from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('surahs', views.get_surah_titles_meanings, name='get_surah_titles_meanings'),
    path('quran/<str:surah_name>', views.get_surah, name='get_surah'),
    path('quran/no/<int:surah_no>', views.get_surah_by_no, name='get_surah_by_no'),
]