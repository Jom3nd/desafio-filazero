from dataclasses import dataclass

@dataclass
class Unidade(slots=True):
    nome: str
    endereco: str
    servicos: list[str]
    slug: str