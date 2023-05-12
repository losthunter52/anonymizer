import random

class Pseudoanonymizer:
    def __init__(self, replacements, standard_value, method):
        self.replacements = replacements
        self.standard_value = standard_value
        self.method= method
        self.data_log = {}
    
    def pseudoanonymize(self, data):
        database = data.get_database()
        fields = data.get_fields()
        key = []
        if self.method == 'single':
            for i in range(len(database)):
                for field in fields:
                    if database[i][field] in self.replacements:
                        original_word = database[i][field]
                        new_word = self.replacements[original_word]
                        database[i][field] = new_word
                        key.append((i, field, original_word, new_word))
                        self.data_log[original_word] = new_word
            for k in key:
                data.log.add_key(k)

            return database
        else:
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

                            replacement = f'{self.standard_value}{len(replacements) + 1}'
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

           
           
    def get_data_log(self):
        return self.data_log
