import random
from .log import Log


class Data:
    def __init__(self, database):
        self.database = database
        self.fields = []
        self.log = Log()
        self.method_counter = 0

    def prepare_fields(self, fields):
        self.method_counter += 1
        self.fields = fields
        for i in range(len(self.fields)):
            self.fields[i] = str(self.fields[i])
        fields_with_warning = []
        for field in self.fields:
            error = False
            for i in range(len(self.database)):
                if not field in self.database[i]:
                    if error == False:
                        fields_with_warning.append(field)
                        error = True
                    self.database[i][field] = ("*" * random.randint(1, 30))
                    self.database = self.database
        if len(fields_with_warning) > 0:
            self.log.add_warning("Param [" + str(self.method_counter) + "]:")
            self.log.add_warning("  -  One or more random values ​​were generated in the fields:")
            self.log.add_warning("         *" + str(fields_with_warning))

    def set_int_fields(self, fields):
        self.prepare_fields(fields)
        fields_with_warning = []
        for field in self.fields:
            error = False
            buffer = 0
            for i in range(len(self.database)):
                try:
                    self.database[i][field] = int(self.database[i][field])
                    buffer = self.database[i][field]
                except:
                    if error == False:
                        fields_with_warning.append(field)
                        error = True
                        self.database[i][field] = buffer
        if len(fields_with_warning) > 0:
            self.log.add_warning("Param [" + str(self.method_counter) + "]:")
            self.log.add_warning("  -  One or more integer values ​​were generated in the fields:")
            self.log.add_warning("         *" + str(fields_with_warning))

    def set_float_fields(self, fields):
        self.prepare_fields(fields)
        fields_with_warning = []
        for field in self.fields:
            error = False
            buffer = 0
            for i in range(len(self.database)):
                try:
                    self.database[i][field] = float(self.database[i][field])
                    buffer = self.database[i][field]
                except:
                    if error == False:
                        fields_with_warning.append(field)
                        error = True
                        self.database[i][field] = buffer
        if len(fields_with_warning) > 0:
            self.log.add_warning("Param [" + str(self.method_counter) + "]:")
            self.log.add_warning("  -  One or more real values ​​were generated in the fields:")
            self.log.add_warning("         *" + str(fields_with_warning))

    def set_boolean_fields(self, fields):
        self.prepare_fields(fields)
        fields_with_warning = []
        true_fields = ['true', 't', 'yes', 'y', 'v', 's', '1', 1, True]
        false_fields = ['false', 'f', 'no', 'n', 'f', '0', 0, False]
        for field in self.fields:
            error = False
            for i in range(len(self.database)):
                if self.database[i][field].lower() in true_fields:
                    self.database[i][field] = True
                elif self.database[i][field].lower() in false_fields:
                    self.database[i][field] = False
                else:
                    self.database[i][field] = bool(random.getrandbits(1))
                    if error == False:
                        fields_with_warning.append(field)
                        error = True
        if len(fields_with_warning) > 0:
            self.log.add_warning("Param [" + str(self.method_counter) + "]:")
            self.log.add_warning("  -  One or more boolean values ​​were generated in the fields:")
            self.log.add_warning("         *" + str(fields_with_warning))

    def set_numeric_fields(self, fields):
        self.prepare_fields(fields)
        fields_with_warning = []
        for field in self.fields:
            error = False
            buffer = 0
            for i in range(len(self.database)):
                try:
                    self.database[i][field] = float(self.database[i][field])
                    if self.database[i][field] % 1 == 0:
                        self.database[i][field] = int(self.database[i][field])
                    buffer = self.database[i][field]
                except:
                    if error == False:
                        fields_with_warning.append(field)
                        error = True
                    self.database[i][field] = buffer
        if len(fields_with_warning) > 0:
            self.log.add_warning("Param [" + str(self.method_counter) + "]:")
            self.log.add_warning("  -  One or more numeric values ​​were generated in the fields:")
            self.log.add_warning("         *" + str(fields_with_warning))

    def set_string_fields(self, fields):
        self.prepare_fields(fields)
        for i in range(len(self.database)):
            for field in self.fields:
                self.database[i][field] = str(self.database[i][field])

    def update_database(self, database):
        self.database = database

    def get_log(self):
        return self.log.get_log()

    def get_database(self):
        return self.database

    def get_fields(self):
        return self.fields
