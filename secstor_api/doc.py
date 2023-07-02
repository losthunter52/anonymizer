doc = [
    {
        "id": "mask",
        "name": "Masking",
        "desc": """Available from anonymizer.lib.data_masking, the algorithm
          data masking can be invoked through the
          mask_data function. The algorithm must receive as a parameter
          an object of type Date (Already processed through the function
          “set_string_fields"), the method to be executed and its
          parameters. After executing the method, the function will update
          the Data object received as a parameter with the anonymized dataset.""",
        "methods": [
            {
                "id": "full",
                "name": "Full",
                "desc": """The fields of objects that pass through this method will
                  have their values ​​masked completely, starting to have the value “*”. """,
                "params": [
                    {
                        "name": "database",
                        "desc": "list of objects that will be anonymized"
                    },
                    {
                        "name": "fields",
                        "desc": "list of fields that will be affected"
                    }
                ],
                "input":   """  import json\n
                                from anonymizer.utils.data import Data\n
                                from anonymizer.lib.data_masking import mask_data\n
                                  \n
                                data =  [\n
                                        {\n
                                            "name": "Wain",\n
                                            "surname": "Mitchard",\n
                                            "fe": "01 - SC",\n
                                            "birth": "01/01/1997",\n
                                            "email": "wain_mitchard@anonymizer.com",\n
                                            "cpf": "111.111.111-11"\n
                                        },\n
                                        {\n
                                            "name": "Mariam",\n
                                            "surname": "Backson",\n
                                            "fe": "01 - SC",\n
                                            "birth": "10/04/1992",\n
                                            "email": "mariam@anonymizer.com",\n
                                            "cpf": "222.222.222-22"\n
                                        },\n
                                        {\n
                                            "name": "Amalea",\n
                                            "surname": "Gambles",\n
                                            "fe": "02 - PR",\n
                                            "birth": "07/02/2001",\n
                                            "email": "amalea.g@anonymizer.com",\n
                                            "cpf": "333.333.333-33"\n
                                        }\n
                                    ]\n
                                  \n
                                fields = [\n
                                          "surname"\n
                                         ]\n
                                  \n
                                data = Data(data)\n
                                  \n
                                data.set_string_fields(fields)\n
                                data = mask_data(data=data, method='full')\n\n
                                print(json.dumps(data.get_database(), indent=4))""",
                "output":   """[\n
                                   {\n
                                     "name": "Wain",\n
                                     "surname": "*",\n
                                     "fe": "01 - SC",\n
                                     "birth": "01/01/1997",\n
                                     "email": "wain_mitchard@anonymizer.com",\n
                                     "cpf": "111.111.111-11"\n
                                   },\n
                                   {\n
                                     "name": "Mariam",\n
                                     "surname": "*",\n
                                     "fe": "01 - SC",\n
                                     "birth": "10/04/1992",\n
                                     "email": "mariam@anonymizer.com",\n
                                     "cpf": "222.222.222-22"\n
                                   },\n
                                   {\n
                                     "name": "Amalea",\n
                                     "surname": "*",\n
                                     "fe": "02 - PR",\n
                                     "birth": "07/02/2001",\n
                                     "email": "amalea.g@anonymizer.com",\n
                                     "cpf": "333.333.333-33"\n
                                   }\n
                                ]"""          
            },
            {
                "id": "posit",
                "name": "Positional",
                "desc": """The fields of objects that pass through this method will 
                be masked in order to present in their output values ​​only the string
                range defined through the initial_rage and final_range parameters, 
                added a “*” at the beginning/end of the value if necessary. """,
                "params": [
                    {
                        "name": "database",
                        "desc": "list of objects that will be anonymized"
                    },
                    {
                        "name": "fields",
                        "desc": "list of fields that will be affected"
                    },
                    {
                        "name": "initial_range",
                        "desc": "initial position of values"
                    },
                    {
                        "name": "final_range",
                        "desc": "final position of values"
                    }
                ],
                "input":   """  import json\n
                                from anonymizer.utils.data import Data\n
                                from anonymizer.lib.data_masking import mask_data\n
                                  \n
                                data =  [\n
                                        {\n
                                            "name": "Wain",\n
                                            "surname": "Mitchard",\n
                                            "fe": "01 - SC",\n
                                            "birth": "01/01/1997",\n
                                            "email": "wain_mitchard@anonymizer.com",\n
                                            "cpf": "111.111.111-11"\n
                                        },\n
                                        {\n
                                            "name": "Mariam",\n
                                            "surname": "Backson",\n
                                            "fe": "01 - SC",\n
                                            "birth": "10/04/1992",\n
                                            "email": "mariam@anonymizer.com",\n
                                            "cpf": "222.222.222-22"\n
                                        },\n
                                        {\n
                                            "name": "Amalea",\n
                                            "surname": "Gambles",\n
                                            "fe": "02 - PR",\n
                                            "birth": "07/02/2001",\n
                                            "email": "amalea.g@anonymizer.com",\n
                                            "cpf": "333.333.333-33"\n
                                        }\n
                                    ]\n
                                  \n
                                fields = [\n
                                          "surname"\n
                                         ]\n
                                  \n
                                data = Data(data)\n
                                  \n
                                data.set_string_fields(fields)\n
                                data = mask_data(data=data, method='positional', initial_range=1, final_range=3)\n\n
                                print(json.dumps(data.get_database(), indent=4))""",
                "output":   """[\n
                                   {\n
                                     "name": "Wain",\n
                                     "surname": "Mit*",\n
                                     "fe": "01 - SC",\n
                                     "birth": "01/01/1997",\n
                                     "email": "wain_mitchard@anonymizer.com",\n
                                     "cpf": "111.111.111-11"\n
                                   },\n
                                   {\n
                                     "name": "Mariam",\n
                                     "surname": "Bac*",\n
                                     "fe": "01 - SC",\n
                                     "birth": "10/04/1992",\n
                                     "email": "mariam@anonymizer.com",\n
                                     "cpf": "222.222.222-22"\n
                                   },\n
                                   {\n
                                     "name": "Amalea",\n
                                     "surname": "Gam*",\n
                                     "fe": "02 - PR",\n
                                     "birth": "07/02/2001",\n
                                     "email": "amalea.g@anonymizer.com",\n
                                     "cpf": "333.333.333-33"\n
                                   }\n
                                ]"""     
            },
            {
                "id": "rtl",
                "name": "Right to Left",
                "desc": """The fields of objects that pass through this method will be masked in order to present,
                in a non-masked form, at most the first N characters of the input values, where N = length, plus
                one or more “*” at the end of the string if necessary. """,
                "params": [
                    {
                        "name": "database",
                        "desc": "list of objects that will be anonymized"
                    },
                    {
                        "name": "fields",
                        "desc": "list of fields that will be affected"
                    },
                    {
                        "name": "length",
                        "desc": "the maximum number of unmasked characters"
                    },
                    {
                        "name": "mask_result_lenght",
                        "desc": "Whether the string should keep its original length or mask it."
                    }
                ],
                "input":   """import json\n
                                from anonymizer.utils.data import Data\n
                                from anonymizer.lib.data_masking import mask_data\n
                                  \n
                                data =  [\n
                                        {\n
                                            "name": "Wain",\n
                                            "surname": "Mitchard",\n
                                            "fe": "01 - SC",\n
                                            "birth": "01/01/1997",\n
                                            "email": "wain_mitchard@anonymizer.com",\n
                                            "cpf": "111.111.111-11"\n
                                        },\n
                                        {\n
                                            "name": "Mariam",\n
                                            "surname": "Backson",\n
                                            "fe": "01 - SC",\n
                                            "birth": "10/04/1992",\n
                                            "email": "mariam@anonymizer.com",\n
                                            "cpf": "222.222.222-22"\n
                                        },\n
                                        {\n
                                            "name": "Amalea",\n
                                            "surname": "Gambles",\n
                                            "fe": "02 - PR",\n
                                            "birth": "07/02/2001",\n
                                            "email": "amalea.g@anonymizer.com",\n
                                            "cpf": "333.333.333-33"\n
                                        }\n
                                    ]\n
                                  \n
                                fields = [\n
                                          "surname"\n
                                         ]\n
                                  \n
                                data = Data(data)\n
                                  \n
                                data.set_string_fields(fields)\n
                                data = mask_data(data=data, method='right_to_left', length=5, mask_result_lenght=False)\n\n
                                print(json.dumps(data.get_database(), indent=4))""",
                "output":   """[\n
                                   {\n
                                     "name": "Wain",\n
                                     "surname": "Mitch***",\n
                                     "fe": "01 - SC",\n
                                     "birth": "01/01/1997",\n
                                     "email": "wain_mitchard@anonymizer.com",\n
                                     "cpf": "111.111.111-11"\n
                                   },\n
                                   {\n
                                     "name": "Mariam",\n
                                     "surname": "Backs**",\n
                                     "fe": "01 - SC",\n
                                     "birth": "10/04/1992",\n
                                     "email": "mariam@anonymizer.com",\n
                                     "cpf": "222.222.222-22"\n
                                   },\n
                                   {\n
                                     "name": "Amalea",\n
                                     "surname": "Gambl**",\n
                                     "fe": "02 - PR",\n
                                     "birth": "07/02/2001",\n
                                     "email": "amalea.g@anonymizer.com",\n
                                     "cpf": "333.333.333-33"\n
                                   }\n
                                ]"""                                     
            },
            {
                "id": "ltr",
                "name": "Left to Right",
                "desc": """The fields of objects that pass through this method will be masked in order to present, 
                in a non-masked form, at most the last N characters of the input values, where N = length, plus 
                one or more “*” at the begin of the string if necessary.""",
                "params": [
                    {
                        "name": "database",
                        "desc": "list of objects that will be anonymized"
                    },
                    {
                        "name": "fields",
                        "desc": "list of fields that will be affected"
                    },
                    {
                        "name": "length",
                        "desc": "the maximum number of unmasked characters"
                    },
                    {
                        "name": "mask_result_lenght",
                        "desc": "Whether the string should keep its original length or mask it."
                    }
                ],
                "input":   """import json\n
                                from anonymizer.utils.data import Data\n
                                from anonymizer.lib.data_masking import mask_data\n
                                  \n
                                data =  [\n
                                        {\n
                                            "name": "Wain",\n
                                            "surname": "Mitchard",\n
                                            "fe": "01 - SC",\n
                                            "birth": "01/01/1997",\n
                                            "email": "wain_mitchard@anonymizer.com",\n
                                            "cpf": "111.111.111-11"\n
                                        },\n
                                        {\n
                                            "name": "Mariam",\n
                                            "surname": "Backson",\n
                                            "fe": "01 - SC",\n
                                            "birth": "10/04/1992",\n
                                            "email": "mariam@anonymizer.com",\n
                                            "cpf": "222.222.222-22"\n
                                        },\n
                                        {\n
                                            "name": "Amalea",\n
                                            "surname": "Gambles",\n
                                            "fe": "02 - PR",\n
                                            "birth": "07/02/2001",\n
                                            "email": "amalea.g@anonymizer.com",\n
                                            "cpf": "333.333.333-33"\n
                                        }\n
                                    ]\n
                                  \n
                                fields = [\n
                                          "surname"\n
                                         ]\n
                                  \n
                                data = Data(data)\n
                                  \n
                                data.set_string_fields(fields)\n
                                data = mask_data(data=data, method='left_to_right', length=5, mask_result_lenght=True)\n\n
                                print(json.dumps(data.get_database(), indent=4))""",
                "output":   """[\n
                                   {\n
                                     "name": "Wain",\n
                                     "surname": "*chard",\n
                                     "fe": "01 - SC",\n
                                     "birth": "01/01/1997",\n
                                     "email": "wain_mitchard@anonymizer.com",\n
                                     "cpf": "111.111.111-11"\n
                                   },\n
                                   {\n
                                     "name": "Mariam",\n
                                     "surname": "*ckson",\n
                                     "fe": "01 - SC",\n
                                     "birth": "10/04/1992",\n
                                     "email": "mariam@anonymizer.com",\n
                                     "cpf": "222.222.222-22"\n
                                   },\n
                                   {\n
                                     "name": "Amalea",\n
                                     "surname": "*mbles",\n
                                     "fe": "02 - PR",\n
                                     "birth": "07/02/2001",\n
                                     "email": "amalea.g@anonymizer.com",\n
                                     "cpf": "333.333.333-33"\n
                                   }\n
                                ]"""        
            },
            {
                "id": "email",
                "name": "E-Mail",
                "desc": """The emails that go through this method will be masked through a division
                that will only separate their domains. This division will occur through a Split of the 
                “@” character. If there is no “@” character in the input value, the value “email.com” 
                will be assigned as domain, and if there is more than one “@” character, everything after 
                the first “@” will be assigned as domain.""",
                "params": [
                    {
                        "name": "database",
                        "desc": "list of objects that will be anonymized"
                    },
                    {
                        "name": "fields",
                        "desc": "list of fields that will be affected"
                    }
                ],
                "input":   """import json\n
                                from anonymizer.utils.data import Data\n
                                from anonymizer.lib.data_masking import mask_data\n
                                  \n
                                data =  [\n
                                        {\n
                                            "name": "Wain",\n
                                            "surname": "Mitchard",\n
                                            "fe": "01 - SC",\n
                                            "birth": "01/01/1997",\n
                                            "email": "wain_mitchard@anonymizer.com",\n
                                            "cpf": "111.111.111-11"\n
                                        },\n
                                        {\n
                                            "name": "Mariam",\n
                                            "surname": "Backson",\n
                                            "fe": "01 - SC",\n
                                            "birth": "10/04/1992",\n
                                            "email": "mariam@anonymizer.com",\n
                                            "cpf": "222.222.222-22"\n
                                        },\n
                                        {\n
                                            "name": "Amalea",\n
                                            "surname": "Gambles",\n
                                            "fe": "02 - PR",\n
                                            "birth": "07/02/2001",\n
                                            "email": "amalea.g@anonymizer.com",\n
                                            "cpf": "333.333.333-33"\n
                                        }\n
                                    ]\n
                                  \n
                                fields = [\n
                                          "cpf"\n
                                         ]\n
                                  \n
                                data = Data(data)\n
                                  \n
                                data.set_string_fields(fields)\n
                                data = mask_data(data=data, method='email')\n\n
                                print(json.dumps(data.get_database(), indent=4))""",
                "output":   """[\n
                                   {\n
                                     "name": "Wain",\n
                                     "surname": "Mitchard",\n
                                     "fe": "01 - SC",\n
                                     "birth": "01/01/1997",\n
                                     "email": "anonymizer.com",\n
                                     "cpf": "111.111.111-11"\n
                                   },\n
                                   {\n
                                     "name": "Mariam",\n
                                     "surname": "Backson",\n
                                     "fe": "01 - SC",\n
                                     "birth": "10/04/1992",\n
                                     "email": "anonymizer.com",\n
                                     "cpf": "222.222.222-22"\n
                                   },\n
                                   {\n
                                     "name": "Amalea",\n
                                     "surname": "Gambles",\n
                                     "fe": "02 - PR",\n
                                     "birth": "07/02/2001",\n
                                     "email": "anonymizer.com",\n
                                     "cpf": "333.333.333-33"\n
                                   }\n
                                ]"""                                   
            },
            {
                "id": "cpf",
                "name": "CPF",
                "desc": """The method expects that the fields of the stored objects have a CPF as a value,
                which will be masked to display only the first two digits and the two penultimate digits 
                of the CPF. """,
                "params": [
                    {
                        "name": "database",
                        "desc": "list of objects that will be anonymized"
                    },
                    {
                        "name": "fields",
                        "desc": "list of fields that will be affected"
                    },
                    {
                        "name": "masked",
                        "desc": "identifies whether the incoming CPF is masked"
                    }
                ],
                "input":   """import json\n
                                from anonymizer.utils.data import Data\n
                                from anonymizer.lib.data_masking import mask_data\n
                                  \n
                                data =  [\n
                                        {\n
                                            "name": "Wain",\n
                                            "surname": "Mitchard",\n
                                            "fe": "01 - SC",\n
                                            "birth": "01/01/1997",\n
                                            "email": "wain_mitchard@anonymizer.com",\n
                                            "cpf": "111.111.111-11"\n
                                        },\n
                                        {\n
                                            "name": "Mariam",\n
                                            "surname": "Backson",\n
                                            "fe": "01 - SC",\n
                                            "birth": "10/04/1992",\n
                                            "email": "mariam@anonymizer.com",\n
                                            "cpf": "222.222.222-22"\n
                                        },\n
                                        {\n
                                            "name": "Amalea",\n
                                            "surname": "Gambles",\n
                                            "fe": "02 - PR",\n
                                            "birth": "07/02/2001",\n
                                            "email": "amalea.g@anonymizer.com",\n
                                            "cpf": "333.333.333-33"\n
                                        }\n
                                    ]\n
                                  \n
                                fields = [\n
                                          "email"\n
                                         ]\n
                                  \n
                                data = Data(data)\n
                                  \n
                                data.set_string_fields(fields)\n
                                data = mask_data(data=data, method='cpf', masked=True)\n\n
                                print(json.dumps(data.get_database(), indent=4))""",
                "output":   """[\n
                                   {\n
                                     "name": "Wain",\n
                                     "surname": "Mitchard",\n
                                     "fe": "01 - SC",\n
                                     "birth": "01/01/1997",\n
                                     "email": "wain_mitchard@anonymizer.com",\n
                                     "cpf": "11*.***.*11-**"\n
                                   },\n
                                   {\n
                                     "name": "Mariam",\n
                                     "surname": "Backson",\n
                                     "fe": "01 - SC",\n
                                     "birth": "10/04/1992",\n
                                     "email": "mariam@anonymizer.com",\n
                                     "cpf": "22*.***.*22-**"\n
                                   },\n
                                   {\n
                                     "name": "Amalea",\n
                                     "surname": "Gambles",\n
                                     "fe": "02 - PR",\n
                                     "birth": "07/02/2001",\n
                                     "email": "amalea.g@anonymizer.com",\n
                                     "cpf": "33*.***.*33-**"\n
                                   }\n
                                ]"""    
            },
        ],
    },
    {
        "id": "pert",
        "name": "Perturbation",
        "desc": """desc desc desc desc desc desc """,
        "methods": [
            {
                "id": "numv",
                "name": "number_variation"
            },
            {
                "id": "randnumv",
                "name": "random_number_variation"
            },
        ],
    },
    {
        "id": "null-out",
        "name": 'Nulling Out',
        "desc": """Available at anonymizer.lib.nulling_out, the data nulling algorithm can be called through the null_data function and its purpose is to perform the complete removal of the informed fields.""",
        "methods": [
            {
                "id": "nullout",
                "name": "Null Out",
                "desc": """The fields of objects that pass through this method will be completely removed from the dataset.""",
                "params": [
                    {
                        "name": "data",
                        "desc": "Data object already prepared through the prepare_fields function."
                    }
                ],
                "input":   """import json\n
                                from anonymizer.utils.data import Data\n
                                from anonymizer.lib.nulling_out import null_out\n
                                  \n
                                data =  [\n
                                        {\n
                                            "name": "Wain",\n
                                            "surname": "Mitchard",\n
                                            "fe": "01 - SC",\n
                                            "birth": "01/01/1997",\n
                                            "email": "wain_mitchard@anonymizer.com",\n
                                            "cpf": "111.111.111-11"\n
                                        },\n
                                        {\n
                                            "name": "Mariam",\n
                                            "surname": "Backson",\n
                                            "fe": "01 - SC",\n
                                            "birth": "10/04/1992",\n
                                            "email": "mariam@anonymizer.com",\n
                                            "cpf": "222.222.222-22"\n
                                        },\n
                                        {\n
                                            "name": "Amalea",\n
                                            "surname": "Gambles",\n
                                            "fe": "02 - PR",\n
                                            "birth": "07/02/2001",\n
                                            "email": "amalea.g@anonymizer.com",\n
                                            "cpf": "333.333.333-33"\n
                                        }\n
                                    ]\n
                                  \n
                                fields = [\n
                                          "name",\n
                                          "cpf"\n
                                         ]\n
                                  \n
                                data = Data(data)\n
                                  \n
                                data.prepare_fields(fields)\n
                                data = null_out(data)\n\n
                                print(json.dumps(data.get_database(), indent=4))""",
                "output":   """[\n
                                   {\n
                                     "surname": "Mitchard",\n
                                     "fe": "01 - SC",\n
                                     "birth": "01/01/1997",\n
                                     "email": "wain_mitchard@anonymizer.com"\n
                                   },\n
                                   {\n
                                     "surname": "Backson",\n
                                     "fe": "01 - SC",\n
                                     "birth": "10/04/1992",\n
                                     "email": "mariam@anonymizer.com"\n
                                   },\n
                                   {\n
                                     "surname": "Gambles",\n
                                     "fe": "02 - PR",\n
                                     "birth": "07/02/2001",\n
                                     "email": "amalea.g@anonymizer.com"\n
                                   }\n
                                ]"""      
            }
        ],

    },
    {
        "id": "swapp",
        "name": "Swapping",
        "desc": """desc desc desc desc desc desc """,
        "methods": [
            {
                "id": "randsub",
                "name": "random_substitution"
            }
        ],
    },
        {
        "id": "hashing",
        "name": "Hashing",
        "desc": """Available at anonymizer.lib.nulling_out, the data hash algorithm can be called through 
        the hash_data function and has the objective of performing hash functions on the content of 
        the informed fields.""",
        "methods": [
            {
                "id": "hash_data",
                "name": "Hash Data",
                "desc": """The fields of objects passed through will be replaced by the result of a hash 
                method executed on it. Currently the algorithm has support for md5, sha1 and sha256 hash 
                methods.""",
                "params": [
                    {
                        "name": "data",
                        "desc": "Data object already prepared through the prepare_fields function."
                    },
                    {
                        "name": "method",
                        "desc": "hash method to be utilized"
                    }
                ],
                "input":   """import json\n
                                from anonymizer.utils.data import Data\n
                                from anonymizer.lib.hashing import hash_data\n
                                  \n
                                data =  [\n
                                        {\n
                                            "name": "Wain",\n
                                            "surname": "Mitchard",\n
                                            "fe": "01 - SC",\n
                                            "birth": "01/01/1997",\n
                                            "email": "wain_mitchard@anonymizer.com",\n
                                            "cpf": "111.111.111-11"\n
                                        },\n
                                        {\n
                                            "name": "Mariam",\n
                                            "surname": "Backson",\n
                                            "fe": "01 - SC",\n
                                            "birth": "10/04/1992",\n
                                            "email": "mariam@anonymizer.com",\n
                                            "cpf": "222.222.222-22"\n
                                        },\n
                                        {\n
                                            "name": "Amalea",\n
                                            "surname": "Gambles",\n
                                            "fe": "02 - PR",\n
                                            "birth": "07/02/2001",\n
                                            "email": "amalea.g@anonymizer.com",\n
                                            "cpf": "333.333.333-33"\n
                                        }\n
                                    ]\n
                                  \n
                                fields = [\n
                                          "name",\n
                                          "surname",\n
                                          "email",\n
                                          "cpf"\n
                                         ]\n
                                  \n
                                data = Data(data)\n
                                  \n
                                data.set_string_fields(fields)\n
                                data = hash_data(data=data, method='sha256')\n\n
                                print(json.dumps(data.get_database(), indent=4))""",
                "output":   """[\n
                                   {\n
                                     "name": "485b0ece00ac7255c2d48d82ccb39423180b10c412f6ae7bf1976169c8792be7",\n
                                     "surname": "0af60cc1307f00c6bcf2fc68f94065ac977550541fa4b639fd0a862101a3b505",\n
                                     "fe": "01 - SC",\n
                                     "birth": "01/01/1997",\n
                                     "email": "a8acf104ef6c7fc3a9eb564df823877f194e338a58af85f46173f83420928387",\n
                                     "cpf": "a3a17c4901071c0d73dcecb9de6cb3bf839204eb4b031b0562c6a972839a01bc"\n
                                   },\n
                                   {\n
                                     "name": "af51fbbe0358aba96ca96033aacccec4d6bf1261a3777eade9aa739dd8a8beb1",\n
                                     "surname": "bc621c1c593deb8a0a6176eac2680e9a7a78daeec26c3ab65321a0c43fa8eb52",\n
                                     "fe": "01 - SC",\n
                                     "birth": "10/04/1992",\n
                                     "email": "ee32c158d614a82d847bd10f4526718c120a42e987359eabc34bb9c88bfd98de",\n
                                     "cpf": "33a4ee11c86eb213ab9ae7528ec524d2e4c56707fe69522037daca670b46e898"\n
                                   },\n
                                   {\n
                                     "name": "acae5db1b514a090a467b38e25b2c880477cd0850d4778898c7c3d07fd859dd0",\n
                                     "surname": "2111931529c6c8213a7133d87cab3a7b0a31559ad4ce77dd943c6d535079f3a8",\n
                                     "fe": "02 - PR",\n
                                     "birth": "07/02/2001",\n
                                     "email": "ca76be310b738423d30e998fa68d3d8bf5825b5e6e9f2f68bef06cd6f3d162bb",\n
                                     "cpf": "33a4ee11c86eb213ab9ae7528ec524d2e4c56707fe69522037daca670b46e898"\n
                                   }\n
                                ]"""      
            }
        ],
    },
]
