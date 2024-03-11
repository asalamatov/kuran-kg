import json

# I have a file in the same directory as this script called 'whole_quran.json'
with open('whole_quran111.json', 'r') as f:
    original_json = json.load(f)

# print(original_json)

texts_json = []
explanations_json = []

text_id = 0
expl_id = 0

for surah_name, surah_data in original_json.items():
    for ayah_number, text in surah_data['text'].items():
        if surah_name == 'tawbah':
            ayah_no_id = int(ayah_number) - 1
            if ayah_no_id < 0:
                ayah_no_id = 0
        else:
            ayah_no_id = int(ayah_number) - 2
            if ayah_no_id < 0:
                ayah_no_id = 0
        texts_json.append({
            'id': text_id,
            'text_number': int(ayah_number),
            'surah_name': surah_name,
            'ayah_number': ayah_no_id,
            'ayah_text': text
        })
        text_id += 1

    for expl_number, explanation in surah_data['explanation'].items():
        explanations_json.append({
            'id': expl_id,
            'expl_number': int(expl_number),
            'surah_name': surah_name,
            'explanation': explanation
        })
        expl_id += 1


texts_json_output = json.dumps(texts_json, indent=2)
explanations_json_output = json.dumps(explanations_json, indent=2)

print("Texts JSON:")
print(texts_json_output)
with open('texts.json', 'w') as f:
    f.write(texts_json_output)

print("\nExplanations JSON:")
print(explanations_json_output)
with open('explanations.json', 'w') as f:
    f.write(explanations_json_output)
