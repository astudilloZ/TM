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
from Cruds import Database_Mision, Database_Municipio, Database_Depto
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QDateTime
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
        #Ajustar formatos datetime
        self.inicioDT.setDisplayFormat("dd/MM/yyyy hh:mm:ss")
        self.finDT.setDisplayFormat("dd/MM/yyyy hh:mm:ss")
        #Setear fecha datetime
        self.SetDatetimeInicio()
        self.SetDatetimeFin()
        #Listeners de los botones
        self.Rbutton.clicked.connect(self.insertarUsuario)
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

    #Setear fecha en datatime inicio
    def SetDatetimeInicio(self):
        now = QDateTime.currentDateTime()
        self.inicioDT.setDateTime(now)

    def SetDatetimeFin(self):
        now = QDateTime.currentDateTime()
        self.finDT.setDateTime(now)

    #Obtener fecha de inicio mision
    def GetDatetimeInicio(self):
        dt = self.inicioDT.dateTime()
        dt_string = dt.toString(self.inicioDT.displayFormat())
        return dt_string

    #Obtener fecha de fin mision
    def GetDatetimeFin(self):
        dt = self.finDT.dateTime()
        dt_string = dt.toString(self.finDT.displayFormat())
        return dt_string

    #Metodo registrarse 
    def insertarUsuario(self):
        #Extraer información
        depto_I = self.deptoCB.currentText()
        municipio_I = self.munCB.currentText()
        lugar_I = self.lugarR.text()       
        nombre_I= self.nombreR.text()
        apellido_I = self.apellidoR.text()
        email_I = self.emailR.text()
        contrasena_I = self.contrasenaR.text()
        contrasena_Confirmacion = self.contrasenaR2.text()
        fecha_Ini_Mision = self.GetDatetimeInicio()
        fecha_Fin_Mision = self.GetDatetimeFin()

        """
        print("depto: "+str(depto_I)+" muni: "+str(municipio_I)+" lugar: "+str(lugar_I)+" nombreI: "+str(nombre_I))
        print(" apellidoI: "+str(apellido_I)+" emailI: "+str(email_I)+" contrasenaI: "+str(contrasena_I))
        print(" contrasenaI2: "+str(contrasena_Confirmacion)+" fechaI: "+str(fecha_Ini_Mision)+" fechaF: "+str(fecha_Fin_Mision))
        """

        #Verificar que los campos sean validos
        if nombreIntroducido == "" or contrasenaIntroducida == "" or emailIntroducido == "":
            QMessageBox.warning(self, "Error en las credenciales", "Los campos nombre de usuario, email y/o contraseña no pueden ser nulos", QMessageBox.Ok)
        #Verificar que las contraseñas coincidan
        elif contrasenaIntroducida != contrasenaIntroducidaConfirmacion:   
            QMessageBox.warning(self, "Error en las credenciales", "Las contraseñas deben coincidir", QMessageBox.Ok) 
        #Si son validos
        else:
            #Buscar si el usuario ya existe
            bd = Database_Table_Usuarios()
            existe = bd.ElUsuarioExiste(emailIntroducido)
            #Si no existe, se inserta en base de datos
            if existe == False:  
                try:
                    bd.IngresarUsuario(nombreIntroducido, contrasenaIntroducida, direccionIntroducida, emailIntroducido)
                    QMessageBox.information(self, "Correcto", "Usuario guardado", QMessageBox.Ok)
                except:
                    QMessageBox.warning(self, "Error", "No se pudo registrar el usuario, por favor vuelva a intentarlo.", QMessageBox.Ok)
            #Si existe se manda mensaje de error
            else:
                QMessageBox.warning(self, "Error", "El usuario ya existe!!", QMessageBox.Ok)  
            #Cerrar conexió base de datos
            bd.close()
        

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
