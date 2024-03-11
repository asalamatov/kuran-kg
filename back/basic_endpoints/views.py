from django.shortcuts import render
from .models import Surah, SurahText, SurahExplanation

# Create your views here.
from django.http import HttpResponse, JsonResponse
import os, json, requests

id_to_name = {'fatihah': 'аль-Фатиха', 'baqarah': 'аль-Бакара', 'al_e_imran': 'Аали ‘Имран', 'nisa': 'ан-Ниса’', 'maidah': 'аль-Маа’ида', 'anam': 'аль-Ан‘ам', 'araf': 'аль-А‘раф', 'anfal': 'аль-Анфал', 'tawbah': 'ат-Тауба', 'yunus': 'Йунус', 'hud': 'Хууд', 'yusuf': 'Йусуф', 'rad': 'Ар-Ра‘д', 'ibrahim': 'Ибрахим', 'hijr': 'Ал-Хижр', 'nahl': 'Ан-Нахль', 'isra': 'аль-Исра’', 'kahf': 'аль-Кахф', 'maryam': 'Марьям', 'taha': 'То Ха', 'anbiya': 'аль-Анбия’', 'hajj': 'аль-Хажж', 'muminoon': 'аль-Му’минун', 'nur': 'ан-Нур', 'furqan': 'аль-Фуркан', 'shuara': 'аш-Шу‘ара’', 'naml': 'ан-Намль', 'qasas': 'аль-Касас', 'ankabut': 'аль-‘Анкабут', 'rum': 'ар-Рум', 'luqman': 'Лукман', 'sajdah': 'ас-Сажда', 'ahzab': 'аль-Ахзаб', 'saba': 'Саба', 'fatir': 'Фаатыр', 'yasin': 'Йа Син', 'saffat': 'ас-Сааффат', 'sad': 'Сод', 'zumar': 'аз-Зумар', 'ghafir': 'Гаафир', 'fussilat': 'Фуссылят', 'shura': 'аш-Шура', 'zukhruf': 'аз-Зухруф', 'dukhan': 'ад-Духан', 'jathiyah': 'аль-Жаасия', 'ahqaf': 'аль-Ахкаф', 'muhammad': 'Мухаммед', 'fath': 'аль-Фатх', 'hujurat': 'аль-Хужураат', 'qaf': 'Каф', 'dhariyat': 'аз-Заарият', 'tur': 'ат-Тур', 'najm': 'ан-Нажм', 'qamar': 'аль-Камар', 'rahman': 'Ар-Рахман', 'waqiah': 'аль-Вакы‘а', 'hadid': 'аль-Хадид', 'mujadilah': 'аль-Мужадила', 'hashr': 'аль-Хашр', 'mumtahanah': 'аль-Мумтахана', 'saff': 'ас-Софф', 'jumuah': 'аль-Жуму‘а', 'munafiqoon': 'аль-Мунафикун', 'taghabun': 'ат-Тагаабун', 'talaq': 'ат-Талак', 'tahrim': 'ат-Тахрим', 'mulk': 'аль-Мульк', 'qalam': 'аль-Калам', 'haqqah': 'аль-Хаакка', 'maarij': 'аль-Ма‘ариж', 'nuh': 'Нух', 'jinn': 'аль-Жинн', 'muzzammil': 'аль-Муззаммил', 'muddathir': 'аль-Муддассир', 'qiyamah': 'аль-Кыяма', 'insan': 'аль-Инсан', 'mursalat': 'аль-Мурсалят', 'naba': 'ан-Наба’', 'naziat': 'ан-Нази‘ат', 'abasa': '‘Абаса', 'takwir': 'ат-Таквир', 'infitar': 'аль-Инфитар', 'mutaffifin': 'аль-Мутоффифин', 'inshiqaq': 'аль-Иншикак', 'buruj': 'аль-Буруж', 'tariq': 'ат-Торик', 'ala': 'аль-А‘ля', 'ghashiyah': 'аль-Гаашия', 'fajr': 'аль-Фажр', 'balad': 'аль-Балад', 'shams': 'аш-Шамс', 'lail': 'аль-Ляйл', 'duha': 'ад-Духа', 'sharh': 'аль-Инширах', 'tin': 'ат-Тин', 'alaq': 'аль-‘Алак', 'qadr': 'аль-Кадр', 'bayyinah': 'аль-Баййина', 'zalzalah': 'аз-Залзала', 'adiyat': 'аль-‘Адият', 'qariah': 'аль-Коори‘а', 'takathur': 'ат-Такаасур', 'asr': 'аль-‘Аср', 'humazah': 'аль-Хумаза', 'fil': 'аль-Фил', 'quraysh': 'Курайш', 'maun': 'аль-Маа‘уун', 'kawthar': 'аль-Каусар', 'kafirun': 'аль-Каафирун', 'nasr': 'ан-Наср', 'masad': 'аль-Масад', 'ikhlas': 'аль-Ихлас', 'falaq': 'аль-Фалак', 'nas': 'ан-Наас'}

