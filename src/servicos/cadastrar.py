from modelos.contato import Contato, contatos

def cadastrar_contato(contato: Contato):
    """Cadastra um novo contato."""
    contatos.append(contato)
    return {"mensagem": "Contato cadastrado com sucesso"}