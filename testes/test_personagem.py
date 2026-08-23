import pytest
from src.personagem import Personagem
from src.mundo import Mundo
from src.evento import Evento
from src.percepcao import Percepcao


def test_kael_comeca_com_estado_inicial():
    kael = Personagem("Kael", "Bárbaro")

    assert kael.saude == 100
    assert kael.energia == 80
    assert kael.fome == 30
    assert kael.cansaco == 20
    assert kael.medo == 20
    assert kael.confianca == 60


#def test_fome_deve_respeitar_limites():
   # kael = Personagem("Kael", "Bárbaro")

   # kael.fome = 150

   # assert kael.fome <= 100

def test_fome_pode_ser_alterada_com_limites():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_fome(20)

    assert kael.fome == 50

def test_fome_nao_passa_de_100():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_fome(100)

    assert kael.fome == 100

def test_fome_nao_fica_abaixo_de_zero():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_fome(-100)

    assert kael.fome == 0
def test_energia_pode_ser_alterada():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_energia(-20)

    assert kael.energia == 60


def test_energia_nao_passa_de_100():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_energia(100)

    assert kael.energia == 100


def test_energia_nao_fica_abaixo_de_zero():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_energia(-100)

    assert kael.energia == 0

def test_alterar_fome_rejeita_valor_invalido():
    kael = Personagem("Kael", "Bárbaro")

    with pytest.raises(TypeError):
        kael.alterar_fome("muito")


def test_cansaco_pode_ser_alterado_com_limites():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_cansaco(20)

    assert kael.cansaco == 40


def test_cansaco_nao_passa_de_100():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_cansaco(100)

    assert kael.cansaco == 100


def test_cansaco_nao_fica_abaixo_de_zero():
    kael = Personagem("Kael", "Bárbaro")

    kael.alterar_cansaco(-100)

    assert kael.cansaco == 0


def test_personagem_pode_perceber_evento_do_mundo():
    mundo = Mundo()
    kael = Personagem("Kael", "Bárbaro")

    evento = Evento("som")

    percepcao = Percepcao()

    resultado = percepcao.observar(kael, evento)

    assert resultado["tipo"] == "som"

def test_percepcao_identifica_intensidade_do_evento():
    kael = Personagem("Kael", "Bárbaro")

    evento = Evento("som", intensidade=80)

    percepcao = Percepcao()

    resultado = percepcao.observar(kael, evento)

    assert resultado["tipo"] == "som"
    assert resultado["intensidade"] == 72


def test_percepcao_identifica_luz():
    kael = Personagem("Kael", "Bárbaro")

    evento = Evento("luz", intensidade=50)

    percepcao = Percepcao()

    resultado = percepcao.observar(kael, evento)

    assert resultado["tipo"] == "luz"
    assert resultado["intensidade"] == 45


def test_percepcao_identifica_movimento():
    kael = Personagem("Kael", "Bárbaro")

    evento = Evento("movimento", intensidade=90)

    percepcao = Percepcao()

    resultado = percepcao.observar(kael, evento)

    assert resultado["tipo"] == "movimento"
    assert resultado["intensidade"] == 81


def test_percepcao_identifica_cheiro():
    kael = Personagem("Kael", "Bárbaro")

    evento = Evento("cheiro", intensidade=70)

    percepcao = Percepcao()

    resultado = percepcao.observar(kael, evento)

    assert resultado["tipo"] == "cheiro"
    assert resultado["intensidade"] == 63


def test_percepcao_nao_carrega_dados_do_evento_anterior():
    kael = Personagem("Kael", "Bárbaro")
    percepcao = Percepcao()

    evento_som = Evento("som", intensidade=80)
    resultado_som = percepcao.observar(kael, evento_som)

    evento_cheiro = Evento("cheiro", intensidade=30)
    resultado_cheiro = percepcao.observar(kael, evento_cheiro)

    assert resultado_som["tipo"] == "som"
    assert resultado_som["intensidade"] == 72

    assert resultado_cheiro["tipo"] == "cheiro"
    assert resultado_cheiro["intensidade"] == 27

def test_percepcao_nao_altera_intensidade_do_evento():
    kael = Personagem("Kael", "Bárbaro")

    evento = Evento(
        "som",
        intensidade=80,
        caracteristica="batida"
    )

    percepcao = Percepcao()

    percepcao.observar(kael, evento)

    assert evento.intensidade == 80

def test_percepcao_preserva_caracteristica_do_evento():
    kael = Personagem("Kael", "Bárbaro")

    evento = Evento(
        "cheiro",
        intensidade=70,
        caracteristica="fumaça"
    )

    percepcao = Percepcao()

    resultado = percepcao.observar(kael, evento)

    assert resultado["tipo"] == "cheiro"
    assert resultado["intensidade"] == 63
    assert resultado["caracteristica"] == "fumaça"


def test_personagens_com_cansaco_diferente_podem_perceber_diferente():
    evento = Evento(
        "som",
        intensidade=80,
        caracteristica="batida"
    )

    descansado = Personagem("Kael", "Bárbaro")
    cansado = Personagem("Kael", "Bárbaro")

    descansado.alterar_cansaco(-20)
    cansado.alterar_cansaco(80)

    percepcao = Percepcao()

    resultado_descansado = percepcao.observar(descansado, evento)
    resultado_cansado = percepcao.observar(cansado, evento)

    assert resultado_descansado["cansaco"] == 0
    assert resultado_cansado["cansaco"] == 100


