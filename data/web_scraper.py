import requests, json
from bs4 import BeautifulSoup

url = 'http://mursel-ahiskali.blogspot.com/2014/02/81-tekvir-suresi.html'



whole_quran = {}

links = {}

with open('data/links.json', 'r') as file:
    links = json.load(file)

#! for surah_name, link in links.items():
#     whole_quran[surah_name] = {
#         'text': [],
#         'explanation': []
#     }




def find_indices(a, b):
    # Find the part of string a that is not in string b
    difference = a.replace(b, '').strip().split('[')[0].strip()
    # print(difference)
    dif_arr = difference.split(' ')
    # print(dif_arr)
    b_arr = b.split(' ')
    b_arr = [word.split('[')[0] for word in b_arr]
    # print(b_arr)

    indices = [b_arr.index(word) for word in dif_arr if word in b_arr]

    return indices

# print(json.dumps(links, indent=4))



# divs_with_class = soup.find_all('div', class_='post hentry')



# print(len(divs_with_class)) # 1

# with open('data/fatiha.html', 'w') as file:
#     file.write(divs_with_class[0].prettify())

# Path: data/fatiha.html

# get title h3

# title = divs_with_class[0].h3.text
# print(title.strip()) # Fatiha  - the file contains only one h3 tag




# print(len(div_mso_footnote_text))



def main_text(url):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    array_expl= []
    text = []
    div_mso_normal = soup.find_all('div', class_='MsoNormal')
    div_mso_footnote_text = soup.find_all('div', class_='MsoFootnoteText')

    for div in div_mso_footnote_text:
        span_elements = div.find_all('span', recursive=False)
        string = ''
        for span in span_elements:
            if span.text:
                # print(span.text.strip().replace('\n', ' ').strip(), end=' ')
                string += span.text.strip().replace('\n', ' ').strip()
        # if div.find('span'):
            # print()
        array_expl.append(string)

    # print()
    # for i in range(len(array_expl)):

    #     with open('data/qiyamah_expl.txt', 'a') as file:
    #         file.write(f'{array_expl[i]}')
    #         if i != len(array_expl) - 1:
    #             file.write('\n')


    for i in range(len(div_mso_normal)):
        string = ''
        span_elements = div_mso_normal[i].find_all('span', recursive=False)
        for span in span_elements:
            if span.text:
                string += span.text.strip().replace('\n', ' ').strip()
                # print(span.text.strip().replace('\n', ' ') if span.text else '', end=' ')
            string += ' '
        text.append(string)

                # with open('data/qiyamah.txt', 'a') as file:
                #     if span.text:
                #         file.write(span.text.strip().replace('\n', ' '))

        # if div_mso_normal[i].find('span'): #? comment
            # print() #? comment
        #     with open('data/qiyamah.txt', 'a') as file:
        #         file.write('\n')

    text = [i for i in text if i != '']
    begin, end = text[:2], text[2:]
    # remove 1. 2. 3. etc from the beginning of the text first split then join except for the first 2 elements
    end = [i for i in end if i[0].isnumeric()]
    for i in range(len(end)): # in ne v etom
         end[i] = '.'.join(end[i].split('.')[1:]).strip()
    text = begin + end
    array_expl = [i for i in array_expl if i != '']
    return text, array_expl

# a, b = main_text('http://mursel-ahiskali.blogspot.com/2014/02/bakara-suresi_2674.html')

print("-------------------------")
# for i in b:
#     print(i)

for surah_name, link in links.items():
    whole_quran[surah_name] = {
        'text': [],
        'explanation': []
    }
    a, b = main_text(link)
    whole_quran[surah_name]['text'] = {str(i-1): val for i, val in enumerate(a)}
    whole_quran[surah_name]['explanation'] = {str(i+1): val for i, val in enumerate(b)}

listic = []

for i in whole_quran:
    listic.append({
        'number': i,
        'name': whole_quran[i]['text'][0],
        'translationTitle': whole_quran[i]['text'][1]
    })

# with open('data/surahs.json', 'w', encoding='ascii') as file:
#     json.dump(listic, file, indent=4)

# with open('data/whole_quran.json', 'w', encoding='ascii') as file:
#     json.dump(whole_quran, file, indent=4)

# with open('data/whole_quran.json', 'r', encoding='ascii') as file:
#     whole_quran1 = json.load(file)


# get a list of dict with the number of surah, name, translationTitle,
# for i in whole_quran1:
#     listic.append({
#         'number': i,
#         'name': whole_quran1[i]['text'][0],
#         'translationTitle': whole_quran1[i]['text'][1]
#     })

# with open('data/surahs.json', 'w', encoding='ascii') as file:
#     json.dump(listic, file, indent=4)


# print(whole_quran1['fatihah']['text'])
# print(json.dumps(whole_quran1['fatihah']['explanation'], indent=4))


# starting from the begging of the string (a or temp) and ending at the end of a
#delete all the characters that are the same in both strings from temp





    # with open('data/maida.txt', 'a') as file:
    #     file.write(i)
    #     file.write('\n')
# print(len(a))
# for i in b:
#     with open('data/maida_expl.txt', 'a') as file:
#         file.write(i)
#         file.write('\n')
#     print(i)
# print(len(b))

