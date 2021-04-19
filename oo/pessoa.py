class Pessoa():
    def __init__(self, *filhos, nome = None, idade = 0):
        self.nome = nome
        self.idade = idade
        self.altura = 1.85
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    Filhos = Pessoa(nome = 'Daniel', idade= 5)
    # print(Pessoa.cumprimentar(p))
    # print(id(p))
    # print(p.cumprimentar())
    Fco = Pessoa(Filhos)
    Fco.nome = 'Francisco'
    Fco.altura = 1.85
    print(Fco.nome, Fco.altura)
    for filho in Fco.filhos:
        print(filho.nome, filho.idade)



