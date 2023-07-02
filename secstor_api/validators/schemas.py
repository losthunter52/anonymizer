from ..config import tools


def schema():
    avaible_tools = []
    for tool in tools:
        avaible_tools.append(tool)
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
                            "type": "object"
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
    return schema


def schema_methods(tool):
    properties = {}
    tool = tools[tool]
    for parameter in tool:
        propertie = dict(tool[parameter])
        propertie.pop('default', None)
        properties.update({parameter: propertie})
    schema = {
        "title": "Param",
        "type": "object",
        "properties": {
            "tool": {"type": "string"},
            "config": {
                "type": "object",
                "properties": properties
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
    return schema

def result_schema():
    schema = {
        "title": "task",
        "type": "object",
        "properties": {
            "task_id": {"type": "string"}
        },
        "required": ["task_id"]
    }
    return schema