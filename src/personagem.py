class EstadoLimitado:
    def __init__(self, valor, minimo=0, maximo=100):
        self.valor = valor
        self.minimo = minimo
        self.maximo = maximo

    def alterar(self, variacao):
        self.valor = max(
            self.minimo,
            min(self.maximo, self.valor + variacao)
        )


class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe

        self.saude = 100
        self._energia = EstadoLimitado(80)
        self._fome = EstadoLimitado(30)
        self._cansaco = EstadoLimitado(20)

        self.raiva = 10
        self.alegria = 50
        self.tristeza = 10
        self.medo = 20
        self.confianca = 60

    @property
    def energia(self):
        return self._energia.valor

    @property
    def fome(self):
        return self._fome.valor

    @property
    def cansaco(self):
        return self._cansaco.valor

    def alterar_fome(self, variacao):
        self._fome.alterar(variacao)

    def alterar_energia(self, variacao):
        self._energia.alterar(variacao)

    def alterar_cansaco(self, variacao):
        self._cansaco.alterar(variacao)

    def descansar(self):
        self.alterar_energia(20)
        self.alterar_cansaco(-30)
