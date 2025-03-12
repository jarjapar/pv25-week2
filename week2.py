import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

class UserRegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.setGeometry(100, 100, 500, 400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserRegistrationForm()
    window.show()
    sys.exit(app.exec_())
