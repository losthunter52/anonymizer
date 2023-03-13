def mask_data(
    data,
    fields,
    method,
    length,
    masked,
    initial_rage,
    final_range,
    mask_result_lenght
):
    match method:

        case 'full':
            data = full(data, fields)

        case 'positional':
            data = positional(data, fields, initial_rage, final_range)

        case 'right_to_left':
            data = right_to_left(data, fields, length, mask_result_lenght)

        case 'left_to_right':
            data = lelf_to_right(data, fields, length, mask_result_lenght)

        case 'email':
            data = email(data, fields)

        case 'cpf':
            data = cpf(data, fields, masked)

    return data


def full(data, fields):
    for i in range(len(data)):
        for field in fields:
            data[i][field] = "*"
    return data


def positional(data, fields, initial_range, final_range):
    for i in range(len(data)):
        for field in fields:
            field_len = len(str(data[i][field]))
            if initial_range >= 1 and final_range < field_len:
                data[i][field] = "*" + \
                    str(data[i][field])[initial_range:final_range] + "*"
            elif initial_range > 1:
                data[i][field] = "*" + str(data[i][field])[initial_range:]
            elif final_range < field_len:
                data[i][field] = str(data[i][field])[:final_range] + "*"
    return data


def right_to_left(data, fields, length, mask_result_lenght):
    if mask_result_lenght:
        for i in range(len(data)):
            for field in fields:
                if len(str(data[i][field])) > length:
                    data[i][field] = str(data[i][field])[:length] + "*"
    else:
        for i in range(len(data)):
            for field in fields:
                field_len = len(str(data[i][field]))
                if field_len > length:
                    data[i][field] = str(data[i][field])[
                        :length] + str('*'*(field_len-length))
    return data


def lelf_to_right(data, fields, length, mask_result_lenght):
    if mask_result_lenght:
        for i in range(len(data)):
            for field in fields:
                field_len = len(str(data[i][field]))
                if field_len > length:
                    data[i][field] = "*" + \
                        str(data[i][field])[field_len-length:]
    else:
        for i in range(len(data)):
            for field in fields:
                field_len = len(str(data[i][field]))
                if field_len > length:
                    data[i][field] = str(
                        '*'*(field_len-length)) + str(data[i][field])[field_len-length:]
    return data


def email(data, fields):
    for i in range(len(data)):
        for field in fields:
            email = str(data[i][field])
            dominioEmail = email.split("@")
            data[i][field] = dominioEmail[1]
    return data


def cpf(data, fields, masked):
    if masked:
        for i in range(len(data)):
            for field in fields:
                cpf = str(data[i][field])
                new_cpf = cpf[0:2]+"*.***.*" + cpf[9:11] + "-**"
                data[i][field] = new_cpf
    else:
        for i in range(len(data)):
            for field in fields:
                cpf = str(data[i][field])
                new_cpf = cpf[0:2]+"*****" + cpf[7:9] + "**"
                data[i][field] = new_cpf
    return data

