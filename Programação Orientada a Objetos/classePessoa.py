class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def correr(self):
        print('Estou correndo!')

    def __apresentar_documento(self):
        print(self.__cpf)

    def beber(self, bebida):
        if bebida == 'Cerveja':
            self.__apresentar_documento()
        print('Bebendo...')


ronaldo = Pessoa('Ronaldo', 32, '83475kjhfsk')
print(ronaldo.beber('Cerveja'))
