var spec = {
    "openapi": "3.0.1",
    "info": {
      "version": "1.0.0",
      "title": "API Specification Example Anonymizer "
    },
    "paths": {
      "/anonymizer": {
        "post": {
          "summary": "Create an article.",
          "operationId": "createArticle",
          "tags": [
            "Anonymizer API"
          ],
          "requestBody": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DataBase"
                }
              }
            }
          },
          "x-swagger-ui": {
            "operationsSorter": "method"
          }
        }
      }
    },
    "components": {
      "schemas": {
       
        "Params": {
          "properties": {
            "id": {
              "$ref": "#/components/schemas/Id"
            },
            "params:": {
              "description": "Category of an params",
              "type": "string",
              "example":  [
                {
                    "tool": "masking",
                    "config": {
                        "method": "right_to_left",
                        "length": 5,
                        "mask_result_lenght": false
                    },
                    "fields": [
                        "nome",
                        "sobrenome"
                    ]
                }
            ],
            }
          }
        },
        "DataBase": {
          "allOf": [
            {
              "$ref": "#/components/schemas/Params"
            }
          ],
          "required": [
            "text"
          ],
          "properties": {
            "database": {
              "description": "Content of an params",
              "type": "string",
              "maxLength": 1024,
              "example": [
                {
                    "nome": "Wain",
                    "sobrenome": "Mitchard"
                },
                {
                    "nome": "Mariam",
                    "sobrenome": "Backson"
                    
                
                },
                {
                    "nome": "Amalea",
                    "sobrenome": "Gambles"
                }
            ]
            }
          }
        },
       
      },
      
      "responses": {
        
      }
    }
  }
  