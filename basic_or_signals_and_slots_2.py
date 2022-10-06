import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # We need to be able to access the buttton in our the_button_was_clicked method,
        # so we keep a reference to it on self
        self.button = QPushButton('Press me')
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText(
            'You already clicked me')  # You can change the text of a button by passing a str to .setText()
        self.button.setEnabled(False)  # to disable a button call .set Enabled() with False.

        self.setWindowTitle("My Oneshot App")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
