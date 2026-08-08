from src.services.provisionamento_service import ProvisionamentoService

def test_processar():
    ps = ProvisionamentoService()
    resultado = ps.processar("data/unidades.csv")