no_to_id = { 1 : 'fatihah', 2 : 'baqarah', 3 : 'al_e_imran', 4 : 'nisa', 5 : 'maidah', 6 : 'anam', 7 : 'araf', 8 : 'anfal', 9 : 'tawbah', 10 : 'yunus', 11 : 'hud', 12 : 'yusuf', 13 : 'rad', 14 : 'ibrahim', 15 : 'hijr', 16 : 'nahl', 17 : 'isra', 18 : 'kahf', 19 : 'maryam', 20 : 'taha', 21 : 'anbiya', 22 : 'hajj', 23 : 'muminoon', 24 : 'nur', 25 : 'furqan', 26 : 'shuara', 27 : 'naml', 28 : 'qasas', 29 : 'ankabut', 30 : 'rum', 31 : 'luqman', 32 : 'sajdah', 33 : 'ahzab', 34 : 'saba', 35 : 'fatir', 36 : 'yasin', 37 : 'saffat', 38 : 'sad', 39 : 'zumar', 40 : 'ghafir', 41 : 'fussilat', 42 : 'shura', 43 : 'zukhruf', 44 : 'dukhan', 45 : 'jathiyah', 46 : 'ahqaf', 47 : 'muhammad', 48 : 'fath', 49 : 'hujurat', 50 : 'qaf', 51 : 'dhariyat', 52 : 'tur', 53 : 'najm', 54 : 'qamar', 55 : 'rahman', 56 : 'waqiah', 57 : 'hadid', 58 : 'mujadilah', 59 : 'hashr', 60 : 'mumtahanah', 61 : 'saff', 62 : 'jumuah', 63 : 'munafiqoon', 64 : 'taghabun', 65 : 'talaq', 66 : 'tahrim', 67 : 'mulk', 68 : 'qalam', 69 : 'haqqah', 70 : 'maarij', 71 : 'nuh', 72 : 'jinn', 73 : 'muzzammil', 74 : 'muddathir', 75 : 'qiyamah', 76 : 'insan', 77 : 'mursalat', 78 : 'naba', 79 : 'naziat', 80 : 'abasa', 81 : 'takwir', 82 : 'infitar', 83 : 'mutaffifin', 84 : 'inshiqaq', 85 : 'buruj', 86 : 'tariq', 87 : 'ala', 88 : 'ghashiyah', 89 : 'fajr', 90 : 'balad', 91 : 'shams', 92 : 'lail', 93 : 'duha', 94 : 'sharh', 95 : 'tin', 96 : 'alaq', 97 : 'qadr', 98 : 'bayyinah', 99 : 'zalzalah', 100 : 'adiyat', 101 : 'qariah', 102 : 'takathur', 103 : 'asr', 104 : 'humazah', 105 : 'fil', 106 : 'quraysh', 107 : 'maun', 108 : 'kawthar', 109 : 'kafirun', 110 : 'nasr', 111 : 'masad', 112 : 'ikhlas', 113 : 'falaq', 114 : 'nas' }
id_to_no = { 'fatihah' : 1, 'baqarah' : 2, 'al_e_imran' : 3, 'nisa' : 4, 'maidah' : 5, 'anam' : 6, 'araf' : 7, 'anfal' : 8, 'tawbah' : 9, 'yunus' : 10, 'hud' : 11, 'yusuf' : 12, 'rad' : 13, 'ibrahim' : 14, 'hijr' : 15, 'nahl' : 16, 'isra' : 17, 'kahf' : 18, 'maryam' : 19, 'taha' : 20, 'anbiya' : 21, 'hajj' : 22, 'muminoon' : 23, 'nur' : 24, 'furqan' : 25, 'shuara' : 26, 'naml' : 27, 'qasas' : 28, 'ankabut' : 29, 'rum' : 30, 'luqman' : 31, 'sajdah' : 32, 'ahzab' : 33, 'saba' : 34, 'fatir' : 35, 'yasin' : 36, 'saffat' : 37, 'sad' : 38, 'zumar' : 39, 'ghafir' : 40, 'fussilat' : 41, 'shura' : 42, 'zukhruf' : 43, 'dukhan' : 44, 'jathiyah' : 45, 'ahqaf' : 46, 'muhammad' : 47, 'fath' : 48, 'hujurat' : 49, 'qaf' : 50, 'dhariyat' : 51, 'tur' : 52, 'najm' : 53, 'qamar' : 54, 'rahman' : 55, 'waqiah' : 56, 'hadid' : 57, 'mujadilah' : 58, 'hashr' : 59, 'mumtahanah' : 60, 'saff' : 61, 'jumuah' : 62, 'munafiqoon' : 63, 'taghabun' : 64, 'talaq' : 65, 'tahrim' : 66, 'mulk' : 67, 'qalam' : 68, 'haqqah' : 69, 'maarij' : 70, 'nuh' : 71, 'jinn' : 72, 'muzzammil' : 73, 'muddathir' : 74, 'qiyamah' : 75, 'insan' : 76, 'mursalat' : 77, 'naba' : 78, 'naziat' : 79, 'abasa' : 80, 'takwir' : 81, 'infitar' : 82, 'mutaffifin' : 83, 'inshiqaq' : 84, 'buruj' : 85, 'tariq' : 86, 'ala' : 87, 'ghashiyah' : 88, 'fajr' : 89, 'balad' : 90, 'shams' : 91, 'lail' : 92, 'duha' : 93, 'sharh' : 94, 'tin' : 95, 'alaq' : 96, 'qadr' : 97, 'bayyinah' : 98, 'zalzalah' : 99, 'adiyat' : 100, 'qariah' : 101, 'takathur' : 102, 'asr' : 103, 'humazah' : 104, 'fil' : 105, 'quraysh' : 106, 'maun' : 107, 'kawthar' : 108, 'kafirun' : 109, 'nasr' : 110, 'masad' : 111, 'ikhlas' : 112, 'falaq' : 113, 'nas' : 114 }

