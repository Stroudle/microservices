from modelos.contato import contatos

def consultar_contato(nome: str):
    """Consulta um contato pelo nome."""
    for contato in contatos:
        if contato.nome == nome:
            return contato
    return {"message": "Contato não encontrado."}