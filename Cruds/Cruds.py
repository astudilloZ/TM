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

"""Conexión a tabla Mision 

Funciones:

1. ...

"""
class Database_Mision:
    def __init__(self):
        self._cnx = mysql.connector.connect(user='root', password='',host='localhost',database='tm-fly3d-v2')
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

    def CrearMision(self, UserId, MunicipioId, Lugar, Fecha, HoraInicio, HoraFinal): #LaserCalM, LaserCalB, VelocidadVuelo, paramAlg1, paramAlg2, paramAlg3, paramAlg4):
        self.cursor.execute(("INSERT INTO Mision(Users_id, Municipio_id, Lugar, Fecha, HoraInicio, HoraFin, LaserCalM, LaserCalB, VelocidadVuelo, paramAlg1, paramAlg2, paramAlg3, paramAlg4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"), (UserId, MunicipioId, Lugar.lower(), Fecha, HoraInicio, HoraFinal, 1, 1, 1, 1, 1, 1, 1))
        self.commit()

"""Conexión a tabla Usuarios 

Funciones:

1. Obtener usuarios
2. Verificar existencia de usuario (input = email)
3. Obtener nombre de usuario 
4. Insertar usuario


"""
class Database_Users:
    def __init__(self):
        self._cnx = mysql.connector.connect(user='root', password='',host='localhost',database='tm-fly3d-v2')
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
        self.cursor.execute("SELECT NombreUsuario, ApellidosUsuario, EmailUsuario FROM Users")
        usuarios = self.cursor.fetchall()
        return usuarios  

    def ElUsuarioExiste(self, Email):
        self.cursor.execute("SELECT EmailUsuario FROM Users")
        usuarios = self.cursor.fetchall()
        self.existe = False
        for row in usuarios:
            if row[0].lower() == Email.lower():
                self.existe = True
        return self.existe   

    def ObtenerNombreUsuario(self, Email):
        self.cursor.execute("SELECT EmailUsuario, NombreUsuario FROM Users")
        usuarios = self.cursor.fetchall()
        self.nombre = ""
        for row in usuarios:
            if row[0].lower() == Email.lower():
                self.nombre = row[1]
        return self.nombre

    def IngresarUsuario(self, NombreUsuario, ApellidosUsuario, EmailUsuario, ClaveUsuario):
        self.cursor.execute(("INSERT INTO Users(NombreUsuario, ApellidosUsuario, EmailUsuario, ClaveUsuario) VALUES (%s, %s, %s, %s)"), (NombreUsuario.lower(), ApellidosUsuario.lower(), EmailUsuario.lower(), ClaveUsuario))
        self.commit()

    def ObtenerIdUsuario(self, Email):
        self.cursor.execute(("SELECT id FROM Users WHERE EmailUsuario = %s"), (Email.lower(),))
        idUsuario = self.cursor.fetchall()
        return idUsuario[0][0]

    def CompararContrasena(self, Email, contrasenaIngresada):
        contrasena = self.cursor.execute(("SELECT ClaveUsuario FROM Users WHERE EmailUsuario = %s"), (Email.lower(),))
        self.coincide = False
        if contrasena == contrasenaIngresada:
            self.coincide = True
        return self.coincide

"""Conexión a tabla Depto

Funciones:

1. ObtenerDeptos():
2. IngresarDepto(nombre, descripcion): Permite ingresar datos de municipios
3. ExisteDepto(nombre):
4. BorrarDepto(nombre)

"""

class Database_Depto:
    def __init__(self):
        self._cnx = mysql.connector.connect(user='root', password='',host='localhost',database='tm-fly3d-v2')
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
        self._cnx = mysql.connector.connect(user='root', password='',host='localhost',database='tm-fly3d-v2')
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

    def ObtenerMunicipiosFromDepto(self, nombre):
        self.cursor.execute("SELECT municipio.nombre, depto.nombre FROM municipio INNER JOIN depto ON municipio.Depto_id = depto.id WHERE depto.nombre = %s", (nombre.lower(),))
        municipios = self.cursor.fetchall()
        return municipios
    
    def IngresarMunicipio(self, deptoId, nombre, descripcion):
        self.cursor.execute(("INSERT INTO municipio(Depto_id, nombre, descripcion) VALUES (%s, %s, %s)"), (deptoId, nombre, descripcion,))
        self.commit()

    def ExisteMunicipio(self, nombre):
        self.cursor.execute("SELECT nombre FROM municipio")
        deptos = self.cursor.fetchall()
        self.existe = False
        for row in deptos:
            if row[0].lower() == nombre.lower():
                self.existe = True
        return self.existe   

    def BorrarMunicipio(self, nombre):
        self.cursor.execute("DELETE FROM municipio WHERE nombre = %s", nombre)    
        self.commit()
        return self.cursor.rowcount

    def ObtenerDepto(self, nombre):
        self.cursor.execute("SELECT municipio.nombre, depto.nombre FROM municipio INNER JOIN depto ON municipio.Depto_id = depto.id WHERE municipio.nombre = %s", (nombre.lower(),))
        return self.cursor.fetchall()

    def ObtenerIdMunicipio(self, nombre):
        self.cursor.execute(("SELECT id FROM Municipio WHERE nombre = %s"), (nombre.lower(),))
        idMuni = self.cursor.fetchall()
        return idMuni[0][0]

"""Conexión a tabla Laser

Funciones:

1. ObtenerDeptos():
2. IngresarDepto(nombre, descripcion): Permite ingresar datos de municipios
3. ExisteDepto(nombre):
4. BorrarDepto(nombre)

"""

class Database_LaserData:
    def __init__(self):
        self._cnx = mysql.connector.connect(user='root', password='',host='localhost',database='tm-fly3d-v2')
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
        self._cnx = mysql.connector.connect(user='root', password='',host='localhost',database='tm-fly3d-v2')
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
        self._cnx = mysql.connector.connect(user='root', password='',host='localhost',database='tm-fly3d-v2')
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

"""
con = Database_Municipio()
municipios = con.ObtenerMunicipiosFromDepto('VALLE DEL CAUCA')
print(municipios)
con.close()
"""

#db = Database_Mision()
#print(db.ElUsuarioExiste("jsaz977@gmail.com"))
#print(db.ObtenerUsuarios())
#db.IngresarUsuario("Juan", "Astudillo", "jsaz977@gmail.com", "1234")
#print(db.ObtenerIdUsuario("jsaz977@gmail.com"))
#print(db.ObtenerIdMunicipio("medellin"))
#db.CrearMision(2, 1005, "canchas", "2021-01-17", "16:31:45", "16:31:45")
#db.close()