import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox

class UserRegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        identitas_group = QGroupBox("Identitas")
        identitas_layout = QVBoxLayout()
        identitas_layout.addWidget(QLabel("Nama : Muhammad Fajar Maulana"))
        identitas_layout.addWidget(QLabel("NIM : F1D022072"))
        identitas_layout.addWidget(QLabel("Kelas : D"))
        identitas_group.setLayout(identitas_layout)

        nav_group = QGroupBox("Navigation")
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        nav_group.setLayout(nav_layout)

        main_layout.addWidget(identitas_group)
        main_layout.addWidget(nav_group)

        self.setLayout(main_layout)
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.setGeometry(100, 100, 500, 400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserRegistrationForm()
    window.show()
    sys.exit(app.exec_())