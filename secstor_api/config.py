tools = {
    'masking': {
        "method": {
            "type": "string",
            "enum": ['full', 'positional', 'right_to_left', 'left_to_right', 'email', 'cpf'],
            "default": 'full'
        },
        "length": {
            "type": "integer",
            "default": 0
        },
        "masked": {
            "type": "boolean",
            "default": False
        },
        "initial_rage": {
            "type": "integer",
            "default": 0
        },
        "final_range": {
            "type": "integer",
            "default": 0
        },
        "mask_result_lenght": {
            "type": "boolean",
            "default": False
        }
    },
    'perturbation': {
        "method": {
            "type": "string",
            "enum": ['number_variation',
                     'random_number_variation', 
                     'time_variation', 
                     'random_time_variation',
                     'date_variation', 
                     'random_date_variation',],
            "default": 'number_variation'
        },
        "variation": {
            "type": "number",
            "default": 0
        },
        "jump": {
            "type": "number",
            "default": 0
        },
        "decimal_places": {
            "type": "integer",
            "default": 0
        },
        "format": {
            "type": "string",
            "enum": ['%d/%m/%Y',
                     '%Y/%m/%d',
                     '%d-%m-%Y',
                     '%Y-%m-%d',
                     '%H:%M:%S',
                     '%M:%S',
                     '%H:%M'],
            "default": '%d/%m/%Y'
        }
    },
    'nulling_out': {},
    'swapping': {
        "method": {
            "type": "string",
                    "enum": ['random_substitution','group_random_substitution'],
                    "default": 'random_substitution'
        },
    },
    'hashing': {
        "method": {
            "type": "string",
                    "enum": ['md5', 'sha1', 'sha256'],
                    "default": 'md5'
        },
    },
    'pseudonymization': {
        "replacements": {
          "type": "object",
          "additionalProperties": {
                  "type": "string"
                 },
            "default": []
        },
        "standard_value": {
            "type": "string",
            "default": "Object"
        },
        "method": {
            "type": "string",
            "enum": ['full','single'],
            "default": 'full'
        }
    },
    'encryption': {
        "method": {
            "type": "string",
                    "enum": ['cryptocode', 'aes256'],
                    "default": 'cryptocode'
        },
    },
}

VALIDATION = False