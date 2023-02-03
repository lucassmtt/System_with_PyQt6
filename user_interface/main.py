from PyQt5 import QtCore, QtGui, QtWidgets
from login import Main_window_login
from esqueci import Window_forget_password

if __name__ == "__main__":
    import sys
    class Window_Login(Main_window_login):
        def __init__(self):
            super().__init__()

            self.btn_esqueci.clicked.connect(self.make_forget)



        def make_forget(self):
            print('OLA')
            self.MakeWindow_2 = QtWidgets.QMainWindow()
            self.Window_forget = Window_forget_password()

            self.Window_forget.setupUi(self.MakeWindow_2)

            self.MakeWindow_2.show()


    app = QtWidgets.QApplication(sys.argv)
    MakeWindow_1 = QtWidgets.QMainWindow()


    Window_login = Main_window_login()
    Window_login.setupUi(MakeWindow_1)

    MakeWindow_1.show()

    sys.exit(app.exec())
