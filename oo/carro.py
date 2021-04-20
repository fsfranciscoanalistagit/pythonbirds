"""
    N
 O      L
    S

    Exemplo:
    #testando o motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> direcao = Direcao()
    >>> direcao.direcao
    'norte'
    >>> direcao.girar_esquerda()
    >>> direcao.direcao
    'oeste'
    >>> direcao.girar_direita()
    >>> direcao.direcao
    'norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'norte'
    >>> carro.girar_direita()
    >>> carro.calcular_direcao()
    'leste'
    >>> carro.girar_esquerda()
    >>> carro.calcular_direcao()
    'norte'
    >>> carro.girar_esquerda()
    >>> carro.calcular_direcao()
    'oeste'

"""
class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()
    def frear(self):
        self.motor.frear()
    def calcular_direcao(self):
        return self.direcao.direcao
    def girar_direita(self):
        self.direcao.girar_direita()
    def girar_esquerda(self):
        self.direcao.girar_esquerda()







NORTE = 'norte'
SUL = 'sul'
LESTE = 'leste'
OESTE = 'oeste'

class Direcao:
    def __init__(self):
        self.direcao = NORTE

    def girar_esquerda(self):
        rotacao_esquerda_dct = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}
        self.direcao = rotacao_esquerda_dct[self.direcao]

    def girar_direita(self):
        rotacao_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
        self.direcao = rotacao_direita_dct[self.direcao]


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


