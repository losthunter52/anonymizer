def mask_data(
    data,
    method = 'full',
    length = 0,
    masked = False,
    initial_range = 0,
    final_range = 0,
    mask_result_lenght = False
):
    database = data.get_database()
    fields = data.get_fields()

    match method:

        case 'full':
            data.update_database(full(database, fields))

        case 'positional':
            data.update_database(positional(
                database, fields, initial_range, final_range))

        case 'right_to_left':
            data.update_database(right_to_left(
                database, fields, length, mask_result_lenght))

        case 'left_to_right':
            data.update_database(lelf_to_right(
                database, fields, length, mask_result_lenght))

        case 'email':
            data.update_database(email(database, fields))

        case 'cpf':
            data.update_database(cpf(database, fields, masked))

    return data


def full(database, fields):
    for i in range(len(database)):
        for field in fields:
            database[i][field] = "*"
    return database


def positional(database, fields, initial_range, final_range):
    for i in range(len(database)):
        for field in fields:
            field_len = len(str(database[i][field]))
            if initial_range > 1 and final_range < field_len:
                database[i][field] = "*" + \
                    str(database[i][field])[initial_range-1:final_range] + "*"
            elif initial_range > 1:
                database[i][field] = "*" + \
                    str(database[i][field])[initial_range-1:]
            elif final_range < field_len:
                database[i][field] = str(database[i][field])[
                    :final_range] + "*"
    return database


def right_to_left(database, fields, length, mask_result_lenght):
    if mask_result_lenght:
        for i in range(len(database)):
            for field in fields:
                if len(str(database[i][field])) > length:
                    database[i][field] = str(database[i][field])[:length] + "*"
    else:
        for i in range(len(database)):
            for field in fields:
                field_len = len(str(database[i][field]))
                if field_len > length:
                    database[i][field] = str(database[i][field])[
                        :length] + str('*'*(field_len-length))
    return database


def lelf_to_right(database, fields, length, mask_result_lenght):
    if mask_result_lenght:
        for i in range(len(database)):
            for field in fields:
                field_len = len(str(database[i][field]))
                if field_len > length:
                    database[i][field] = "*" + \
                        str(database[i][field])[field_len-length:]
    else:
        for i in range(len(database)):
            for field in fields:
                field_len = len(str(database[i][field]))
                if field_len > length:
                    database[i][field] = str(
                        '*'*(field_len-length)) + str(database[i][field])[field_len-length:]
    return database


def email(database, fields):
    for i in range(len(database)):
        for field in fields:
            email = str(database[i][field])
            dominioEmail = email.split("@")
            if len(dominioEmail) > 0:
                database[i][field] = dominioEmail[-1]
            else:
                database[i][field] = "email.com"
    return database


def cpf(database, fields, masked):
    if masked:
        for i in range(len(database)):
            for field in fields:
                cpf = str(database[i][field])
                new_cpf = cpf[0:2]+"*.***.*" + cpf[9:11] + "-**"
                database[i][field] = new_cpf
    else:
        for i in range(len(database)):
            for field in fields:
                cpf = str(database[i][field])
                new_cpf = cpf[0:2]+"*****" + cpf[7:9] + "**"
                database[i][field] = new_cpf
    return database
