from src.personagem import Personagem


def test_descansar_recupera_energia():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_energia(-30)

    kael.descansar()

    assert kael.energia == 70

def test_descansar_reduz_cansaco():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_cansaco(30)

    kael.descansar()

    assert kael.cansaco == 20


def test_descansar_nao_passa_energia_de_100():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_energia(10)

    kael.descansar()

    assert kael.energia == 100

def test_descansar_nao_deixa_cansaco_abaixo_de_zero():
    kael = Personagem("Kael", "Bárbaro")

    kael.descansar()

    assert kael.cansaco == 0

def test_cansaco_inicial_esta_dentro_dos_limites():
    kael = Personagem("Kael", "Bárbaro")

    assert 0 <= kael.cansaco <= 100
