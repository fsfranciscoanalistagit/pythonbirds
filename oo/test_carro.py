from oo.carro import *

motor = Motor()
motor.acelerar()
print(motor.acelerar())

direcao = Direcao()
direcao.girar_esquerda()
print(direcao.girar_esquerda())

carro = Carro(direcao, motor)
print(carro.acelerar(), carro.girar_esquerda())
