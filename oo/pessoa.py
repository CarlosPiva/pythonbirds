class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá {id(self)}"


if __name__ == '__main__':
    piva = Pessoa(nome='Piva')
    carlos = Pessoa(piva, nome='Carlos')
    print(Pessoa.cumprimentar(carlos))
    print(id(carlos))
    print(carlos.cumprimentar())
    print(carlos.nome)
    print(carlos.idade)
    for filho in carlos.filhos:
         print(filho.nome)
    #atributo dinâmico (fazendo a atribuição aqui msm)
    carlos.sobrenome = 'Roberto'
    print(carlos.sobrenome)
    del carlos.filhos
    #atributos de instâncias ficam presentes no __dict__
    print(carlos.__dict__)
    print(piva.__dict__)