import template

def postman_collection(data, nome_projeto: str, entidades):
    data = set_name_postman(data, nome_projeto)

    for entidade in entidades:
        data["item"].append(template.json_template_crud_postman(entidade))

    return data

def set_name_postman(data, nome_projeto):
    data["info"]["name"] = nome_projeto
    return data