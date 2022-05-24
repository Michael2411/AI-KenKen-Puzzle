import re
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import Generate
import AIGUI
from PyQt5.uic import loadUiType
MainUI, _ = loadUiType('kenken.ui')

#from NEW_ERROR_FINAL import *

#from interface import Ui_MainWindow


class Main(QMainWindow, MainUI):

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
        self.btn_play.clicked.connect(self.startPlay)

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
        grid = Generate.generate(size)

    def startPlay(self):
        print(size, grid)
        AIGUI.GamePlaying(size, grid)

    #     self.generateScannerOutput.setEnabled(False)
    #     self.startScanningButton.setEnabled(False)
    #     self.insertButton.clicked.connect(self.import_file)
    #     #self.generateScannerOutput.connect(self.import_output_file)
    #     #self.d = self.addressLineEdit.text()
    #     self.generateScannerOutput.clicked.connect(self.importOutputFile)
    #     self.startScanningButton.clicked.connect(self.behavior)
    #     self.showTree.clicked.connect(self.showPicture)

    # def showPicture(self):
    #     self.picture.setPixmap(QtGui.QPixmap("sun.png"))
    #     self.picture.setScaledContents(True)

    # def behavior(self):
    #     self.alertLineEdit.setText("THe file is being scanned......")
    #     loop = QEventLoop()
    #     QTimer.singleShot(2000, loop.quit)
    #     loop.exec_()
    #     self.alertLineEdit.setText("File is finished !")
    #     self.generateScannerOutput.setEnabled(True)

    # def import_file(self):
    #     global line
    #     file_filter = 'Data File(*.txt)'

    #     response = QFileDialog.getOpenFileNames(
    #         parent=self,
    #         caption='select a data file',
    #         directory=os.getcwd(),
    #         filter=file_filter,
    #         initialFilter='Data File(*.txt)'
    #     )
    #     print(response[0])
    #     word_url = str(response[0]).replace('[', '')
    #     word_url = word_url.replace(']', '')
    #     word_url = word_url.replace("'", '')
    #     self.addressLineEdit.setText(word_url)
    #     self.startScanningButton.setEnabled(True)
    #     #file_name = re.split('/', word_url)
    #     #print(file_name[-1])
    #     #os.startfile(word_url)
    #     if word_url:
    #         line = compilers.scannerMain(word_url)
    #     else:
    #         self.alertLineEdit.setText("")
    #         self.tokensLineEdit.setText("")
    #     #compilers.getUrl(word_url)
    #     return word_url

    # def importOutputFile(self):
    #     #compilers.scannerMain(self.import_file())
    #     #output=compilers.scannerMain(self.import_file())
    #     os.startfile("outputTokens.txt")
    #     self.tokensLineEdit.setText(line)


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
