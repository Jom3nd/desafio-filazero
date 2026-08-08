from src.services.provisionamento_service import ProvisionamentoService

def test_slug():
    ps = ProvisionamentoService()
    slug = ps._gerar_slug("Unidade de Saúde São josé")
    assert slug == "unidade-de-saude-sao-jose"