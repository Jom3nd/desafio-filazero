from models.unidade import Unidade
from services.csv_service import read
from services.viacep_service import ViaCepService
from exceptions.api_exception import ApiException
from config.settings import logger
import re
import unicodedata

class ProvisionamentoService:

    def processar(self, caminho_csv: str) -> dict:

        unidades: list[Unidade] = []
        falhas: list[dict[str, str]] = []

        leitor = read(caminho_csv)

        via_cep = ViaCepService()

        logger.info(f"Iniciando o provisionamento de {len(leitor)} unidades")
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
                logger.info(
                    f"{linha['nome']} ({linha['cep']}) processada com sucesso"
                )

            except ApiException as e:

                logger.error(f"{linha['nome']} -> {e}") 

                
                falhas.append({
                    "unidade": linha["nome"],
                    "erro": str(e)
                })

        logger.info(
            f"Fim do provisionamento. "
            f"Sucesso: {len(unidades)} "
            f"Falhas: {len(falhas)}"
        )

        return {
            "unidades": unidades,
            "falhas": falhas
        }

    @staticmethod
    def _gerar_slug(nome: str) -> str:

        slug = nome.lower().strip() #Remove os espaços extras no início e no fim do nome

        slug = unicodedata.normalize("NFD", slug)
        slug = "".join(
            c for c in slug
            if unicodedata.category(c) != "Mn"
        )

        slug = re.sub(r"[^a-z0-9\s-]", "", slug)

        slug = re.sub(r"\s+", "-", slug)

        return slug