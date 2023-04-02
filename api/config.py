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
    'nulling_out': {}
}
