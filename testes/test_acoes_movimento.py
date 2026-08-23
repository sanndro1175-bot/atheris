from src.personagem import Personagem
from src.acoes import Andar


def test_andar_altera_estado_do_personagem():
    kael = Personagem("Kael", "Bárbaro")

    acao = Andar()
    acao.executar(kael)

    assert kael.energia == 70
    assert kael.cansaco == 30
    assert kael.fome == 35


def test_andar_nao_deixa_energia_abaixo_de_zero():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_energia(-80)

    acao = Andar()
    acao.executar(kael)

    assert kael.energia == 0


def test_andar_nao_deixa_fome_acima_de_cem():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_fome(70)

    acao = Andar()
    acao.executar(kael)

    assert kael.fome == 100

def test_andar_repetidamente_respeita_limites():
    kael = Personagem("Kael", "Bárbaro")

    acao = Andar()

    for _ in range(20):
        acao.executar(kael)

    assert kael.energia == 0
    assert kael.cansaco == 100
    assert kael.fome == 100
