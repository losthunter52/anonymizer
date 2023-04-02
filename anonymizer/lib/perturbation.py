import random


def pertubate_data(
    data,
    method='number_variation',
    variation=0,
    jump=0,
    decimal_places=0
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
