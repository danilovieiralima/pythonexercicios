from abs_class import AbstractClass


class Filha(AbstractClass):

    def apresentar_metodo(self) -> None:
        print(self.atributo)


filha = Filha()
filha.apresentar_metodo()
filha.metodo('Estou aqui')


abstractClass = AbstractClass()
abstractClass.metodo('Fazendo algo')
