"""
Realizó: Juan Sebastian Astudillo
TG: Fly3d
25-oct-2020
"""

"""
Pasos git:
1. git add.
2. git commit -m "nota"   (git commit -am “msj”)
3. git pull origin master
4. git push origin master
"""

import sys
import mysql.connector 

"""Conexión a tabla Mision - Nuevo commit

Funciones:

1. ObtenerDeptos():
2. IngresarDepto(nombre, descripcion): Permite ingresar datos de municipios
3. ExisteDepto(nombre):
4. BorrarDepto(nombre)

"""
class Database_Mision:
    def __init__(self):
        self._cnx = mysql.connector.connect(user='root', password='',host='localhost',database='tm-fly3d')
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
        self.cursor.execute("SELECT EmailUsuario FROM mision")
        usuarios = self.cursor.fetchall()
        return usuarios  

    def ElUsuarioExiste(self, Email):
        self.cursor.execute("SELECT EmailUsuario FROM mision")
        usuarios = self.cursor.fetchall()
        self.existe = False
        for row in usuarios:
            if row[0].lower() == Email.lower():
                self.existe = True
        return self.existe   

    def ObtenerNombreUsuario(self, Email):
        self.cursor.execute("SELECT EmailUsuarios, NombreUsuario FROM mision")
        usuarios = self.cursor.fetchall()
        self.nombre = ""
        for row in usuarios:
            if row[0].lower() == Email.lower():
                self.nombre = row[1]
        return self.nombre

    #Se debe ifentificar municipio / Ingresar calibración y párametros base 
    def IngresarUsuario(self, NombreUsuario, Contrasena, Direccion, email):
        self.cursor.execute(("INSERT INTO mision(Lugar, NombreUsuario, ApellidosUsuario, EmailUsuario, ClaveUsuario, Fecha, HoraInicio, HoraFin) VALUES (%s, %s, %s, %s)"), (NombreUsuario, Contrasena, Direccion, email))
        self.commit()

"""Conexión a tabla Depto

Funciones:

1. ObtenerDeptos():
2. IngresarDepto(nombre, descripcion): Permite ingresar datos de municipios
3. ExisteDepto(nombre):
4. BorrarDepto(nombre)

"""

class Database_Depto:
    def __init__(self):
        self._cnx = mysql.connector.connect(user='root', password='',host='localhost',database='tm-fly3d')
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

    def ObtenerDeptos(self):
        self.cursor.execute("SELECT nombre FROM Depto")
        usuarios = self.cursor.fetchall()
        return usuarios 
    
    def IngresarDepto(self, nombre, descripcion):
        self.cursor.execute(("INSERT INTO Depto(nombre, descripcion) VALUES (%s, %s)"), (nombre, descripcion))
        self.commit()

    def ExisteDepto(self, nombre):
        self.cursor.execute("SELECT nombre FROM Depto")
        deptos = self.cursor.fetchall()
        self.existe = False
        for row in deptos:
            if row[0].lower() == nombre.lower():
                self.existe = True
        return self.existe   

    def BorrarDepto(self, nombre):
        self.cursor.execute("DELETE FROM Depto WHERE nombre = %s", nombre)    
        self.commit()
        return self.cursor.rowcount


"""Conexión a tabla Municipio

Funciones:

1. ObtenerDeptos():
2. IngresarDepto(nombre, descripcion): Permite ingresar datos de municipios
3. ExisteDepto(nombre):
4. BorrarDepto(nombre)

"""

class Database_Municipio:
    def __init__(self):
        self._cnx = mysql.connector.connect(user='root', password='',host='localhost',database='tm-fly3d')
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

    def ObtenerMunicipios(self):
        self.cursor.execute("SELECT nombre FROM municipio")
        usuarios = self.cursor.fetchall()
        return usuarios 
    
    def IngresarMunicipio(self, deptoId, nombre, descripcion):
        self.cursor.execute(("INSERT INTO municipio(Depto_id, nombre, descripcion) VALUES (%s, %s, %s)"), (deptoId, nombre, descripcion,))
        self.commit()

    def ExisteMunicipio(self, nombre):
        self.cursor.execute("SELECT nombre FROM Municipio")
        deptos = self.cursor.fetchall()
        self.existe = False
        for row in deptos:
            if row[0].lower() == nombre.lower():
                self.existe = True
        return self.existe   

    def BorrarMunicipio(self, nombre):
        self.cursor.execute("DELETE FROM Municipio WHERE nombre = %s", nombre)    
        self.commit()
        return self.cursor.rowcount

    def ObtenerDepto(self, nombre):
        self.cursor.execute("SELECT municipio.nombre, depto.nombre FROM municipio INNER JOIN depto ON municipio.Depto_id = depto.id WHERE municipio.nombre = %s", (nombre.lower(),))
        return self.cursor.fetchall()

"""Conexión a tabla Laser

Funciones:

1. ObtenerDeptos():
2. IngresarDepto(nombre, descripcion): Permite ingresar datos de municipios
3. ExisteDepto(nombre):
4. BorrarDepto(nombre)

"""

class Database_LaserData:
    def __init__(self):
        self._cnx = mysql.connector.connect(user='root', password='',host='localhost',database='tm-fly3d')
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

"""Conexión a tabla Telemetria

Funciones:

1. ObtenerDeptos():
2. IngresarDepto(nombre, descripcion): Permite ingresar datos de municipios
3. ExisteDepto(nombre):
4. BorrarDepto(nombre)

"""

class Database_Telemetria:
    def __init__(self):
        self._cnx = mysql.connector.connect(user='root', password='',host='localhost',database='tm-fly3d')
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

"""Conexión a tabla Waypoints

Funciones:

1. ObtenerDeptos():
2. IngresarDepto(nombre, descripcion): Permite ingresar datos de municipios
3. ExisteDepto(nombre):
4. BorrarDepto(nombre)

"""

class Database_Waypoints:
    def __init__(self):
        self._cnx = mysql.connector.connect(user='root', password='',host='localhost',database='tm-fly3d')
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


def main():
    bd = Database_Municipio()
    #idDepto = bd.ObtenerIdDepto('Medellin')

    print(bd.ObtenerDepto('Palmira'))

    bd.close()


main()
