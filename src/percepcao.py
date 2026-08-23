class Percepcao:

    def observar(self, personagem, evento):
        intensidade = evento.intensidade

        fator_cansaco = 1 - (personagem.cansaco / 200)
        intensidade *= fator_cansaco

        distancia = getattr(evento, "distancia", 0)

        fator_distancia = 1 / (1 + distancia / 100)
        intensidade *= fator_distancia

        intensidade = max(0, min(100, intensidade))

        return {
            "tipo": evento.tipo,
            "intensidade": intensidade,
            "caracteristica": evento.caracteristica,
            "cansaco": personagem.cansaco,
            "distancia": distancia
        }
