import sys
from PyQt5.QtWidgets import QLabel,QMainWindow, QApplication,QAction,QMenu, QSlider, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon('web.png') ,'&b1', self)
        
        exitAct.triggered.connect(self.muestra)
        impMenu = QMenu('SM1', self)
        impAct = QAction('b2', self)
        impAct.triggered.connect(self.muestra2)
        impMenu.addAction(impAct)
        self.statusBar().showMessage('Ready')
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&M1')
        fileMenu.addAction(exitAct)
        fileMenu.addMenu(impMenu)
        self.label= QLabel(self)
        self.label.setGeometry(380,250,30,30)
        self.label.setText('50')
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)
        btn1 = QPushButton("Boton 1", self)
        btn1.move(150, 150)
        btn2 = QPushButton("Boton 2", self)
        btn2.move(300, 150)
        btn1.clicked.connect(self.botonPulsado)
        btn2.clicked.connect(self.botonPulsado)
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(170, 250, 200, 30)
        sld.setMinimum(0)
        sld.setMaximum(100)
        sld.setValue(50)
        sld.valueChanged[int].connect(self.changeValue)
        self.setGeometry(300, 300, 550, 350)
        self.setWindowTitle('cosas')
        self.show()
    
    def muestra(self):
        self.statusBar().showMessage('hola')
        
    def muestra2(self):
        self.statusBar().showMessage('hola2')
        
    def changeValue(self, value):
        self.label.setText(f'{value}')
        if value == 100:
            self.statusBar().showMessage('maximo alcanzado')
        if value == 0:
            self.statusBar().showMessage('minimo alcanzado')
    
    def botonPulsado(self):
        txt = self.sender().text()
        self.statusBar().showMessage(txt)        

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()