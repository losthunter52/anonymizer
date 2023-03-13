from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

avaible_tools = [
    "masking"
    ]

avaible_methods = [
    "full",
    "positional",
    "right_to_left",
    "left_to_right",
    "email",
    "cpf"
    ]

schema = {
    "title": "Anonymize",
    "type": "object",
    "properties": {
        "params": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "tool": {"type": "string", "enum": avaible_tools},
                    "config": {
                        "type": "object",
                        "properties": {
                            "method": {"type": "string", "enum": avaible_methods},
                            "length": {"type": "integer"},
                            "masked": {"type": "boolean"},
                            "initial_rage": {"type": "integer"},
                            "final_range": {"type": "integer"},
                            "mask_result_lenght": {"type": "boolean"}
                        }
                    },
                    "fields": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                },
                "required": [
                    "tool",
                    "fields"
                ]
            }
        },
        "database": {
            "type": "array",
            "items": {"type": "object"}
        }
    },
    "required": [
        "params",
        "database"
    ]
}

def validate_request(request):
    content_type = request.headers['Content-Type']
    payload = request.data
    if content_type == "application/json":
        try:
            validate(payload, schema)
            return True
        except ValidationError as error:
            return { "Validation Error": error.message }
        except SchemaError as error:
            return { "Schema Error": error.message }
    else:
        return False
