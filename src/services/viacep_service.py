import requests
from src.models.endereco import Endereco
from src.exceptions.api_exception import ApiException
from src.config.settings import VIACEP_BASE_URL

class ViaCepService:


    def buscar_endereco(self, cep: str) -> Endereco:

        viacep_url = f"{VIACEP_BASE_URL}/{cep}/json/"

        try:
            response = requests.get(viacep_url, timeout=5)

            response.raise_for_status()

            data = response.json()

        except (requests.RequestException, ValueError) as e:
            raise ApiException(f"Erro ao consultar o ViaCEP: {e}")

        if data.get("erro"):
            raise ApiException(f"CEP '{cep}' não encontrado.")

        return Endereco(    
            logradouro=data["logradouro"],
            bairro=data["bairro"],
            cidade=data["localidade"],
            uf=data["uf"],
            cep=data["cep"]
        )
            


    