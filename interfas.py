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
        texto = QLabel(self)
        texto.setText("Prueba de interfas grafica")
        texto.move(100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaConTexto()
    window.show()
    sys.exit(app.exec_())
