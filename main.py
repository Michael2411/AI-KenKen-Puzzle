# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kenken.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(718, 313)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 11, 437, 33))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 87, 389, 52))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.r_1 = QtWidgets.QRadioButton(self.layoutWidget)
        self.r_1.setObjectName("r_1")
        self.horizontalLayout.addWidget(self.r_1)
        self.r_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.r_2.setObjectName("r_2")
        self.horizontalLayout.addWidget(self.r_2)
        self.r_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.r_3.setObjectName("r_3")
        self.horizontalLayout.addWidget(self.r_3)
        self.r_4 = QtWidgets.QRadioButton(self.layoutWidget)
        self.r_4.setObjectName("r_4")
        self.horizontalLayout.addWidget(self.r_4)
        self.r_5 = QtWidgets.QRadioButton(self.layoutWidget)
        self.r_5.setObjectName("r_5")
        self.horizontalLayout.addWidget(self.r_5)
        self.r_6 = QtWidgets.QRadioButton(self.layoutWidget)
        self.r_6.setObjectName("r_6")
        self.horizontalLayout.addWidget(self.r_6)
        self.r_7 = QtWidgets.QRadioButton(self.layoutWidget)
        self.r_7.setObjectName("r_7")
        self.horizontalLayout.addWidget(self.r_7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 311, 21))
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 230, 518, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_backtrack = QtWidgets.QPushButton(self.widget)
        self.btn_backtrack.setObjectName("btn_backtrack")
        self.horizontalLayout_4.addWidget(self.btn_backtrack)
        self.btn_forward = QtWidgets.QPushButton(self.widget)
        self.btn_forward.setObjectName("btn_forward")
        self.horizontalLayout_4.addWidget(self.btn_forward)
        self.btn_arc = QtWidgets.QPushButton(self.widget)
        self.btn_arc.setObjectName("btn_arc")
        self.horizontalLayout_4.addWidget(self.btn_arc)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 718, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">WELCOME TO KENKEN PUZZLE !</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">PLEASE CHOOSE THE SIZE OF GRID:</span></p></body></html>"))
        self.r_1.setText(_translate("MainWindow", "3x3"))
        self.r_2.setText(_translate("MainWindow", "4X4"))
        self.r_3.setText(_translate("MainWindow", "5X5"))
        self.r_4.setText(_translate("MainWindow", "6X6"))
        self.r_5.setText(_translate("MainWindow", "7X7"))
        self.r_6.setText(_translate("MainWindow", "8X8"))
        self.r_7.setText(_translate("MainWindow", "9X9"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">PLEASE CHOOSE THE ALGORITHM:</span></p></body></html>"))
        self.btn_backtrack.setText(_translate("MainWindow", "Backtracking"))
        self.btn_forward.setText(_translate("MainWindow", "Backtracking with forward checking"))
        self.btn_arc.setText(_translate("MainWindow", "Backtracking with arc consistency"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

