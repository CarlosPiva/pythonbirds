class Pessoa:
    #atributo de classe/instancia
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá {id(self)}"

    @staticmethod
    def metodo_estatico():
        return 33
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'
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
    piva.olhos = 3
    del piva.olhos
    #atributos de instâncias ficam presentes no __dict__
    print(carlos.__dict__)
    print(piva.__dict__)
    Pessoa.olhos = 1
    print(Pessoa.olhos)
    print(carlos.olhos)
    print(piva.olhos)
    print(id(Pessoa.olhos), id(carlos.olhos), id(piva.olhos))
    #utilizando o metodo static
    print(Pessoa.metodo_estatico(), carlos.metodo_estatico())
    #print de exemplo pela classe             ou indiretamente pelo objeto
    print(Pessoa.nome_e_atributos_de_classe(), carlos.nome_e_atributos_de_classe())
