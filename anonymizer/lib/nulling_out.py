def null_out(data):
    database = data.get_database()
    fields = data.get_fields()

    for i in range(len(database)):
        for field in fields:
            database[i].pop(field, None)

    data.update_database(database)

    return data
