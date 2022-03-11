from typing import Type


class Conexao:

    def conectar(self):
        print('Conectando ao Banco de Dados')

    def desconectar(self):
        print('Desconectando ao Banco de Dados')


class MySQLRepo(Conexao):
    def __init__(self):
        super().__init__()

    def select(self):
        self.conectar()
        print('SELECT * FROM table')


def CasodeUso():
    def buscar(self, db_repo: Type[MySQLRepo]):
        db_repo.select()
