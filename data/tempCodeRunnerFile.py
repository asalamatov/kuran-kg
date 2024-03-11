
explanations_json = []

for surah_id, surah_data in original_json.items():
    for ayah_number, text in surah_data['text'].items():
        texts_json.append({
            'surah_id': surah_id,
            'ayah_number': int(ayah_number),
            'text': text
        })

    for expl_number, explanation in surah_data['explanation'].items():
        explanations_json.append({
            'surah_id': surah_id,
            'expl_number': int(expl_number),
            'explanation': explanation
        })

texts_json_output = json.dumps(texts_json, indent=2)
explanations_json_output = json.dumps(explanations_json, indent=2)

print("Texts JSON:")
print(texts_json_output)

print("\nExplanations JSON:")
print(explanations_json_output)