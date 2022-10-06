import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #  We must always call the __init__ method of the super() class.

        self.setWindowTitle("My App")

        button = QPushButton("Press me")

        # notice that when the program is running the maximized control is disabled
        # self.setFixedSize(QSize(400,600)) # create a fixed size window

        # set the minimum and maximum sizes respectively.
        self.setMaximumSize(QSize(400,400))
        self.setMinimumSize(QSize(200,200))
        # also could use:
        # self.setMaximumWidth()
        # self.setMaximumHeight()
        # self.setMinimumWidth()
        # self.setMinimumHeight()

        # This is a QMainWindow specific function that allows you to set the widget that goes in the middle of the window.
        self.setCentralWidget(button) # to place a widget in the QMainWindow. Set the central widget of the Window.

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()