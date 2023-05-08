import hashlib

def hash_data(
    data,
    method = 'md5',
):
    database = data.get_database()
    fields = data.get_fields()

    match method:

        case 'md5':
            h = hashlib.md5()

        case 'sha1':
            h = hashlib.sha1()

        case 'sha256':
            h = hashlib.sha256()
    
    for i in range(len(database)):
        for field in fields:
            h.update(database[i][field].encode('utf-8'))
            database[i][field] = str(h.hexdigest())
    
    data.update_database(database)

    return data


