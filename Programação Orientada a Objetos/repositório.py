class Repositorio:

    def select(self, db_connection: any) -> None:
        conection = db_connection.conectar()
        print(f'Conectei ao Banco {conection}')
        print('Fazendo um SELECT * FROM...')
        db_connection.desconectar()

    def insert(self, db_connection: any) -> None:
        conection = db_connection.conectar()
        print(f'Conectei ao Banco {conection}')
        print('Fazendo um Insert Values...')
        db_connection.desconectar()
    