# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyToDo.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 481)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 70, 311, 411))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(18)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(10, 0, 191, 51))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 50, 191, 51))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 100, 191, 51))
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 150, 191, 51))
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 200, 191, 51))
        self.checkBox_7.setText("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_8.setGeometry(QtCore.QRect(10, 250, 191, 51))
        self.checkBox_8.setText("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_9.setGeometry(QtCore.QRect(10, 300, 191, 51))
        self.checkBox_9.setText("")
        self.checkBox_9.setObjectName("checkBox_9")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 60, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 100, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(350, 150, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 26))
        self.menubar.setObjectName("menubar")
        self.menuHELP = QtWidgets.QMenu(self.menubar)
        self.menuHELP.setObjectName("menuHELP")
        self.menuEDIT = QtWidgets.QMenu(self.menubar)
        self.menuEDIT.setObjectName("menuEDIT")
        self.menuFORM = QtWidgets.QMenu(self.menubar)
        self.menuFORM.setObjectName("menuFORM")
        self.menuSETTINGS = QtWidgets.QMenu(self.menubar)
        self.menuSETTINGS.setObjectName("menuSETTINGS")
        self.menuHELP_2 = QtWidgets.QMenu(self.menubar)
        self.menuHELP_2.setObjectName("menuHELP_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHELP.menuAction())
        self.menubar.addAction(self.menuEDIT.menuAction())
        self.menubar.addAction(self.menuFORM.menuAction())
        self.menubar.addAction(self.menuSETTINGS.menuAction())
        self.menubar.addAction(self.menuHELP_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TO-DO LIST"))
        self.label_2.setText(_translate("MainWindow", "ADD A OBJECTIVE ("))
        self.label_3.setText(_translate("MainWindow", "(SEVEN OBJECTIVES ONLY)"))
        self.pushButton.setText(_translate("MainWindow", "ADD OBJECTIVE"))
        self.menuHELP.setTitle(_translate("MainWindow", "HELP"))
        self.menuEDIT.setTitle(_translate("MainWindow", "EDIT"))
        self.menuFORM.setTitle(_translate("MainWindow", "FORM"))
        self.menuSETTINGS.setTitle(_translate("MainWindow", "SETTINGS"))
        self.menuHELP_2.setTitle(_translate("MainWindow", "HELP"))
        self.pushButton.clicked.connect(self.addTask)

    def addTask(self):
        if self.checkBox == "":
            self.checkBox.setText(lineEdit)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
