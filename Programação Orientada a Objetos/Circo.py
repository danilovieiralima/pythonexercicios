'''class Circo:

    def apresentar(self, tipo):  # FECHADO
        if tipo == 1:
            self.apresentar_malabarista()
        if tipo == 2:
            self.apresentar_palhaco()

    def apresentar_malabarista(self):
        print('Malabarista apresentando seu show')

    def apresentar_palhaco(self):
        print('Palhaço apresentando seu show')


circo = Circo()
circo.apresentar(2)'''


class Circo:
    def apresentar(self, apresentador: any):        # ABERTO
        apresentador.apresentar_show()


class Malabarista:
    def apresentar_show(self):
        print('Malabarista apresentando seu show')


class Palhaco:
    def apresentar_show(self):
        print('Palhaço apresentando seu show')


class Domador:
    def apresentar_show(self):
        print('Domador apresentando seu show')


circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()
domador = Domador()

circo.apresentar(malabarista)
circo.apresentar(palhaco)
circo.apresentar(domador)
