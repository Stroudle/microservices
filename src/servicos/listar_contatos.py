from modelos.contato import contatos

def listar_contatos():
    """Lista todos os contatos cadastrados."""
    if not contatos:
        return {"message": "Nenhum contato cadastrado."}
    return contatos