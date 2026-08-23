from src.personagem import Personagem
from src.acoes import Andar, Comer, Descansar


def test_sequencia_longa_mantem_estados_validos():
    kael = Personagem("Kael", "Bárbaro")

    andar = Andar()
    comer = Comer()
    descansar = Descansar()

    for _ in range(20):
        andar.executar(kael)

    for _ in range(20):
        comer.executar(kael)

    for _ in range(20):
        descansar.executar(kael)

    assert 0 <= kael.energia <= 100
    assert 0 <= kael.fome <= 100
    assert 0 <= kael.cansaco <= 100


def test_acoes_repetidas_nao_criam_estado_invalido():
    kael = Personagem("Kael", "Bárbaro")

    andar = Andar()
    comer = Comer()
    descansar = Descansar()

    for _ in range(50):
        andar.executar(kael)
        comer.executar(kael)
        descansar.executar(kael)

    assert 0 <= kael.energia <= 100
    assert 0 <= kael.fome <= 100
    assert 0 <= kael.cansaco <= 100
