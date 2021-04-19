class Pessoa():
    olhos = 2
    def __init__(self, *filhos, nome = None, idade = 0):
        self.nome = nome
        self.idade = idade
        self.altura = 1.85
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_atributo_classe(cls):
        return f'{cls} olhos {cls.olhos}'
if __name__ == '__main__':
    Filhos = Pessoa(nome = 'Daniel', idade= 5)
    # print(Pessoa.cumprimentar(p))
    # print(id(p))
    print(Filhos.cumprimentar())
    Fco = Pessoa(Filhos, idade= 35)
    Fco.nome = 'Francisco'
    Fco.altura = 1.85
    Fco.sobrenome = 'Araujo'
    print(Fco.__dict__)
    print(Fco.nome, Fco.sobrenome, Fco.altura, Fco.idade)

    for filho in Fco.filhos:
        print(filho.nome, filho.idade)
    del Fco.filhos
    print(Fco.__dict__)
    Fco.olhos = 4
    #del Fco.olhos
    #Pessoa.olhos = 3
    print(Filhos.olhos, "-",  id(Filhos.olhos), Fco.olhos, "-", id(Fco.olhos), Pessoa.olhos,
          "-", id(Pessoa.olhos))
    print(Pessoa.metodo_estatico(), Fco.metodo_estatico())
    print(Pessoa.nome_atributo_classe())




