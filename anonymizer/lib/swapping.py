
import random
import time

def swap_data(
    data,
    method = 'random_substitution'
):
    match method:

        case 'random_substitution':
            substitution(data)

    return data

def substitution(data):
    database = data.get_database()
    fields = data.get_fields()
    original_key = []
    cifred_key = []
    for i in range(len(database)):
        for field in fields:
            for character in database[i][field]:
                if not character in original_key:
                    original_key.append(character)
                    cifred_key.append(character)
    random.shuffle(cifred_key)
    for i in range(len(database)):
        for field in fields:
            char_list = list(database[i][field])
            for char in range(len(char_list)):
                char_list[char] = cifred_key[original_key.index(char_list[char])]
            database[i][field] = ''.join(char_list)
    data.log.add_key("Param [" + str(data.method_counter) + "]:")
    data.log.add_key("Swapping Substitution Original Key:")
    data.log.add_key(original_key)
    data.log.add_key("Swapping Substitution Cifred Key:")
    data.log.add_key(cifred_key)
    data.update_database(database)