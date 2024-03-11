import json

file_name = 'SurahTextExported1.json_without_ids.json'

with open(file_name) as f:
    data = json.load(f)

data = data[::-1]
print(data)

new_data_list = []

# i need the same data but with ids
index = 0

for dic in data:
    new_data_list.append({
        'id': index,
        'text_number': dic['text_number'],
        'surah_name': dic['surah_name'],
        'ayah_number': dic['ayah_number'],
        'ayah_text': dic['ayah_text'],
        'controlled': dic['controlled'],
    })
    index += 1


print(new_data_list)
with open(f'{file_name}_with_ids1.json', 'w') as f:
    json.dump(new_data_list, f, indent=2)

