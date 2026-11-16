import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#subclass QMainWindow to customise the application's main window 
class MainWindow(QMainWindow):
    def __init__(self):
        super.__init__()

        self.setWindowTitle("My App")
        
        button = QPushButton("This is a button")
        self.setCentralWidget(button) #used to place a widget in the window - by default it takes the whole of the window

#passing in sys.argv allows command line arguments 
app = QApplication(sys.argv)

window = QMainWindow()
window.show()

app.exec()