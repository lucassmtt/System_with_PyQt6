from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib

ROOT = pathlib.Path()

PATH_JSON = ROOT.absolute() / 'DB' / 'cadastro.json'
print(PATH_JSON)

class mainwindowLogin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Main Window")
        MainWindow.resize(661, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 651, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_email = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_email.setObjectName("label_email")
        self.verticalLayout.addWidget(self.label_email)
        self.input_email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_email.setObjectName("input_email")
        self.verticalLayout.addWidget(self.input_email)
        self.label_senha = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_senha.setObjectName("label_senha")
        self.verticalLayout.addWidget(self.label_senha)
        self.input_senha = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_senha.setObjectName("input_senha")
        self.verticalLayout.addWidget(self.input_senha)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 319, 661, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_signin = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_signin.setObjectName("btn_signin")
        self.horizontalLayout.addWidget(self.btn_signin)
        self.btn_login = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout.addWidget(self.btn_login)
        self.btn_esqueci = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_esqueci.setObjectName("btn_esqueci")
        self.horizontalLayout.addWidget(self.btn_esqueci)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_login.clicked.connect(self.call_login)
        self.btn_signin.clicked.connect(self.call_signin)
        self.btn_esqueci.clicked.connect(self.call_esqueci)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Faça login com sua conta!"))
        MainWindow.setFixedSize(670, 450)
        self.label_email.setText(_translate("MainWindow", "Email:"))
        self.label_senha.setText(_translate("MainWindow", "Senha:"))
        self.btn_signin.setText(_translate("MainWindow", "Sign-in"))
        self.btn_login.setText(_translate("MainWindow", "Log-in"))
        self.btn_esqueci.setText(_translate("MainWindow", "Esqueci minha senha"))

    def call_login(self):
        print('Call-back login')
        import sqlite3 as sql
        from pathlib import Path
        absolute_root = Path.absolute()
        print(absolute_root)
    def call_esqueci(self):
        print('Call-back ')
        from forget_password import Window_forget_password
        self.Janela = QtWidgets.QMainWindow()

        self.ui_esqueci = Window_forget_password()
        self.ui_esqueci.setupUi(self.Janela)
        self.Janela.show()

    def call_signin(self):
        print('callback signin')
        from signin import signin_Ui
        self.janela_signin = QtWidgets.QMainWindow()

        self.ui_signin = signin_Ui()
        self.ui_signin.setupUi(self.janela_signin)
        self.janela_signin.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainwindowLogin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
