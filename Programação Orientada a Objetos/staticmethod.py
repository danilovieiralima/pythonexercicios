class MinhaClasse:

    def __init__(self, estado):
        self.estado = estado

    @staticmethod
    def metodo_estatico():
        print('Estou no meu método estático :)')


objeto = MinhaClasse(True)
objeto.metodo_estatico()
MinhaClasse.metodo_estatico()
print()
print()


class Erro:

    @staticmethod
    def error_500():
        print('Internal Server Error')

    @staticmethod
    def error_404():
        print('Not Found')


obj1 = Erro()
obj1.error_500()
