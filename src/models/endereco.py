from dataclasses import dataclass, field

@dataclass(slots=True)
class Endereco:
    logradouro: str
    bairro: str
    localidade: str
    uf: str
    cep: str

