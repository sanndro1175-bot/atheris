from src.personagem import Personagem
from src.acoes import Descansar


def test_acao_descansar_externa_altera_estado():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_energia(-30)
    kael.alterar_cansaco(30)

    acao = Descansar()
    acao.executar(kael)

    assert kael.energia == 70
    assert kael.cansaco == 20

def test_acao_descansar_externa_respeita_limites():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_energia(20)
    kael.alterar_cansaco(-20)

    acao = Descansar()
    acao.executar(kael)

    assert kael.energia == 100
    assert kael.cansaco == 0
