import json

file_name = 'SurahTextExported1.json'

with open(file_name) as f:
    data = json.load(f)

# print(type(data))

new_data_list = []

for dic in data:
    new_dic = {}
    for k, v in dic.items():
        if k != 'id':
            new_dic[k] = v
    new_data_list.append(new_dic)

# print(new_data_list)


with open(f'{file_name}_without_ids.json', 'w') as f:
    json.dump(new_data_list, f, indent=2)

print('Done!')