import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button_is_checked = True  # Set the default value for our variable

        self.button = QPushButton('Press me') # We need to keep a reference to the button on self so we acn access it in out slot.
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released) # The released signal fires when the button is released, but does not send the check state
        self.button.setChecked(self.button_is_checked)


        self.setCentralWidget(self.button)


    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()  # .isChecked() returen the check state of the button

        print(self.button_is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
