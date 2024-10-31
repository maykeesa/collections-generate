import template
import generate_collection

nome_projeto = "Alugueis"
entidades = ["casa", "banheiro", "cozinha", "varanda"]

data = template.get_json_template_default('./templates/postman/postman_collection.json')
data = generate_collection.postman_collection(data, nome_projeto, entidades)
template.save_json_template_modify(nome_projeto, data)

