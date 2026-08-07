import requests
from models.endereco import Endereco

class ViaCepService:


    def buscar_endereco(self, cep: str) -> Endereco:

        viacep_url = f"VIACEP_BASE_URL/{cep}/json/"

        response = requests.get(viacep_url, timeout=5)

        response.raise_for_status()

        data = response.json()

        if data.get("erro"):
            raise ValueError(f"CEP '{cep}' não encontrado.")

        return Endereco(
            logradouro=data["logradouro"],
            bairro=data["bairro"],
            localidade=data["localidade"],
            uf=data["uf"],
            cep=data["cep"]
        )


    