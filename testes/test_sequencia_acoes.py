from src.personagem import Personagem
from src.acoes import Andar, Comer, Descansar


def test_sequencia_andar_comer_descansar():
    kael = Personagem("Kael", "Bárbaro")

    andar = Andar()
    comer = Comer()
    descansar = Descansar()

    andar.executar(kael)
    comer.executar(kael)
    descansar.executar(kael)

    assert kael.energia == 90
    assert kael.fome == 5
    assert kael.cansaco == 0
