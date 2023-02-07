import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QWidget


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 200)

        # Connect to database
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()

        # Create username and password inputs
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        # Create login button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Username"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Password"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        # Set layout to central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Check if username and password match any record in the database
        query = "SELECT * FROM users WHERE username=? AND password=?"
        result = self.cursor.execute(query, (username, password)).fetchone()

        if result:
            self.close()
            print("Login successful")
        else:
            print("Login failed")

    def closeEvent(self, event):
        self.conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())