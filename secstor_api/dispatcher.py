from anonymizer.utils.data import Data
from anonymizer.lib.data_masking import mask_data
from anonymizer.lib.nulling_out import null_out
from anonymizer.lib.perturbation import pertubate_data
from anonymizer.lib.swapping import swap_data
from anonymizer.lib.hashing import hash_data
from anonymizer.lib.pseudonymization import psedoanonymize_data
from anonymizer.lib.encryption import encript_data
from .validators.validate import validate_request
from .config import tools, VALIDATION 
import json
from copy import deepcopy

def process_data(request):
    test = True
    if VALIDATION:
        test = validate_request(request)
    if test == True:
        return dispatch(request)
    else:
        return test


def dispatch(request):
    log = []
    payload = request['data']
    data = Data(payload['database'])
    for param in payload['params']:
        tool = param['tool']
        arguments = deepcopy(tools[tool])
        fields = param['fields']
        if 'config' in param:
            for parameter in param['config']:
                if parameter in arguments:
                    arguments[parameter]['default'] = param['config'][parameter]
        caller(arguments, tool, fields, data)
    log = data.get_log()
    response = {}
    if log:
        response.update({'log':log})
    database = json.loads(json.dumps(data.get_database(), sort_keys=True))
    response.update({'database':database})
    return response

def caller(arguments, tool, fields, data):
    if tool == "masking":
            data.set_string_fields(fields)
            data = mask_data(
                data,
                arguments['method']['default'],
                arguments['length']['default'],
                arguments['masked']['default'],
                arguments['initial_rage']['default'],
                arguments['final_range']['default'],
                arguments['mask_result_lenght']['default']
            )
    if tool == "nulling_out":
            data.prepare_fields(fields)
            data = null_out(data)
    if tool == "perturbation":
            if arguments['method']['default'] == "number_variation":
                    data.set_numeric_fields(fields)
            if arguments['method']['default'] == "random_number_variation":
                    data.set_numeric_fields(fields)
            if arguments['method']['default'] == "time_variation":
                    data.set_string_fields(fields)
            if arguments['method']['default'] == "time_variation":
                    data.set_string_fields(fields)
            if arguments['method']['default'] == "random_time_variation":
                    data.set_string_fields(fields)
            if arguments['method']['default'] == "date_variation":
                    data.set_string_fields(fields)
            if arguments['method']['default'] == "random_date_variation":
                    data.set_string_fields(fields)
            data = pertubate_data(
                data,
                arguments['method']['default'],
                arguments['variation']['default'],
                arguments['jump']['default'],
                arguments['decimal_places']['default'],
                arguments['format']['default'],
            )
    if tool == "swapping":
            data.set_string_fields(fields)
            data = swap_data(data, arguments['method']['default'])
    if tool == "hashing":
            data.set_string_fields(fields)
            data = hash_data(data, arguments['method']['default'])
    if tool == "pseudonymization":    
            data.set_string_fields(fields)
            data = psedoanonymize_data(data,
                arguments['method']['default'],
                arguments['standard_value']['default'],
                arguments['replacements']['default'])
    if tool == "encryption":
            data.set_string_fields(fields)
            data = encript_data(data, arguments['method']['default'])
    return data
