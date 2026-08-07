from models.unidade import Unidade
from services.csv_service import read
from services.viacep_service import ViaCepService
from exceptions.api_exception import ApiException
import requests
import re
import unicodedata

class ProvisionamentoService:

    def processar(self, caminho_csv: str) -> list[Unidade]:

        unidades = []
         
        falhas = []

        leitor = read(caminho_csv)

        via_cep = ViaCepService()

        for linha in leitor:

            try:

                endereco = via_cep.buscar_endereco(linha["cep"])

                servicos = linha["servicos"].split(";")

                slug = self._gerar_slug(linha["nome"])

                unidade = Unidade(
                    nome=linha["nome"],
                    endereco=endereco,
                    servicos=servicos,
                    slug=slug
                )
                
                unidades.append(unidade)

            except (ApiException, requests.RequestException) as e:
                falhas.append({
                    "unidade": linha["nome"],
                    "erro": str(e)
                })

        return {
            "unidades": unidades,
            "falhas": falhas
        }

    @staticmethod
    def _gerar_slug(nome: str) -> str:

        slug = nome.lower()

        slug = unicodedata.normalize("NFD", slug)
        slug = "".join(
            c for c in slug
            if unicodedata.category(c) != "Mn"
        )

        slug = re.sub(r"[^a-z0-9\s-]", "", slug)

        slug = re.sub(r"\s+", "-", slug)

        return slug