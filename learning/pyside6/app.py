import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#subclass QMainWindow to customise the application's main window 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.setFixedSize(400, 400)
        
        button = QPushButton("Press!")
        button.setCheckable(True)
        button.clicked.connect(self.button_pressed) #connect the signal to the slot receiver

        self.setCentralWidget(button) #used to place a widget in the window - by default it takes the whole of the window

    def button_pressed(self):
        print("Button was pressed...")

#passing in sys.argv allows command line arguments 
app = QApplication(sys.argv)

window = MainWindow() #change from QMainWindow to MainWindow class
window.show()

app.exec()