def index(request):
    return HttpResponse("Server is Running!")

# def get_surah_titles_meanings(request):
#     json_file_path = '../data/surah_names_meanings3.json'

#     if not os.path.exists(json_file_path):
#         return JsonResponse({'error': 'File does not exist'}, status=404)

#     with open(json_file_path, 'r') as file:
#         json_data = json.load(file)

#     # not convert to json
#     json_data = json.dumps(json_data, indent=4)

#     return JsonResponse(json_data, status=200, safe=False)

def get_surah_titles_meanings(request):
    surahs = Surah.objects.all()

    surahs_list = []
    for surah in surahs:
        surahs_list.append({
            'id': surah.id,
            'name': surah.name,
            'meaning': surah.meaning,
            'no': surah.no,
        })

    return JsonResponse(surahs_list, status=200, safe=False)


# endpoint: /api/kg/quran/fatihah return 'Fatihah'
# def get_surah(request, surah_name):
#     json_file_path = f'../data/whole_quran111.json'

#     if not os.path.exists(json_file_path):
#         return JsonResponse({'error': 'File does not exist'}, status=404)

#     with open(json_file_path, 'r') as file:
#         json_data = json.load(file)

#     # add cyrillic name to json_data: fatihah -> Фатиха
#     for i in json_data.keys():
#         json_data[i]['name'] = id_to_name[i]

