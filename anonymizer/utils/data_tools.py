import random


def prepare_fields(fields):
    for i in range(len(fields)):
        fields[i] = str(fields[i])
    return fields

def prepare_database_fields(database, fields):
    fields = prepare_fields(fields)
    fields_with_error = []
    for field in fields:
        error = False
        for data in database:
            if not field in data:
                if error == False:
                    fields_with_error.append(field)
                    error = True
                data[field] = ("*" * random.randint(1, 30))
    if len(fields_with_error) > 0:
        log = "Warning! The Field(s) "
        log = log + str(fields_with_error)
        log = log + " are missing in one or more database records."
        return { "database": database, "fields": fields, "log": log }
    else:
        return { "database": database, "fields": fields, "log": "" }