def test_cansaco_pode_reduzir_intensidade_percebida():
    evento = Evento(
        "som",
        intensidade=80,
        caracteristica="batida"
    )

    descansado = Personagem("Kael", "Bárbaro")
    cansado = Personagem("Kael", "Bárbaro")

    descansado.alterar_cansaco(-20)
    cansado.alterar_cansaco(80)

    percepcao = Percepcao()

    resultado_descansado = percepcao.observar(descansado, evento)
    resultado_cansado = percepcao.observar(cansado, evento)

    assert resultado_descansado["intensidade"] > resultado_cansado["intensidade"]


def test_cansaco_zero_nao_reduz_percepcao():
    personagem = Personagem("Kael", "Bárbaro")
    personagem.alterar_cansaco(-20)

    evento = Evento(
        "som",
        intensidade=80,
        caracteristica="batida"
    )

    percepcao = Percepcao()
    resultado = percepcao.observar(personagem, evento)

    assert personagem.cansaco == 0
    assert resultado["intensidade"] == 80


def test_cansaco_alto_reduz_percepcao():
    personagem = Personagem("Kael", "Bárbaro")
    personagem.alterar_cansaco(80)

    evento = Evento(
        "som",
        intensidade=80,
        caracteristica="batida"
    )

    percepcao = Percepcao()
    resultado = percepcao.observar(personagem, evento)

    assert personagem.cansaco == 100
    assert resultado["intensidade"] < 80


def test_evento_sem_intensidade_continua_sem_intensidade():
    personagem = Personagem("Kael", "Bárbaro")

    evento = Evento(
        "som",
        intensidade=0,
        caracteristica="batida"
    )

    percepcao = Percepcao()
    resultado = percepcao.observar(personagem, evento)

    assert resultado["intensidade"] == 0


def test_percepcao_responde_gradualmente_ao_cansaco():
    evento = Evento("som", intensidade=100, caracteristica="batida")

    descansado = Personagem("Kael", "Bárbaro")
    medio = Personagem("Kael", "Bárbaro")
    cansado = Personagem("Kael", "Bárbaro")

    medio.alterar_cansaco(50)
    cansado.alterar_cansaco(80)

    percepcao = Percepcao()

    r0 = percepcao.observar(descansado, evento)
    r50 = percepcao.observar(medio, evento)
    r80 = percepcao.observar(cansado, evento)

    assert r0["intensidade"] > r50["intensidade"]
    assert r50["intensidade"] > r80["intensidade"]

def test_percepcao_mapeia_cansaco():
    evento = Evento("som", intensidade=100)

    percepcao = Percepcao()

    for cansaco in (0, 20, 40, 60, 80, 100):
        personagem = Personagem("Kael", "Bárbaro")
        personagem.alterar_cansaco(cansaco - personagem.cansaco)

        resultado = percepcao.observar(personagem, evento)

        print(
            f"cansaco={cansaco:3} "
            f"intensidade={resultado['intensidade']}"
        )

def test_percepcao_respeita_limites_da_intensidade():
    personagem = Personagem("Kael", "Bárbaro")
    percepcao = Percepcao()

    for cansaco in (0, 20, 50, 80, 100):
        personagem.alterar_cansaco(cansaco - personagem.cansaco)

        for intensidade in (0, 25, 50, 100):
            evento = Evento("som", intensidade=intensidade)

            resultado = percepcao.observar(personagem, evento)

            assert 0 <= resultado["intensidade"] <= intensidade

def test_percepcao_considera_distancia_do_evento():
    personagem = Personagem("Kael", "Bárbaro")

    evento_perto = Evento(
        "som",
        intensidade=100,
        caracteristica="batida",
        distancia=10
    )

    evento_longe = Evento(
        "som",
        intensidade=100,
        caracteristica="batida",
        distancia=100
    )

    percepcao = Percepcao()

    resultado_perto = percepcao.observar(personagem, evento_perto)
    resultado_longe = percepcao.observar(personagem, evento_longe)

    assert resultado_perto["intensidade"] > resultado_longe["intensidade"]


def test_percepcao_distancia_zero_nao_reduz_intensidade():
    personagem = Personagem("Kael", "Bárbaro")
    personagem.alterar_cansaco(-20)

    evento = Evento(
        "som",
        intensidade=100,
        caracteristica="batida",
        distancia=0
    )

    percepcao = Percepcao()
    resultado = percepcao.observar(personagem, evento)

    assert resultado["intensidade"] == 100

def test_percepcao_distancia_maior_reduz_intensidade():
    personagem = Personagem("Kael", "Bárbaro")
    personagem.alterar_cansaco(-20)

    evento_perto = Evento(
        "som",
        intensidade=100,
        caracteristica="batida",
        distancia=10
    )

    evento_longe = Evento(
        "som",
        intensidade=100,
        caracteristica="batida",
        distancia=100
    )

    percepcao = Percepcao()

    resultado_perto = percepcao.observar(personagem, evento_perto)
    resultado_longe = percepcao.observar(personagem, evento_longe)

    assert resultado_perto["intensidade"] > resultado_longe["intensidade"]


