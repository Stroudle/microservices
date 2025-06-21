from fastapi import FastAPI
from servicos.cadastrar import cadastrar_contato
from servicos.consultar import consultar_contato
from servicos.listar_contatos import listar_contatos
from modelos.contato import Contato

app = FastAPI()

@app.post("/contato/")
def cria_contato(contato: Contato):
    return cadastrar_contato(contato)

@app.get("/contato/{nome}")
def get_contato(nome: str):
    return consultar_contato(nome)

@app.get("/contatos/")
def get_todos_contatos():
    return listar_contatos()