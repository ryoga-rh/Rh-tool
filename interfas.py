import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class VentanaConTexto(QWidget):
    def __int__(self):
        super(VentanaConTexto, self).__int__()
        self.crearventana()
    def crearventana(self):
        self.setGeometry(350, 350, 600, 1000)
        self.setWindowTitle("Rh tool")
        self.ponertexto()
    def ponertexto(self):
        texto = QLabel.accessibleDescription(self)
        texto.setText("Prueba de interfas grafica")
        texto.move(100, 100)

class Aplicacion_Gui(QWidget):

    def __init__(self, logic):
        super().__init__()
        self.title = 'Mi aplicación'
        self.left = 80
        self.top = 80
        self.width = 300
        self.height = 320
        self.inicializar_GUI()

    def inicializar_GUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion_Gui()
    window.show()
    sys.exit(app.exec_())
