from dataclasses import dataclass
from models.endereco import Endereco

@dataclass
class Unidade(slots=True):
    nome: str
    endereco: Endereco
    servicos: list[str]
    slug: str