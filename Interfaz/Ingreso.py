"""
Realizó: Juan Sebastian Astudillo
TG: Fly3d
25-oct-2020
"""

#Importar paths
import sys
import datetime
sys.path.append('/Users/juansebastianastudillozambrano/Documents/TM-git/Cruds')
#Importar librerias 
from Cruds import Database_Mision, Database_Users, Database_Municipio, Database_Depto
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QDateTime, QTime, QDate
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDialog, QGridLayout, 
QMessageBox, QLabel, QPushButton, QLineEdit, QSpinBox)

class IngresoUsuarios(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        global nombre
        global ingreso
        nombre = ""
        ingreso = False
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("/Users/juansebastianastudillozambrano/Documents/TM-git/Interfaz/Login.ui", self) 
        self.setWindowTitle("Fly3D")
        #Poner campos de contraseña ocultos
        self.contrasenaIS.setEchoMode(QLineEdit.Password)
        self.contrasenaR.setEchoMode(QLineEdit.Password)
        self.contrasenaR2.setEchoMode(QLineEdit.Password)
        #Centrar pantalla
        self.centerOnScreen()
        #Llenar combo box
        self.mostrarDeptos()
        self.mostrarMuni()
        #Ajustar formatos date
        self.FechaR.setDisplayFormat("yyyy-MM-dd")
        #Ajustar formatos time
        self.HoraInicioR.setDisplayFormat("hh:mm:ss")
        self.HoraFinR.setDisplayFormat("hh:mm:ss")
        #Setear fecha 
        self.SetDatetimeInicio()
        #Setear horas
        self.SetHoraInicio()
        self.SetHoraFin()
        #Listeners de los botones
        self.Rbutton.clicked.connect(self.NuevaMision)
        self.ISbutton.clicked.connect(self.IniciarSesion)
        self.deptoCB.activated.connect(self.mostrarMuni) 
    
    #Obtener nombre de usuario
    def get_nombre(self):
        global nombre
        return nombre

    #Obtener ingreso 
    def get_ingreso(self):
        global ingreso
        return ingreso

    #Centrar la ventana  
    def centerOnScreen(self):
        qr = self.frameGeometry()
        qr.moveCenter(QtWidgets.QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())

    #Evento para cuando la ventana se cierra
    def closeEvent(self, event):
        global ingreso
        if ingreso == False:
            resultado = QMessageBox.question(self, "Salir ...", "¿Seguro que quieres salir de la aplicación?", QMessageBox.Yes | QMessageBox.No)
            if resultado == QMessageBox.Yes: 
                event.accept()
                sys.exit
            else: event.ignore() 
        else:
            event.accept()
            sys.exit

    #Cargar departamentos
    def mostrarDeptos(self):
        con = Database_Depto()
        deptos = con.ObtenerDeptos()
        con.close()
        for i in range(len(deptos)):
            self.deptoCB.addItem(str(deptos[i])[2:-3])
    
    #Cargar municipios
    def mostrarMuni(self):
        self.munCB.clear()
        con = Database_Municipio()   
        municipios = con.ObtenerMunicipiosFromDepto(self.deptoCB.currentText())
        con.close()
        for i in range(len(municipios)):
            self.munCB.addItem(str(municipios[i][0]))

    #Setear fecha en fecha inicio 
    def SetDatetimeInicio(self):
        now = QDate.currentDate()
        self.FechaR.setDate(now)

    #Obtener fecha de inicio mision
    def GetDatetimeInicio(self):
        dt = self.FechaR.date()
        dt_string = dt.toString(self.FechaR.displayFormat())
        return dt_string

    #Setear hora en hora de inicio 
    def SetHoraInicio(self):
        now = QTime.currentTime()
        self.HoraInicioR.setTime(now)

    #Setear hora en hora fin
    def SetHoraFin(self):
        now = QTime.currentTime()
        self.HoraFinR.setTime(now)

    #Obtener hora de inicio
    def GetHoraInicio(self):
        dt = self.HoraInicioR.time()
        dt_string = dt.toString(self.HoraInicioR.displayFormat())
        return dt_string

    #Obtener hora de inicio
    def GetHoraFin(self):
        dt = self.HoraFinR.time()
        dt_string = dt.toString(self.HoraFinR.displayFormat())
        return dt_string

    #Metodo registrar misión 
    def NuevaMision(self):
        #Extraer información
        depto_I = self.deptoCB.currentText()
        municipio_I = self.munCB.currentText()
        lugar_I = self.lugarR.text()       
        nombre_I= self.nombreR.text()
        apellido_I = self.apellidoR.text()
        email_I = self.emailR.text()
        contrasena_I = self.contrasenaR.text()
        contrasena_Confirmacion = self.contrasenaR2.text()
        fecha_I = self.GetDatetimeInicio()
        hora_I = self.GetHoraInicio()
        hora_Fin = self.GetHoraFin()

        print("depto_I: "+depto_I)
        print("municipio_I: "+municipio_I)
        print("lugar_I: "+lugar_I)
        print("nombre_I: "+nombre_I)
        print("apellido_I: "+apellido_I)
        print("email_I: "+email_I)
        print("contrasena_I: "+contrasena_I)
        print("contrasena_Confirmacion: "+contrasena_Confirmacion)
        print("fecha_I: "+fecha_I)
        print("hora_I: "+hora_I)
        print("hora_Fin: "+hora_Fin)

        # ------------- Validación de datos---------------------------
        #Calcular diferencia en fechas
        diff = datetime.datetime.strptime(hora_I, '%H:%M:%S') - datetime.datetime.strptime(hora_Fin, '%H:%M:%S')
        #Verificar que los campos  (depto, muni, lugar, nombre, contraseña, email necesarios no sean nulos
        if depto_I == "" or municipio_I == "" or lugar_I == "" or nombre_I == "" or email_I == "" or contrasena_I == "" or contrasena_Confirmacion == "":
            QMessageBox.warning(self, "Campos vacios", "Los campos marcados * no pueden estar vacios", QMessageBox.Ok)
        #Verificar que las contraseñas coincidan
        elif contrasena_I != contrasena_Confirmacion:   
            QMessageBox.warning(self, "Error en las credenciales", "Las contraseñas deben coincidir", QMessageBox.Ok) 
        #Verificar que la fecha fin no se menor que la fecha inicio
        elif diff.total_seconds() > 0:
            QMessageBox.warning(self, "Error en los horarios introducidos", "La hora fin debe ser mayor que la hora inicial", QMessageBox.Ok) 
                
        #Si son validos
        else:
            #Buscar si el usuario ya existe
            bd_users = Database_Users()
            bd_muni = Database_Municipio()
            bd_mision = Database_Mision()
            existe = bd_users.ElUsuarioExiste(email_I)
            #Si no existe, se inserta en base de datos
            if existe == False:  
                try:
                    #Crear Usuario
                    bd_users.IngresarUsuario(nombre_I, apellido_I, email_I, contrasena_I)
                    #Crear nueva misión
                    idUsuario = bd_users.ObtenerIdUsuario(email_I)
                    idMuni = bd_muni.ObtenerIdMunicipio(municipio_I)
                    bd_mision.CrearMision(idUsuario, idMuni, lugar_I, fecha_I, hora_I, hora_Fin)                   
                    QMessageBox.information(self, "Correcto", "Usuario y misión creada!", QMessageBox.Ok)

                except:
                    QMessageBox.warning(self, "Error", "No se pudo registrar el usuario, por favor vuelva a intentarlo.", QMessageBox.Ok)
                      
            #Si existe se le crea una nueva mision
            else:               
                try:
                    #Crear nueva misión
                    idUsuario = bd_users.ObtenerIdUsuario(email_I)
                    idMuni = bd_muni.ObtenerIdMunicipio(municipio_I)
                    bd_mision.CrearMision(idUsuario, idMuni, lugar_I, fecha_I, hora_I, hora_Fin)                   
                    QMessageBox.information(self, "Correcto", "Misión creada para el usuario existente!", QMessageBox.Ok)
                except:
                    QMessageBox.warning(self, "Error", "No se pudo registrar la misión, por favor vuelva a intentarlo.", QMessageBox.Ok)
            #Cerrar conexiones bases de datos
            bd_users.close()
            bd_muni.close()
        
    #Metodo iniciar sesión
    def IniciarSesion(self):
        #Obtener información
        emailIntroducido = self.EmailIS.text()
        contrasenaIntroducida = self.ContrasenaIS.text()
        #bd = Database_Table_Usuarios()
        #global nombre
        #nombre = bd.ObtenerNombreUsuario(emailIntroducido)  

        """     
        #Verificar que los campos sean validos
        if emailIntroducido == "" or contrasenaIntroducida == "":
            QMessageBox.warning(self, "Error en las credenciales", "Los campos email y/o contraseña no pueden ser nulos", QMessageBox.Ok)
        else:
            #Buscar si el usuario ya existe        
            existe = bd.ElUsuarioExiste(emailIntroducido)
            #Existe el nombre
            if existe == True:
                #Verificar que la contraseña coincida
                contraCoincide = bd.CompararContrasena(emailIntroducido, contrasenaIntroducida)
                #Coincide la contraseña
                if contraCoincide == True:
                    global ingreso
                    ingreso = True
                    QMessageBox.information(self, "Correcto", "Sesión iniciada", QMessageBox.Ok)
                    #Interfaz de inicio de sesión
                    from Interfaz import Interfaz
                    self.close()
                #Contraseña no coincide 
                else:
                    QMessageBox.warning(self, "Error en las credenciales", "La contraseña no coincide", QMessageBox.Ok)
            #No existe el nombre
            else:
                QMessageBox.warning(self, "Error", "El usuario no existe!!", QMessageBox.Ok)
        bd.close()
        """


#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
app.setStyle("plastique")
#Crear un objeto de la clase
_ventana = IngresoUsuarios()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()
