from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
# from PySide6.QtCore import QFile
from PySide6 import QtCore
import sys


def loadUiWidget(ui_file_name, parent=None):
    loader = QUiLoader()
    uifile = QtCore.QFile(ui_file_name)
    uifile.open(QtCore.QFile.ReadOnly)
    ui = loader.load(uifile, parent)

    return ui

def callback():
    print('Callback login')
def recuperar_senha():
    print('Esqueci')
    recuperacao_window = loadUiWidget('esqueci.ui')
    recuperacao_window.show()

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    MainWindow = loadUiWidget('untitled.ui')
    MainWindow.show()
    MainWindow.setWindowTitle('Faça login agora')
    MainWindow.btn_login.clicked.connect(callback)
    MainWindow.btn_esqueci.clicked.connect(recuperar_senha)

    sys.exit(app.exec())