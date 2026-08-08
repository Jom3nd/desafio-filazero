from src.services.viacep_service import ViaCepService

def test_viacep_service():
    via_cep = ViaCepService()
    endereco = via_cep.buscar_endereco("49010-390")

