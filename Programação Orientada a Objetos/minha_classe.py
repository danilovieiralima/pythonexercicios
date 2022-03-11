class MinhaClasse:

    def __init__(self, atributo):
        self.meu_atributo = 'Olá, Mundo!'
        self.meu_atributo2 = atributo

    def meu_metodo(self):
        print(self.meu_atributo)
        print(self.meu_atributo2)

    def meu_metodo2(self, numero, multiplicador):
        return numero * multiplicador


object = MinhaClasse('Meu nome é Danilo')
print(object.meu_metodo())
