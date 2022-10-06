from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

import sys
from random import choice

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.lable=QLabel()

        self.input = QLineEdit()
        # Note that to connect the input to the label, the input and label must both be defined.
        self.input.textChanged.connect(self.lable.setText)

        # This code adds the two widgets to a layout, and sets that on the window.
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.lable)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
