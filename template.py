import json

def get_json_template_default(path: str):
    with open(path, 'r') as f:
        return json.load(f)

def save_json_template_modify(nome_projeto: str, data):
    try:
        with open(f'/home/maykeesa/Downloads/{nome_projeto}.postman_collection.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        print("| Collection Postman gerada com SUCESSO. |")
    except Exception as ex:
        print("| Houve alguma FALHA na geração da Collection. |")
        print("\n" * 10)
        print(ex)

def json_template_crud_postman(entity_name):
    base_item = {
        "name": entity_name.capitalize(),
        "item": [
            {
                "name": f"/{entity_name}",
                "request": {
                    "method": "GET",
                    "header": [],
                    "url": {
                        "raw": f"{{{{localhost}}}}/{entity_name}",
                        "host": ["{{localhost}}"],
                        "path": [entity_name]
                    }
                },
                "response": []
            },
            {
                "name": f"/{entity_name}/{{id}}",
                "request": {
                    "method": "GET",
                    "header": [],
                    "url": {
                        "raw": f"{{{{localhost}}}}/{entity_name}//{{id}}",
                        "host": ["{{localhost}}"],
                        "path": [entity_name, 1]
                    }
                },
                "response": []
            },
            {
                "name": f"/{entity_name}",
                "request": {
                    "method": "POST",
                    "header": [
                        {"key": "Content-Type", "value": "application/json", "type": "text"}
                    ],
                    "body": {"mode": "raw", "raw": " "},
                    "url": {
                        "raw": f"{{{{localhost}}}}/{entity_name}",
                        "host": ["{{localhost}}"],
                        "path": [entity_name]
                    }
                },
                "response": []
            },
            {
                "name": f"/{entity_name}/{{id}}",
                "request": {
                    "method": "PUT",
                    "header": [
                        {"key": "Content-Type", "value": "application/json", "type": "text"}
                    ],
                    "body": {"mode": "raw", "raw": ""},
                    "url": {
                        "raw": f"{{{{localhost}}}}/{entity_name}/{{id}}",
                        "host": ["{{localhost}}"],
                        "path": [entity_name, "1"]
                    }
                },
                "response": []
            },
            {
                "name": f"/{entity_name}/{{id}}",
                "request": {
                    "method": "DELETE",
                    "header": [],
                    "url": {
                        "raw": f"{{{{localhost}}}}/{entity_name}/{{id}}",
                        "host": ["{{localhost}}"],
                        "path": [entity_name, "1"]
                    }
                },
                "response": []
            }
        ]
    }

    return base_item

