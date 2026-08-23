from src.personagem import Personagem


def test_descansar_altera_estado_do_personagem():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_energia(-30)
    kael.alterar_cansaco(30)

    kael.descansar()

    assert kael.energia == 70
    assert kael.cansaco == 20
