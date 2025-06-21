import requests

BASE_URL = "http://127.0.0.1:8000"

# Contato para teste
contato = {
    "nome": "Julia Moura",
    "numero_telefone": "51998888888",
    "tipo_telefone": "movel",
    "categoria_contato": "familia"
}

# Cadastrar contato
resp = requests.post(f"{BASE_URL}/contato/", json=contato)
print("Cadastro:", resp.status_code, resp.json())

# Consultar contato pelo nome
resp = requests.get(f"{BASE_URL}/contato/Julia Moura")
print("Consulta:", resp.status_code, resp.json())

# Listar todos os contatos
resp = requests.get(f"{BASE_URL}/contatos/")
print("Listagem:", resp.status_code, resp.json())