class Descansar:

    def executar(self, personagem):
        personagem.alterar_energia(20)
        personagem.alterar_cansaco(-30)


class Comer:

    def executar(self, personagem):
        personagem.alterar_fome(-30)


class Andar:

    def executar(self, personagem):
        personagem.alterar_energia(-10)
        personagem.alterar_cansaco(10)
        personagem.alterar_fome(5)
