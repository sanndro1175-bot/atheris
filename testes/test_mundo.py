from src.mundo import Mundo
from src.personagem import Personagem


def test_mundo_existe():
    mundo = Mundo()

    assert mundo is not None


def test_mundo_comeca_com_estado():
    mundo = Mundo()

    assert mundo.estado == "normal"


def test_mundo_e_personagem_possuem_estados_independentes():
    mundo = Mundo()
    kael = Personagem("Kael", "Bárbaro")

    fome_inicial = kael.fome

    mundo.estado = "perigoso"

    assert mundo.estado == "perigoso"
    assert kael.fome == fome_inicial
