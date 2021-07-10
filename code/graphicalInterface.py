# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphicalInterface.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

refreshRate = 50
saveLog = True

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(455, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(180, 80, 101, 51))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.refreshRate = QtWidgets.QPushButton(self.centralwidget)
        self.refreshRate.setGeometry(QtCore.QRect(140, 140, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.refreshRate.setFont(font)
        self.refreshRate.setObjectName("refreshRate")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 30, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.saveLog = QtWidgets.QCheckBox(self.centralwidget)
        self.saveLog.setGeometry(QtCore.QRect(180, 190, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.saveLog.setFont(font)
        self.saveLog.setObjectName("saveLog")
        self.init = QtWidgets.QPushButton(self.centralwidget)
        self.init.setGeometry(QtCore.QRect(140, 220, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.init.setFont(font)
        self.init.setObjectName("init")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 455, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # Colocamos as funcoes que irao fazer o mapeamento

        # Amarra o botao a essa funcao
        self.refreshRate.clicked.connect(self.clicked)
        # Adicionado por nos
        self.refreshRate.clicked.connect(self.pressedRefreshRate)

        self.init.clicked.connect(self.pressedInit)

        self.saveLog


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Logger for ATMega328P"))
        self.label.setText(_translate("MainWindow", "Data Logger - ENGC50"))
        self.comboBox.setItemText(0, _translate("MainWindow", "50"))
        self.comboBox.setItemText(1, _translate("MainWindow", "500"))
        self.comboBox.setItemText(2, _translate("MainWindow", "1000"))
        self.comboBox.setItemText(3, _translate("MainWindow", "5000"))
        self.comboBox.setItemText(4, _translate("MainWindow", "10000"))
        self.comboBox.setItemText(5, _translate("MainWindow", "15000"))
        self.refreshRate.setText(_translate("MainWindow", "Atualizar Taxa"))
        self.label_2.setText(_translate("MainWindow", "Taxa de Aquisição de Dados (ms):"))
        self.saveLog.setText(_translate("MainWindow", "Salvar Log"))
        self.init.setText(_translate("MainWindow", "Inicializar"))
    

    # Event functions pra mapear os eventos com a Interface Grafica
    def clicked(self):
        print("[INFO]: Setting new rate for the acquistion...")

    def pressedRefreshRate(self):
        global refreshRate
        print("[INFO]: Retrieving refresh rate for the graph to update...")
        refreshRate = self.comboBox.currentText()
        refreshRate = int(refreshRate)
        print("[INFO]: Refresh rate set to: {!r}".format(refreshRate))

    def pressedInit(self):
        print("[INFO]: Calling main program (main from the source code)")
        self.logCheckBox()
        st = "python dataPlotter.py -s "+str(saveLog)+" -r "+str(refreshRate)
        os.system(st)


    def logCheckBox(self):
        global saveLog
        if self.saveLog.isChecked():
            print("[INFO]: Logging has been activated")
            saveLog = True
        else:
            print("[INFO]: Logging has been deactivated")
            saveLog = False




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

