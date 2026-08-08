from dataclasses import dataclass
from src.models.endereco import Endereco

@dataclass(slots=True)
class Unidade:
    nome: str
    endereco: Endereco
    servicos: list[str]
    slug: str