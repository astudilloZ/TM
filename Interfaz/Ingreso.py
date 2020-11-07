import sys
from ConectoresBD import Database_Table_Usuarios
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QGridLayout, QMessageBox, QLabel, QPushButton, QLineEdit, QSpinBox

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
        uic.loadUi("Login.ui", self) 
        self.setWindowTitle("Fly3D")
        #Poner campos de contraseña ocultos
        self.ContrasenaIS.setEchoMode(QLineEdit.Password)
        self.ContrasenaR.setEchoMode(QLineEdit.Password)
        self.ContrasenaR2.setEchoMode(QLineEdit.Password)
        self.centerOnScreen()
        #Listeners de los botones
        self.Rbutton.clicked.connect(self.InsertarUsuario)
        self.ISbutton.clicked.connect(self.IniciarSesion)

    def get_nombre(self):
        global nombre
        return nombre

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

    #Metodo registrarse 
    def InsertarUsuario(self):
        #Extraer información
        nombreIntroducido = self.nombreUsuarioR.text()
        contrasenaIntroducida = self.ContrasenaR.text()
        contrasenaIntroducidaConfirmacion = self.ContrasenaR2.text()
        emailIntroducido = self.EmailR.text()
        direccionIntroducida = self.DireccionR.text()
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
        bd = Database_Table_Usuarios()
        global nombre
        nombre = bd.ObtenerNombreUsuario(emailIntroducido)       
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


#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
app.setStyle("plastique")
#Crear un objeto de la clase
_ventana = IngresoUsuarios()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()