from dataclasses import dataclass, field

@dataclass(slots=True)
class Endereco:
    logradouro: str
    bairro: str
    cidade: str
    uf: str
    cep: str

