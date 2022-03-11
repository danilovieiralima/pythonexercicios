class MySqlDB():

    def __init__(self) -> None:
        self.__conexao = 'MySqlDB'

    def conectar(self) -> str:
        print('Conectando ao Banco MySqlDB...')
        return self.__conexao

    def desconectar(self) -> str:
        print('Desconectando ao Banco MySqlDB...')
        return self.__conexao


banco = MySqlDB()
banco.conectar()
banco.desconectar()
