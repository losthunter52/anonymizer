from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError
from .schemas import schema, schema_methods, result_schema


def validate_request(request):
    payload = request.data
    try:
        validate(payload, schema())
        for param in payload['params']:
            validate(param, schema_methods(param['tool']))
        return True
    except ValidationError as error:
        return {"Validation Error": error.message}
    except SchemaError as error:
        return {"Schema Error": error.message}

def validade_result_request(request):
    payload = request.data
    try:
        validate(payload, result_schema())
        return True
    except ValidationError as error:
        return {"Validation Error": error.message}
    except SchemaError as error:
        return {"Schema Error": error.message}
