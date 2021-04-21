from unittest import TestCase
from oo.carro import *

motor = Motor()
print('Motor', motor.velocidade)

direcao = Direcao()
print('Direcao', direcao.direcao)

carro = Carro(direcao, motor)
carro.calcular_velocidade()
carro.acelerar()
carro.acelerar()
carro.acelerar()
print('Aceleracao', carro.calcular_velocidade())


class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

