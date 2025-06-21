import enum
from pydantic import BaseModel

class TipoTelefone(str, enum.Enum):
    TIPO_TELEFONE_INDEFINIDO = "indefinido"
    MOVEL = "movel"
    FIXO = "fixo"
    COMERCIAL = "comercial"

class CategoriaContato(str, enum.Enum):
    TIPO_CONTATO_INDEFINIDO = "indefinido"
    FAMILIA = "familia"
    AMIGOS = "amigos"
    COMERCIAL = "comercial"
    OUTRO = "outro"

class Contato(BaseModel):
    nome: str
    numero_telefone: str
    tipo_telefone: TipoTelefone
    categoria_contato: CategoriaContato

contatos = []