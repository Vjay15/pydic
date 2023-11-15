from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5 import uic
from pathlib import Path
import logo_rc
import csv

class GUI(QMainWindow):
    def __init__(self):
        super(GUI,self).__init__()
        uic.loadUi("pydic.ui", self)
        self.show()
        self.Search.clicked.connect(self.search)
    def search(self):
        if self.stex.text().isalpha():
            b = self.stex.text() + " "
            root_folder = Path(__file__).parents[1]
            s = "pydic/Dict/"+b[0].upper()+".csv" #To conserve memory
            S = root_folder / s
            A = open(S,"r")
            R = csv.reader(A,delimiter=',')
            global tex
            tex = ""
            for row in R:
                if row == []:
                    continue
                elif b in row[0][0:len(b)]:
                    tex+=row[0]
                    tex+="\n"
            self.output.setText(tex)
        else:
            message = QMessageBox()
            message.setText("Invalid input, Please enter valid words")
            message.exec_()
            tex = "error"
        if tex == "":
            message = QMessageBox()
            message.setText("Word is not available on the dictionary")
            message.exec_()
        A.close()

#Main function calls the Application
def main():
    app = QApplication([])
    window = GUI()
    # Force the style to be the same on all OSs:
    app.setStyle("Fusion")

    # Now a palette to switch to dark colors:
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    app.exec_()

if __name__ == '__main__':
    main()