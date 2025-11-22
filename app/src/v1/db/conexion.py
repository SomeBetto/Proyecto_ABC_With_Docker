import psycopg2

class conexion():
    
    conn=None

    def conectar(self):
        try:
            self.conn = psycopg2.connect(
                host='dev-postgres',
                database='postgres',
                user='postgres',
                password='passw0rd'
            )
            self.conn.autocommit = True
            self.cur = self.conn.cursor()
            print("Conexión exitosa a la base de datos")
        except (Exception, psycopg2.Error) as error:
            print("Error al conectar a la base de datos:", error)

    def ejecutarquery(self,query:str):
        try:
            self.cur.execute(query)
            rows = self.cur.fetchall()
            return rows
        except (Exception, psycopg2.Error) as error:
            print("Error al ejecutar la consulta:", error)

    def cerrar(self):
        try:
            self.cur.close()
            self.conn.close()
            print("Conexión cerrada")
        except (Exception, psycopg2.Error) as error:
            print("Error al cerrar la conexión:", error)