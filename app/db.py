import psycopg2


class Database:
    def __init__(self, user, psw):
        self.user = user
        self.psw = psw
        self.host = 'dpg-cms607ed3nmc73epb3d0-a.oregon-postgres.render.com'
        self.port = '5432'
        self.database = 'organizacion_personal_db'

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


database = Database("organizacion_personal_db_user", "SQBBtQFFkrH3yTrqPqTPn1OTcIXFaMX3")
