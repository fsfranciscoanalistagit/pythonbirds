class Pessoa():
    def __init__(self, nome = None, idade = 0):
        self.nome = nome
        self.idade = idade
        self.altura = 1.85


    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    p = Pessoa('Sales', 35)
    # print(Pessoa.cumprimentar(p))
    # print(id(p))
    # print(p.cumprimentar())
    p.nome = 'Francisco'
    p.altura = 1.85
    print(p.nome, p.idade, p.altura)



