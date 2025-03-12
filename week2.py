import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QComboBox

class UserRegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        identitas_group = QGroupBox("Identitas")
        identitas_layout = QVBoxLayout()
        identitas_layout.addWidget(QLabel("Nama : Muhammad Fajar Maulana"))
        identitas_layout.addWidget(QLabel("NIM : F1D022072"))
        identitas_layout.addWidget(QLabel("Kelas : D"))
        identitas_group.setLayout(identitas_layout)

        nav_group = QGroupBox("Navigation")
        nav_layout = QHBoxLayout()
        home_btn = QPushButton("Home")
        about_btn = QPushButton("About")
        contact_btn = QPushButton("Contact")
        
        nav_layout.addWidget(home_btn)
        nav_layout.addWidget(about_btn)
        nav_layout.addWidget(contact_btn)
        nav_group.setLayout(nav_layout)

        form_group = QGroupBox("User Registration")
        form_layout = QVBoxLayout()
        self.fullname_input = QLineEdit()
        self.fullname_input.setPlaceholderText("Enter your full name")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Enter your phone number")

        self.gender_male = QRadioButton("Male")
        self.gender_female = QRadioButton("Female")
        self.country_select = QComboBox()
        self.country_select.addItems(["Select Country", "Zanzibar", "Kamerun", "Enggres", "Indonesia"])

        form_layout.addWidget(QLabel("Full Name:"))
        form_layout.addWidget(self.fullname_input)
        form_layout.addWidget(QLabel("Email:"))
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(QLabel("Phone:"))
        form_layout.addWidget(self.phone_input)

        gender_layout = QHBoxLayout()
        gender_layout.addWidget(QLabel("Gender:"))
        gender_layout.addWidget(self.gender_male)
        gender_layout.addWidget(self.gender_female)
        form_layout.addLayout(gender_layout)

        country_layout = QHBoxLayout()
        country_layout.addWidget(QLabel("Country:"))
        country_layout.addWidget(self.country_select)
        form_layout.addLayout(country_layout)
        form_group.setLayout(form_layout)

        actions_group = QGroupBox("Actions")
        actions_layout = QHBoxLayout()
        
        submit_btn = QPushButton("Submit")
        cancel_btn = QPushButton("Cancel")
        actions_layout.addWidget(submit_btn)
        actions_layout.addWidget(cancel_btn)
        actions_group.setLayout(actions_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(identitas_group)
        main_layout.addWidget(nav_group)
        main_layout.addWidget(form_group)
        main_layout.addWidget(actions_group)

        self.setLayout(main_layout)
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.setGeometry(100, 100, 500, 400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = UserRegistrationForm()
    window.show()
    sys.exit(app.exec_())