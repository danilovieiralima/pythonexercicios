from typing import Type


class Interruptor:

    def __init__(self, comodo):
        self.__comodo = comodo

    def acender(self):
        print(f'Acendendo {self.__comodo}')

    def apagar(self):
        print(f'Apagando {self.__comodo}')


class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    def dormir(self):
        print('Fui dormir...')


lhama = Pessoa()
interruptor_quarto = Interruptor('Quarto')
interruptor_cozinha = Interruptor('Cozinha')

interruptor_quarto.acender()
lhama.acender_luz(interruptor_cozinha)
lhama.apagar_luz(interruptor_quarto)
lhama.dormir()
