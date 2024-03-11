# import re

# a = 'Биз Сага гана сыйынып, Сенден гана жардам сурайбыз.[6] Сага Сенден [6] [6] [6]'
# b = 'Биз Сага гана сыйынып, Сенден гана жардам сурайбыз.[6]'

# # Extract the part of string a that is not in string b
# result = re.findall(r'(?<=\s)([^[\s]+)(?=\s|$)', a)
# # Convert result to a string separated by space
# result_string = ' '.join(result)

# # Find indexes of result as an array from b
# indexes = [m.start() for m in re.finditer(result_string, b)]

# print(result)
# print(indexes)

# import re

# # Define the strings
# a = 'Биз Сага гана сыйынып, Сенден гана жардам сурайбыз.[6] Сага Сенден [6] [6] [6]'
# b = 'Биз Сага гана сыйынып, Сенден гана жардам сурайбыз.[6]'

# # Find the part of string a that is not in string b
# difference = a.replace(b, '').strip().split('[')[0]
# difference = difference.strip()
# dif_arr = difference.split(' ')
# b_arr = b.split(' ')

# indices = []
# for i in range(len(dif_arr)):
#     indices.append(b_arr.index(dif_arr[i]))

# print("Part of string a not in string b:", difference)
# print(f"Indexes of '{difference}' in string b:", indices)

import re

def find_indices(a, b):
    # Find the part of string a that is not in string b
    difference = a.replace(b, '').strip().split('[')[0].strip()
    print(difference)
    dif_arr = difference.split(' ')
    # print(dif_arr)
    b_arr = b.split(' ')
    b_arr = [word.split('[')[0] for word in b_arr]
    # print(b_arr)

    indices = [b_arr.index(word) for word in dif_arr if word in b_arr]

    return indices

# Define the strings
a = 'Ааламдардын эгеси болгон Аллага[3] мактоо! Аллага [3] [3] [3]'
b = 'Ааламдардын эгеси болгон Аллага[3] мактоо!'

# Call the function and print the results
indices = find_indices(a, b)
print(indices)
