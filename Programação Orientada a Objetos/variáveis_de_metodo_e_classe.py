class MinhaClasse:
    estatico = 'lhama'

    def __init__(self, estado):
        self.estado = estado

    def print_estatico(self):
        print(self.estatico)

    @classmethod
    def mudar_estatico(cls):
        cls.estatico = 'Programador'
        print(cls.estatico)


objeto1 = MinhaClasse(True)
objeto2 = MinhaClasse(False)
objeto1.mudar_estatico()
objeto2.print_estatico()

print(MinhaClasse.estatico)
