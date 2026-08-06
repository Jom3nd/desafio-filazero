from dataclasses import dataclass, field

@dataclass
class Endereco(slots=True):
    logradouro: str
    bairro: str
    localidade: str
    uf: str
    cep: str

