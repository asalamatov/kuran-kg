from bs4 import BeautifulSoup
import requests, json

url = 'https://mursel-ahiskali.blogspot.com/2014/02/krgzca-kuran-kerim-meali.html?m=1'

soup = BeautifulSoup(requests.get(url).content, 'html.parser')

a_tags = soup.find_all('a', href=True)

dictionary = {
    'fatihah' : 'http://mursel-ahiskali.blogspot.com/2014/02/fatiha.html'
}

surahs = '''
baqarah
al_e_imran
nisa
maidah
anam
araf
anfal
tawbah
yunus
hud
yusuf
rad
ibrahim
hijr
nahl
isra
kahf
maryam
taha
anbiya
hajj
muminoon
nur
furqan
shuara
naml
qasas
ankabut
rum
luqman
sajdah
ahzab
saba
fatir
yasin
saffat
sad
zumar
ghafir
fussilat
shura
zukhruf
dukhan
jathiyah
ahqaf
muhammad
fath
hujurat
qaf
dhariyat
tur
najm
qamar
rahman
waqiah
hadid
mujadilah
hashr
mumtahanah
saff
jumuah
munafiqoon
taghabun
talaq
tahrim
mulk
qalam
haqqah
maarij
nuh
jinn
muzzammil
muddathir
qiyamah
insan
mursalat
naba
naziat
abasa
takwir
infitar
mutaffifin
inshiqaq
buruj
tariq
ala
ghashiyah
fajr
balad
shams
lail
duha
sharh
tin
alaq
qadr
bayyinah
zalzalah
adiyat
qariah
takathur
asr
humazah
fil
quraysh
maun
kawthar
kafirun
nasr
masad
ikhlas
falaq
nas'''

surahs_list = surahs.split('\n')[1:]

for i in range(len(surahs_list)):
    link = a_tags[i]['href']
    dictionary[surahs_list[i]] = a_tags[i+2]['href']

print(json.dumps(dictionary, indent=4))
# if data/links.json does not exist, it will be created
# if it exists, need to create links1.json, if links1.json exists, links2.json, etc
cnt = 0
import os

while True:
    if os.path.exists(f'data/links.json'):
        cnt += 1
    elif os.path.exists(f'data/links{cnt}.json'):
        cnt += 1
    else:
        with open(f'data/links{cnt}.json', 'w') as file:
            file.write(json.dumps(dictionary, indent=4))
        break


# while True:
#     try:
#         with open(f'data/links{cnt}.json', 'w') as file:
#             file.write(json.dumps(dictionary, indent=4))
#         break
#     except FileExistsError:
#         cnt += 1

# with open('data/links.json', 'w') as file:
#     file.write(json.dumps(dictionary, indent=4))