class Alarme:

    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor) -> None:
        if isinstance(valor, bool):
            self.__estado = valor


al = Alarme(False)
relogio = al.get_estado()
print(relogio)
al.set_estado('Olá')
relogio = al.get_estado()
print(relogio)
