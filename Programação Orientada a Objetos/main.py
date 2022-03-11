from repositório import Repositorio
from databases import PostgresDB, MySqlDB

db_conn_postgres = PostgresDB()
db_conn_Mysql = MySqlDB()
repo = Repositorio()

repo.insert(db_conn_postgres)
print()
repo.insert(db_conn_Mysql)
