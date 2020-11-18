import sys
import os
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QGridLayout, QMessageBox, QLabel, QPushButton, QLineEdit, QSpinBox, QTableWidget, QTableWidgetItem, QDesktopWidget, QMenu, QVBoxLayout, QSizePolicy, QWidget, QInputDialog, QLineEdit
from PyQt5 import uic, QtGui, QtWidgets
from Ingreso import IngresoUsuarios

class Interfaz(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #self.nombreUsuari = IngresoUsuarios.get_nombre(self)
        global nombre
        nombre = IngresoUsuarios.get_nombre(self)
        global ingreso
        ingreso = IngresoUsuarios.get_ingreso(self)
        #Si se realizó un ingreso satisfactorio se despliega la ventana principal
        if ingreso == True:
            #Cargar la configuración del archivo .ui en el objeto
            uic.loadUi("/Users/juansebastianastudillozambrano/Documents/TM-git/Interfaz/Main.ui", self)
            self.setWindowTitle("Fly3D")
            #Centrar
            self.centerOnScreen()
        else: 
            sys.exit

    #Centrar la ventana  
    def centerOnScreen(self):
        # Get the current screens' dimensions...
        screen = QDesktopWidget().screenGeometry()
        # ... and get this windows' dimensions
        mysize = self.geometry()
        # The horizontal position is calulated as screenwidth - windowwidth /2
        hpos = ( screen.width() - mysize.width() ) / 2
        # And vertical position the same, but with the height dimensions
        vpos = ( screen.height() - mysize.height() ) / 2
        # And the move call repositions the window
        self.move(hpos, vpos)

    #Evento para cuando la ventana se cierra
    def closeEvent(self, event):
        resultado = QMessageBox.question(self, "Salir ...", "¿Seguro que quieres salir de la aplicación?", QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes: 
            event.accept()
            sys.exit
        else: 
            event.ignore() 

    #Evento para cuando la ventana se abre
    def showEvent(self, event):
        #Setear encabezados
        global nombre
        self.BienvenidoLabel.setText("Bienvenido, "+ nombre+" !")  
        self.HoraFecha.setText("Fecha:   "+time.strftime("%d/%m/%y"))

if __name__ == '__main__':
    #Instancia para iniciar una aplicación
    app2 = QApplication(sys.argv)
    app2.setStyle("plastique")
    #Crear un objeto de la clase
    _ventana2 = Interfaz()
    #Mostra la ventana
    _ventana2.show()
    #Ejecutar la aplicación
    try:
        app2.exec()
    except Exception as e:
        sys.exit()