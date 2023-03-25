from anonymizer.anonymize import prepare, mask,num_variation


def dispatch(request):
    log = []
    payload = request.data
    database = payload['database']
    data = database
    for param in payload['params']:
        prepare_database = prepare(data, param['fields'])
        data = prepare_database['database']
        fields = prepare_database['fields']
        if prepare_database['log'] != "":
            log.append(prepare_database['log'])
        match param['tool']:
            case "masking":
                method="full"
                length=0
                masked=False
                initial_rage=0
                final_range=0
                mask_result_lenght=False
                if 'config' in param:
                    if 'method' in param['config']:
                        method = param['config']['method']
                    if 'length' in param['config']:
                        length = param['config']['length']
                    if 'masked' in param['config']:
                        masked = param['config']['masked']
                    if 'initial_rage' in param['config']:
                        initial_rage = param['config']['initial_rage']
                    if 'final_range' in param['config']:
                        final_range = param['config']['final_range']
                    if 'mask_result_lenght' in param['config']:
                        mask_result_lenght = param['config']['mask_result_lenght']
                data = mask(
                    data,
                    fields,
                    method,
                    length,
                    masked,
                    initial_rage,
                    final_range,
                    mask_result_lenght
                )
            case "number_variation":
                data = num_variation(
                    data,
                    fields
                )
    return { "log": log, "database": data }
