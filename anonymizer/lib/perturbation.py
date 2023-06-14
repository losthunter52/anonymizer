import random
import datetime

def pertubate_data(
    data,
    method='number_variation',
    variation=0,
    jump=0,
    decimal_places=0,
    format=''
):
    database = data.get_database()
    fields = data.get_fields()

    match method:
        case "number_variation":
            data.update_database(number_variation(
                database, fields, variation, jump, decimal_places))
        case "random_number_variation":
            data.update_database(random_number_variation(
                data, variation, jump, decimal_places))
        case "time_variation":
            data.update_database(time_variation(data, variation, format))
        case "random_time_variation":
            data.update_database(random_time_variation(data, variation, format))
        case "date_variation":
            data.update_database(date_variation(data, variation, format))
        case "random_date_variation":
            data.update_database(random_date_variation(data, variation, format))
    return data


def number_variation(database, fields, variation, jump, decimal_places):
    limit = variation - (variation % jump)
    limit = variation / jump

    for i in range(len(database)):
        for field in fields:
            variation = random.randint(-limit, limit)
            variation = variation * jump
            value = round(
                (database[i][field] + variation), decimal_places)
            format = "%." + str(decimal_places) + "f"
            value = (format % value)
            database[i][field] = value
    return database


def random_number_variation(data, variation, jump, decimal_places):
    database = data.get_database()
    fields = data.get_fields()
    limit = variation - (variation % jump)
    limit = variation / jump
    key = []

    for i in range(len(database)):
        for field in fields:
            variation = random.randint(-limit, limit)
            variation = variation * jump
            variation = round(variation, decimal_places)
            key.append(variation)
            value = database[i][field] + variation
            format = "%." + str(decimal_places) + "f"
            value = (format % value)
            database[i][field] = value
    data.log.add_key("Param [" + str(data.method_counter) + "]:")
    data.log.add_key("Random Number Variation Generated Key:")
    data.log.add_key(key)
    return database

def time_variation(data, variation, format):
    database = data.get_database()
    fields = data.get_fields()

    for i in range(len(database)):
        for field in fields:
            perturbation = random.randint(-variation, variation)
            current_time = datetime.datetime.strptime(database[i][field], format)
            perturbate_time = current_time + datetime.timedelta(minutes=perturbation)
            database[i][field] = perturbate_time.strftime(format)

    return database

def random_time_variation(data, variation, format):
    database = data.get_database()
    fields = data.get_fields()
    key = []

    for i in range(len(database)):
        for field in fields:
            perturbation = random.randint(-variation, variation)
            key.append(perturbation)
            current_time = datetime.datetime.strptime(database[i][field], format)
            perturbate_time = current_time + datetime.timedelta(minutes=perturbation)
            database[i][field] = perturbate_time.strftime(format)
    data.log.add_key("Param [" + str(data.method_counter) + "]:")
    data.log.add_key("Random Time Variation Generated Key:")
    data.log.add_key(key)
    return database

def date_variation(data, variation, format):
    database = data.get_database()
    fields = data.get_fields()

    for i in range(len(database)):
        for field in fields:
            perturbation = random.randint(-variation, variation)
            current_date = datetime.datetime.strptime(database[i][field], format)
            perturbate_date = current_date + datetime.timedelta(days=perturbation)
            database[i][field] = perturbate_date.strftime(format)
    
    return database

def random_date_variation(data, variation, format):
    database = data.get_database()
    fields = data.get_fields()
    key = []

    for i in range(len(database)):
        for field in fields:
            perturbation = random.randint(-variation, variation)
            key.append(perturbation)
            current_date = datetime.datetime.strptime(database[i][field], format)
            perturbate_date = current_date + datetime.timedelta(days=perturbation)
            database[i][field] = perturbate_date.strftime(format)
    data.log.add_key("Param [" + str(data.method_counter) + "]:")
    data.log.add_key("Random Date Variation Generated Key:")
    data.log.add_key(key)

    return database