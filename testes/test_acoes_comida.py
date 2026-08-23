from src.personagem import Personagem
from src.acoes import Comer


def test_acao_comer_reduz_fome():
    kael = Personagem("Kael", "Bárbaro")

    acao = Comer()
    acao.executar(kael)

    assert kael.fome == 0

def test_comer_nao_deixa_fome_abaixo_de_zero():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_fome(-25)

    acao = Comer()
    acao.executar(kael)

    assert kael.fome == 0

def test_comer_rejeita_alvo_invalido():
    acao = Comer()

    try:
        acao.executar(None)
    except (AttributeError, TypeError):
        pass
    else:
        assert False
