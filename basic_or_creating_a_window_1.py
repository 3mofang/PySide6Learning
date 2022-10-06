# QApplication, the application handler
# QWidget, a basic empty GUIwidget
# both from the QtWidgets module.
from PySide6.QtWidgets import QApplication, QWidget

import sys

# create an instance of QApplication, passing in sys.arg, which is Python
# list containing the command line arguments passed to the application.
app = QApplication(sys.argv)
# If you know you won’t be using command line arguments to control Qt you can
# pass in an empty list instead, e.g app = QApplication([])

window = QWidget() #create an instance of a QWidget using the variable name window.
# Widgets without a parent are invisible by default. So, after
# creating the window object, we must always call .show() to make
# it visible.
window.show()


app.exec() #  to start up the event loop.