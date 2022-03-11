class DataBaseConn:

    def __init__(self) -> None:
        self.__database = 'Postgre'
        self._conn = '//connection_string'
        self.user = 'Lhama'

    def get_database(self) -> None:
        print(self.__database)

    def _testing_connection(self):
        print('Connection OK!')


class Repository(DataBaseConn):

    def __init__(self) -> None:
        super().__init__()
        # print(self.user)
        # print(self.__database)
        # print(self._conn)

    def select(self) -> None:
        self._testing_connection()
        print(f'Connecting to {self._conn}')
        print('SELECT * FROM table')


repo = Repository()
repo.select()
