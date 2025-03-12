import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGroupBox, QVBoxLayout, QHBoxLayout, QPushButton

class UserRegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        form_group = QGroupBox("User Registration")
        form_layout = QVBoxLayout()

        self.fullname_input = QLineEdit()
        self.fullname_input.setPlaceholderText("Enter your full name")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Enter your phone number")

        form_layout.addWidget(QLabel("Full Name:"))
        form_layout.addWidget(self.fullname_input)
        form_layout.addWidget(QLabel("Email:"))
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(QLabel("Phone:"))
        form_layout.addWidget(self.phone_input)
        
        form_group.setLayout(form_layout)

        main_layout.addWidget(form_group)

        self.setLayout(main_layout)
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.setGeometry(100, 100, 500, 400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserRegistrationForm()
    window.show()
    sys.exit(app.exec_())