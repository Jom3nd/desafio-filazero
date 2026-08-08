from src.services.viacep_service import ViaCepService

def test_viacep_service():
    via_cep = ViaCepService()
    endereco = via_cep.buscar_endereco("49010-390")
    assert endereco.cidade == "Aracaju"
    assert endereco.uf == "SE"
    assert endereco.cep == "49010-390"
    assert endereco.logradouro
    assert endereco.bairro

