import re
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
from AIGUI import Game_Gui
from Generate import kenken_generate
from backtracking import kenken_backtracking
from forward import kenken_forward
import kenken_arc
#from PyQt5.uic import loadUiType
#MainUI, _ = loadUiType('kenken.ui')

#from NEW_ERROR_FINAL import *

from main import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.r_1.clicked.connect(self.setSize)  # 3
        self.r_2.clicked.connect(self.setSize)  # 4
        self.r_3.clicked.connect(self.setSize)  # 5
        self.r_4.clicked.connect(self.setSize)  # 6
        self.r_5.clicked.connect(self.setSize)  # 7
        self.r_6.clicked.connect(self.setSize)  # 8
        self.r_7.clicked.connect(self.setSize)  # 9
        self.btn_backtrack.clicked.connect(self.playBacktrack)
        self.btn_forward.clicked.connect(self.playForward)
        self.btn_arc.clicked.connect(self.playArc)

    def setSize(self):
        global size
        size = 0
        if self.r_1.isChecked() == True:
            size = 3
        elif self.r_2.isChecked() == True:
            size = 4
        elif self.r_3.isChecked() == True:
            size = 5
        elif self.r_4.isChecked() == True:
            size = 6
        elif self.r_5.isChecked() == True:
            size = 7
        elif self.r_6.isChecked() == True:
            size = 8
        elif self.r_7.isChecked() == True:
            size = 9
        global grid
        global arc
        kenkengenerate = kenken_generate()  # instance
        grid, arc = kenkengenerate.generate(size)
        #print(grid, arc)

    def playBacktrack(self):
        game = kenken_backtracking()
        solution = game.backtracking(grid)
        #print(solution)
        #solution = backtracking.backtracking(grid)
        if (len(solution) == 0):
            self.show_warning_messagebox()
        else:
            global gui
            gui = Game_Gui()
            gui.GamePlaying(size, grid, solution)

    def playForward(self):
        game = kenken_forward()
        solution = game.forward_checking(grid)
        #solution = forward.forward_checking(grid)
        if (len(solution) == 0):
            self.show_warning_messagebox()
        else:
            #gui = Game_Gui()
            gui.GamePlaying(size, grid, solution)

    def playArc(self):
        solution = kenken_arc.start_arc(size, grid, arc)
        if (len(solution) == 0):
            self.show_warning_messagebox()
        else:
            gui.GamePlaying(size, grid, solution)

    def show_warning_messagebox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        # setting message for Message Box
        msg.setText("there is no solution")

        # setting Message box window title
        msg.setWindowTitle("Warning MessageBox")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        # start the app
        retval = msg.exec_()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
