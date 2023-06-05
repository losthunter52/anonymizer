def psedoanonymize_data(
    data,
    method = 'full',
    standard_value = "Object",
    replacements = []
):
    match method:
        case "single":
            single(data, replacements)
        case "full":
            full(data, standard_value)
    return data

def single(data, replacements):
    database = data.get_database()
    fields = data.get_fields()
    key = []
    for i in range(len(database)):
        for field in fields:
            if database[i][field] in replacements:
                original_word = database[i][field]
                new_word = replacements[original_word]
                database[i][field] = new_word
                key.append((i, field, original_word, new_word))
    for k in key:
        data.log.add_key(k)
    return database
        
def full(data, standard_value):
    database = data.get_database()
    fields = data.get_fields()
    replacements = {}
    used_names = set()

    for i in range(len(database)):
        for field in fields:
            name = database[i][field]
            if name not in replacements:
                if name in used_names:
                    for key, value in replacements.items():
                        if value == name:
                            replacements[name] = key
                            break
                else:
                    replacement = f'{standard_value}{len(replacements) + 1}'
                    replacements[name] = replacement
                    used_names.add(name)

    key = []
    for i in range(len(database)):
        for field in fields:
            name = database[i][field]
            if name in replacements:
                original_word = name
                new_word = replacements[name]
                database[i][field] = new_word
                key.append((i, field, original_word, new_word))
                data.log.add_key((i, field, original_word, new_word))

    return database

