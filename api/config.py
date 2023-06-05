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
            "enum": ['number_variation', 'random_number_variation'],
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
        }
    },
    'nulling_out': {},
    'swapping': {
        "method": {
            "type": "string",
                    "enum": ['random_substitution'],
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
