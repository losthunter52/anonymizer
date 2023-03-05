def mask_data(data, fields, method = "full", length = 0, masked = False, initial_rage = 0, final_range = 0, mask_result_lenght = False):
    match method:
         
        case 'full':
            data = full_method(data, fields)

        case 'positional':
            data = positional_method(data, fields, initial_rage, final_range)

        case 'right_to_left':
            data = right_to_left_method(data, fields, length, mask_result_lenght)

        case 'left_to_right':
            data = lelf_to_right_method(data, fields, length, mask_result_lenght)

        case 'email':
            data = email_method(data, fields)

        case 'cpf':
            data = cpf_method(data, fields, masked)

        case 'credit_card':
            data = credit_card_method(data, fields)

    return data

def full_method(data, fields):
    for i in range(len(data)):
                for field in fields:
                    data[i][field] = "*"
    return data

def positional_method(data, fields, initial_range, final_range):
    for i in range(len(data)):
        for field in fields:
            field_len = len(str(data[i][field]))
            if initial_range > 1 and final_range < field_len:
                data[i][field] = "*" + str(data[i][field])[initial_range:final_range] + "*"
            elif initial_range > 1:
                data[i][field] = "*" + str(data[i][field])[initial_range:]
            elif final_range < field_len:
                data[i][field] = str(data[i][field])[:final_range] + "*"
    return data


def right_to_left_method(data, fields, length, mask_result_lenght):
    if mask_result_lenght:
        for i in range(len(data)):
            for field in fields:
                if len(str(data[i][field]))>length:
                    data[i][field] = str(data[i][field])[:length] + "*"
    else:
        for i in range(len(data)):
            for field in fields:
                field_len = len(str(data[i][field]))
                if field_len>length:
                    data[i][field] = str(data[i][field])[:length] + str('*'*(field_len-length))
    return data

def lelf_to_right_method(data, fields, length, mask_result_lenght):
    if mask_result_lenght:
        for i in range(len(data)):
            for field in fields:
                field_len = len(str(data[i][field]))
                if field_len>length:
                    data[i][field] = "*" + str(data[i][field])[field_len-length:]
    else:
        for i in range(len(data)):
            for field in fields:
                field_len = len(str(data[i][field]))
                if field_len>length:
                    data[i][field] = str('*'*(field_len-length)) + str(data[i][field])[field_len-length:]
    return data

def email_method(data, fields):
    for i in range(len(data)):
        for field in fields:
            email = str(data[i][field])
            dominioEmail = email.split("@")
            data[i][field] = dominioEmail[1]
    return data

def cpf_method(data, fields, masked):
    if masked:
        for i in range(len(data)):
            for field in fields:
                cpf = str(data[i][field])
                new_cpf = "***.***." + cpf[9:11] + "-**"
                data[i][field] = new_cpf
    else: 
        for i in range(len(data)):
            for field in fields:
                cpf = str(data[i][field])
                new_cpf = "******" + cpf[7:9] + "**"
                data[i][field] = new_cpf
    return data

def credit_card_method(data, fields):
    for i in range(len(data)):
        for field in fields:
            card_number = str(data[i][field])
            card_number_len = len(card_number)
            new_card_number = str('*'*(card_number_len-4)) + card_number[card_number_len-4:]
            data[i][field] = new_card_number
    return data

