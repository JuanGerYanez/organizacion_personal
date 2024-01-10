import psycopg2


class Database:
    def __init__(self, user, psw):
        self.user = user
        self.psw = psw
        self.host = 'dpg-cmev8uen7f5s7381hq9g-a.singapore-postgres.render.com'
        self.port = '5432'
        self.database = 'db_organizacion_personal'

    def getConnection(self):
        try:
            conn = psycopg2.connect(
                user=self.user,
                password=self.psw,
                host=self.host,
                port=self.port,
                database=self.database
            )
            conn.autocommit = True
            return conn
        except Exception as e:
            raise Exception(
                "ERROR FATAL: Error al conectar a la base de datos " + str(e))

    def closeConnection(self, conn):
        conn.close()


database = Database("db_organizacion_personal_user", "6Jf406u6tCs7rpknmHQVrB9A1P3FdTdF")
