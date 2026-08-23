import pytest

from src.personagem import EstadoLimitado


def test_estado_limitado_comeca_com_valor():
    estado = EstadoLimitado(30)

    assert estado.valor == 30


def test_estado_limitado_aumenta():
    estado = EstadoLimitado(30)

    estado.alterar(20)

    assert estado.valor == 50


def test_estado_limitado_respeita_maximo():
    estado = EstadoLimitado(90)

    estado.alterar(20)

    assert estado.valor == 100


def test_estado_limitado_respeita_minimo():
    estado = EstadoLimitado(10)

    estado.alterar(-20)

    assert estado.valor == 0


def test_estado_limitado_rejeita_tipo_invalido():
    estado = EstadoLimitado(30)

    with pytest.raises(TypeError):
        estado.alterar("muito")