#     # not convert to json
#     json_data = json.dumps(json_data[surah_name], indent=4)

#     return JsonResponse(json_data, status=200, safe=False)

# https://api.quran.com/api/v4/quran/verses/uthmani?chapter_number=66
# Here I can get the arabic text of the surah, it starts with the first ayah, not bismillah for all surahs except for surah fatihah

def get_arabic_text(surah_no: int) -> dict:
    url = f"https://api.quran.com/api/v4/quran/verses/uthmani?chapter_number={surah_no}"
    # url = f'https://api.alquran.cloud/v1/surah/{surah_no}/editions/quran-uthmani'

    payload={}
    headers = {
      'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload).text
    # parse to dict
    response = json.loads(response)

    return response

# endpoint: /api/kg/quran/fatihah return all texts of surah 'Fatihah'
def get_surah(request, surah_name: str) -> JsonResponse:
    surah_texts = SurahText.objects.filter(surah_name=surah_name)

    texts = []
    for surah_text in surah_texts:
        texts.append({
            'text_number': surah_text.text_number,
            'ayah_number': surah_text.ayah_number,
            'ayah_text': surah_text.ayah_text,
            'surah_name': id_to_name[surah_text.surah_name],
            'arabic_text': get_arabic_text(id_to_no[surah_text.surah_name])['verses'][surah_text.ayah_number - 1]['text_uthmani'] if surah_text.ayah_number != 0 else '',
            # 'arabic_text' : get_arabic_text(id_to_no[surah_text.surah_name])['data'][0]['ayahs'][surah_text.ayah_number - 1]['text'] if surah_text.ayah_number != 0 else '',
            # 'surah_title': id_to_name[surah_text.surah_name],
        })

    return JsonResponse(texts, status=200, safe=False)

# endpoint: /api/kg/quran/no/1 return all texts of surah 'Fatihah'
def get_surah_by_no(request, surah_no):
    surah_id = no_to_id[surah_no]
    surah_texts = SurahText.objects.filter(surah_name=surah_id)

    # I need to get surah and ayah number to get sound in format of 001002
    def format_surah_ayah_number(surah_no: int, ayah_no: int) -> str:
        surah_no = str(surah_no).zfill(3)
        ayah_no = str(ayah_no).zfill(3)

        return surah_no + ayah_no


    texts = []
    for surah_text in surah_texts:
        texts.append({
            'text_number': surah_text.text_number,
            'ayah_number': surah_text.ayah_number,
            'ayah_text': surah_text.ayah_text,
            'surah_name': id_to_name[surah_text.surah_name],
            'arabic_text': get_arabic_text(surah_no)['verses'][surah_text.ayah_number - 1]['text_uthmani'] if surah_text.ayah_number != 0 else '',
            # 'arabic_text' : get_arabic_text(surah_no)['data'][0]['ayahs'][surah_text.ayah_number - 1]['text'] if surah_text.ayah_number != 0 else '',
            'audio_link': f'https://mirrors.quranicaudio.com/everyayah/Husary_64kbps/{format_surah_ayah_number(surah_no, surah_text.ayah_number)}.mp3' if surah_text.ayah_number != 0 else '',
            # 'surah_title': id_to_name[surah_text.surah_name],
        })

    # https://api.quran.com/api/v4/chapter_recitations/6/1 is the link to the audio of the whole first surah
    # texts.append({
    #     'audio_link': f'https://api.quran.com/api/v4/chapter_recitations/6/{surah_no}'
    # })

    return JsonResponse(texts, status=200, safe=False)