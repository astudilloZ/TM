import sys
import mysql.connector 

class Database:
    def __init__(self, TableName):
        self._cnx = mysql.connector.connect(user='root', password='',host='localhost',database=TableName)
        self._cursor = self._cnx.cursor()

    @property
    def connection(self):
        return self._cnx

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.cursor.close()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

class Database_Table_Usuarios:
    def __init__(self):
        self._cnx = mysql.connector.connect(user='root', password='',host='localhost',database='fly3d')
        self._cursor = self._cnx.cursor()

    @property
    def connection(self):
        return self._cnx

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.cursor.close()
        self.connection.close()

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def ObtenerUsuarios(self):
        self.cursor.execute("SELECT NOMBRE FROM usuarios")
        usuarios = self.cursor.fetchall()
        return usuarios 

    def CompararContrasena(self, Email, contrasena):
        self.cursor.execute("SELECT EMAIL, CONTRASENA FROM usuarios")
        rows = self.cursor.fetchall()
        self.coincide = False
        for row in rows:
            if row[0].lower() == Email.lower():
                if row[1] == contrasena:
                    self.coincide = True
        return self.coincide

    def IngresarUsuario(self, NombreUsuario, Contrasena, Direccion, email):
        self.cursor.execute(("INSERT INTO usuarios(NOMBRE, CONTRASENA, EMAIL, DIRECCION) VALUES (%s, %s, %s, %s)"), (NombreUsuario, Contrasena, Direccion, email))
        self.commit()

    def ElUsuarioExiste(self, Email):
        self.cursor.execute("SELECT EMAIL FROM usuarios")
        usuarios = self.cursor.fetchall()
        self.existe = False
        for row in usuarios:
            if row[0].lower() == Email.lower():
                self.existe = True
        return self.existe

    def ObtenerNombreUsuario(self, Email):
        self.cursor.execute("SELECT EMAIL, NOMBRE FROM usuarios")
        usuarios = self.cursor.fetchall()
        self.nombre = ""
        for row in usuarios:
            if row[0].lower() == Email.lower():
                self.nombre = row[1]
        return self.nombre
    
#class CalibracionTable:
#    def __init__(self):
#    def ObtenerCalibracion(self):
#
#    def ModificarCalibracion(self):

#class RutaTable:
#    def __init__(self):
#    def ObtenerRuta(self):
#
#    def IngresarRuta(self):

#class ModelosTable:

#def main():


    #bd = Database_Table_Usuarios()
    #print(bd.ObtenerUsuario('JUAN@gmail.com'))
    #usuarios = bd.ObtenerUsuarios()
    #for row in usuarios:
        #print(row[0].lower()) 
    #    print(row[0])

    #print(bd.ElUsuarioExiste('JUAN@gmail.com'))

    #print(bd.CompararContrasena('JUAN@gmail.com', '1234'))

    #bd.IngresarUsuario('Pepito', '2658', 'pepito@gmail.com')

    #bd.close()
#main()

