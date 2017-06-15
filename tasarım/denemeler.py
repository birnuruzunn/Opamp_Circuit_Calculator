# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from sympy import *
import integral as t
import cizim
import turtle
#--------------------------------------------------------------------------------çizim için setleme----------------------------
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("integral_alıcı")
#tam ekran yapmak için
wn.screensize(1000,1000)
wn.setup(width=1.0, height=1.0, startx=None, starty=None) #tam ekran yapmak için

tosbaga = turtle.Turtle()  # kaplumbağa oluşturduk
tosbaga.color("white")
tosbaga.pensize(2)
tosbaga.speed(20) #0-10 arası değer alır aksi taktirde 0 kabul edilir.
tosbaga.hideturtle() #tosbagayı gizledim
#------------------------------------------------------------------------------------------------------------------------------
class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.WindowModal)
        mainWindow.resize(543, 154)
        mainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(440, 90, 87, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
#---------------------------------------------------------------------------------------------------------buttons-------
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")

        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(340, 90, 87, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(240, 90, 87, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 521, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 10, 21, 17))
        self.label.setObjectName("label")

        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(80, 10, 41, 21))
        self.comboBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 21, 17))
        self.label_2.setObjectName("label_2")

        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 10, 41, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(280, 10, 16, 16))
        self.label_3.setObjectName("label_3")

        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(300, 10, 41, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(390, 10, 16, 17))
        self.label_4.setObjectName("label_4")

        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setGeometry(QtCore.QRect(400, 10, 41, 21))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(490, 10, 21, 17))
        self.label_5.setObjectName("label_5")


        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 41, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 10, 41, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 10, 41, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(340, 10, 41, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(440, 10, 41, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.comboBox.setCurrentIndex(0)
        self.pushButton_3.clicked.connect(self.lineEdit.clear)           #temizle butonuna tıklandığında çalışacak kısım
        self.pushButton_3.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_3.clicked.connect(self.lineEdit_3.clear)
        self.pushButton_3.clicked.connect(self.lineEdit_4.clear)
        self.pushButton_3.clicked.connect(self.lineEdit_5.clear)
        self.pushButton.clicked.connect(mainWindow.close)       #çıkış butonuna yıklanıldığında algılayacak signal slotu
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.pushButton_2.clicked.connect(self.sonuc)

        self.lineEdit.setMaxLength(10)
        self.lineEdit_2.setMaxLength(10)
        self.lineEdit_3.setMaxLength(10)
        self.lineEdit_4.setMaxLength(10)
        self.lineEdit_5.setMaxLength(10) #max girdi boyutunu belirledim

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "simülasyon"))
        self.pushButton.setText(_translate("mainWindow", "ÇIKIŞ"))
        self.pushButton_2.setText(_translate("mainWindow", "HESAPLA"))
        self.pushButton_3.setText(_translate("mainWindow", "TEMİZLE"))
        self.label.setText(_translate("mainWindow", "v\'\'\'"))

        self.comboBox.setItemText(0, _translate("mainWindow", "+"))
        self.comboBox.setItemText(1, _translate("mainWindow", "-"))
        self.label_2.setText(_translate("mainWindow", "v\'\'"))
        self.comboBox_2.setItemText(0, _translate("mainWindow", "+"))
        self.comboBox_2.setItemText(1, _translate("mainWindow", "-"))
        self.label_3.setText(_translate("mainWindow", "v\'"))
        self.comboBox_3.setItemText(0, _translate("mainWindow", "+"))
        self.comboBox_3.setItemText(1, _translate("mainWindow", "-"))
        self.label_4.setText(_translate("mainWindow", "v"))
        self.comboBox_4.setItemText(0, _translate("mainWindow", "+"))
        self.comboBox_4.setItemText(1, _translate("mainWindow", "-"))
        self.label_5.setText(_translate("mainWindow", "= 0"))

    def sonuc(self,mainWindow):
        denklem = ""

        if ((harfkontrol(self.lineEdit.text())) and (harfkontrol(self.lineEdit_2.text())) and (
        harfkontrol(self.lineEdit_3.text())) and (harfkontrol(self.lineEdit_4.text())) and (
        harfkontrol(self.lineEdit_5.text()))):
            if (ilkkontrol(self.lineEdit.text())):
                if ((isaretKontrol(self.lineEdit_2.text())) and (isaretKontrol(self.lineEdit_3.text())) and (
                isaretKontrol(self.lineEdit_4.text())) and (isaretKontrol(self.lineEdit_5.text()))):
                    if (len(self.lineEdit.text()) != 0):
                        denklem = "V\'\'\' "
                    if (len(self.lineEdit_2.text()) != 0):
                        denklem += (self.comboBox.currentText() +" "+"("+ self.lineEdit_2.text()) +"/"+ (self.lineEdit.text())\
                                   +")"+ "*V\'\' "
                    if (len(self.lineEdit_3.text()) != 0):
                        denklem += (self.comboBox_2.currentText() +" "+"("+ self.lineEdit_3.text()) +"/"+ (self.lineEdit.text()) \
                                   +")"+ "*V\' "
                    if (len(self.lineEdit_4.text()) != 0):
                        denklem += (self.comboBox_3.currentText() +" "+"("+ self.lineEdit_4.text()) +"/"+ (self.lineEdit.text()) \
                                   +")"+ "*V "
                    if (len(self.lineEdit_5.text()) != 0):
                        denklem += (self.comboBox_4.currentText() +" "+"(" + self.lineEdit_5.text()) +"/"+ (self.lineEdit.text())+")"
                    if ((len(self.lineEdit.text()) == 0) and (len(self.lineEdit_2.text()) == 0) and (
                        len(self.lineEdit_3.text()) == 0) and (len(self.lineEdit_4.text()) == 0) and (len(self.lineEdit_5.text()) != 0)):
                        denklem += " = " + self.comboBox_4.currentText() + self.lineEdit_5.text()
                    else:
                        denklem += " = 0"
                    if ((len(self.lineEdit.text()) == 0) and (len(self.lineEdit_2.text()) == 0) and (
                        len(self.lineEdit_3.text()) == 0) and (len(self.lineEdit_4.text()) == 0) and (len(self.lineEdit_5.text()) == 0)):
                        denklem = ""
                    if(len(denklem) != 0):
                        print(denklem)

        if ((harfkontrol(self.lineEdit.text())) and (harfkontrol(self.lineEdit_2.text())) and (
        harfkontrol(self.lineEdit_3.text())) and (harfkontrol(self.lineEdit_4.text())) and (
        harfkontrol(self.lineEdit_5.text()))):
            if (ilkkontrol(self.lineEdit.text())):
                if ((isaretKontrol(self.lineEdit_2.text())) and (isaretKontrol(self.lineEdit_3.text())) and (
                isaretKontrol(self.lineEdit_4.text())) and (isaretKontrol(self.lineEdit_5.text()))):
                    if ((len(self.lineEdit.text()) != 0) and (self.lineEdit.text()!= "0")):
                        denklem = "V\'\'\' = "
                        if (len(self.lineEdit_2.text()) != 0):
                            denklem += (("+" if self.comboBox.currentIndex() == 1  else "-")+" "+"("+self.lineEdit_2.text())+"/"+(self.lineEdit.text())\
                                       +")"+ "*({})".format(t.integral(1)) + "*V\'\' "
                        if (len(self.lineEdit_3.text()) != 0):
                            denklem += (("+" if self.comboBox_2.currentIndex() == 1  else "-")+" "+"("+self.lineEdit_3.text())+"/"+(self.lineEdit.text())\
                                       + ")"+ "*({})".format(t.integral(2)) + "*V\' "
                        if (len(self.lineEdit_4.text()) != 0):
                            denklem += (("+" if self.comboBox_3.currentIndex() == 1  else "-") +" "+"("+self.lineEdit_4.text())+"/"+(self.lineEdit.text())\
                                       + ")"+ "*({})".format(t.integral(3)) + "*V "
                        if (len(self.lineEdit_5.text()) != 0):
                            denklem += (("+" if self.comboBox_4.currentIndex() == 1  else "-")+" "+"("+self.lineEdit_5.text())+"/"+(self.lineEdit.text())+")"
                    else:
                        if(self.lineEdit.text()!= "0"):
                            denklem = self.lineEdit.text() + "V\'\'\'"
                            denklem += " = 0"

                    if ((len(self.lineEdit.text()) == 0) and (len(self.lineEdit_2.text()) == 0) and
                        (len(self.lineEdit_3.text()) == 0) and (len(self.lineEdit_4.text()) == 0) and
                        (len(self.lineEdit_5.text()) == 0)):
                        denklem = ""
                    if (len(denklem) != 0):
                        print(denklem)
#-------------------------------------------------------------------------------kulanıcı girişini alıp çizdirdiğim kısım------
            if ((harfkontrol(self.lineEdit.text())) and (harfkontrol(self.lineEdit_2.text())) and (
                    harfkontrol(self.lineEdit_3.text())) and (harfkontrol(self.lineEdit_4.text())) and (
                    harfkontrol(self.lineEdit_5.text()))):
                if (ilkkontrol(self.lineEdit.text())):
                    if ((isaretKontrol(self.lineEdit_2.text())) and (isaretKontrol(self.lineEdit_3.text())) and (
                            isaretKontrol(self.lineEdit_4.text())) and (isaretKontrol(self.lineEdit_5.text()))):
                        if ((len(self.lineEdit.text()) != 0) and (self.lineEdit.text() != "0")):
                            cizim.integral_alan(tosbaga)
                            cizim.integral_alan(tosbaga)
                            cizim.integral_alan(tosbaga)
                            if ((len(self.lineEdit_2.text()) != 0) and (self.lineEdit_2.text() != "0")):
                                if (self.comboBox.currentIndex() == 0):
                                    cizim.konum = [-400, 100]
                                    tosbaga.penup()
                                    tosbaga.setposition(cizim.konum[0] + 131, cizim.konum[1])
                                    tosbaga.pendown()
                                    tosbaga.right(90)
                                    tosbaga.forward(295)
                                    tosbaga.left(90)
                                    tosbaga.forward(100)
                                    if (len(self.lineEdit_4.text()) == 0) or (self.lineEdit_4.text() == "0"):
                                        if (len(self.lineEdit_5.text()) != 0) and (self.lineEdit_5.text() != "0"):
                                            if (self.comboBox_4.currentIndex() == 1):
                                                tosbaga.penup()
                                                cizim.konum = [-170, -145]
                                                tosbaga.pendown()
                                                if (len(self.lineEdit_3.text()) != 0) and (
                                                    self.lineEdit_3.text() != "0"):
                                                    if (self.comboBox_2.currentIndex() == 0):
                                                        cizim.size = 1
                                                    else:
                                                        cizim.size = 2
                                                else:
                                                    cizim.size = 1
                                                cizim.toplayici(tosbaga)
                                                tosbaga.left(90)
                                                tosbaga.forward(225)
                                                tosbaga.right(90)
                                                tosbaga.forward(45)
                                            else:
                                                tosbaga.penup()
                                                cizim.konum = [-170, -195]
                                                tosbaga.pendown()
                                                if (len(self.lineEdit_3.text()) != 0) and (
                                                    self.lineEdit_3.text() != "0"):
                                                    if (self.comboBox_2.currentIndex() == 0):
                                                        cizim.size = 0
                                                    else:
                                                        cizim.size = 1
                                                else:
                                                    cizim.size = 0
                                                cizim.toplayici(tosbaga)
                                                tosbaga.left(90)
                                                tosbaga.forward(225)
                                                tosbaga.right(90)
                                                tosbaga.forward(45)
                                        else:
                                            tosbaga.penup()
                                            cizim.konum = [-170, -195]
                                            tosbaga.pendown()
                                            if (len(self.lineEdit_3.text()) != 0) and (self.lineEdit_3.text() != "0"):
                                                if (self.comboBox_2.currentIndex() == 0):
                                                    cizim.size = 0
                                                else:
                                                    cizim.size = 1
                                            else:
                                                cizim.size = 0
                                            cizim.toplayici(tosbaga)
                                            tosbaga.left(90)
                                            tosbaga.forward(225)
                                            tosbaga.right(90)
                                            tosbaga.forward(45)
                                    else:
                                        if (self.comboBox_3.currentIndex() == 0):
                                            if (len(self.lineEdit_5.text()) != 0) and (self.lineEdit_5.text() != "0"):
                                                if (self.comboBox_4.currentIndex() == 1):
                                                    tosbaga.penup()
                                                    cizim.konum = [-170, -145]
                                                    tosbaga.pendown()
                                                    if (len(self.lineEdit_3.text()) != 0) and (
                                                                self.lineEdit_3.text() != "0"):
                                                        if (self.comboBox_2.currentIndex() == 0):
                                                            cizim.size = 2
                                                        else:
                                                            cizim.size = 3
                                                    else:
                                                        cizim.size = 2
                                                    cizim.toplayici(tosbaga)
                                                    tosbaga.forward(20)
                                                    tosbaga.left(90)
                                                    tosbaga.forward(175)
                                                    tosbaga.right(90)
                                                    tosbaga.forward(25)
                                                else:
                                                    tosbaga.penup()
                                                    cizim.konum = [-170, -145]
                                                    tosbaga.pendown()
                                                    if (len(self.lineEdit_3.text()) != 0) and (
                                                                self.lineEdit_3.text() != "0"):
                                                        if (self.comboBox_2.currentIndex() == 0):
                                                            cizim.size = 1
                                                        else:
                                                            cizim.size = 2
                                                    else:
                                                        cizim.size = 1
                                                    cizim.toplayici(tosbaga)
                                                    tosbaga.forward(20)
                                                    tosbaga.left(90)
                                                    tosbaga.forward(175)
                                                    tosbaga.right(90)
                                                    tosbaga.forward(25)
                                            else:
                                                tosbaga.penup()
                                                cizim.konum = [-170, -145]
                                                tosbaga.pendown()
                                                if (len(self.lineEdit_3.text()) != 0) and (
                                                    self.lineEdit_3.text() != "0"):
                                                    if (self.comboBox_2.currentIndex() == 0):
                                                        cizim.size = 1
                                                    else:
                                                        cizim.size = 2
                                                else:
                                                    cizim.size = 1
                                                cizim.toplayici(tosbaga)
                                                tosbaga.forward(20)
                                                tosbaga.left(90)
                                                tosbaga.forward(175)
                                                tosbaga.right(90)
                                                tosbaga.forward(25)
                                            cizim.konum = [69, 70]
                                            tosbaga.penup()
                                            tosbaga.setposition(cizim.konum[0], cizim.konum[1])
                                            tosbaga.pendown()
                                            tosbaga.right(90)
                                            tosbaga.forward(125)
                                            tosbaga.right(90)
                                            tosbaga.forward(255)
                                            tosbaga.left(90)
                                            tosbaga.forward(90)
                                            tosbaga.left(90)
                                            tosbaga.forward(20)
                                        else:
                                            if (len(self.lineEdit_5.text()) != 0) and (self.lineEdit_5.text() != "0"):
                                                if (self.comboBox_4.currentIndex() == 1):
                                                    tosbaga.penup()
                                                    cizim.konum = [-170, -195]
                                                    tosbaga.pendown()
                                                    if (len(self.lineEdit_3.text()) != 0) and (
                                                                self.lineEdit_3.text() != "0"):
                                                        if (self.comboBox_2.currentIndex() == 0):
                                                            cizim.size = 1
                                                        else:
                                                            cizim.size = 2
                                                    else:
                                                        cizim.size = 1
                                                    cizim.toplayici(tosbaga)
                                                    tosbaga.left(90)
                                                    tosbaga.forward(225)
                                                    tosbaga.right(90)
                                                    tosbaga.forward(45)
                                                else:
                                                    tosbaga.penup()
                                                    cizim.konum = [-170, -195]
                                                    tosbaga.pendown()
                                                    if (len(self.lineEdit_3.text()) != 0) and (
                                                                self.lineEdit_3.text() != "0"):
                                                        if (self.comboBox_2.currentIndex() == 0):
                                                            cizim.size = 0
                                                        else:
                                                            cizim.size = 1
                                                    else:
                                                        cizim.size = 0
                                                    cizim.toplayici(tosbaga)
                                                    tosbaga.left(90)
                                                    tosbaga.forward(225)
                                                    tosbaga.right(90)
                                                    tosbaga.forward(45)
                                            else:
                                                tosbaga.penup()
                                                cizim.konum = [-170, -195]
                                                tosbaga.pendown()
                                                if (len(self.lineEdit_3.text()) != 0) and (
                                                    self.lineEdit_3.text() != "0"):
                                                    if (self.comboBox_2.currentIndex() == 0):
                                                        cizim.size = 0
                                                    else:
                                                        cizim.size = 1
                                                else:
                                                    cizim.size = 0
                                                cizim.toplayici(tosbaga)
                                                tosbaga.left(90)
                                                tosbaga.forward(225)
                                                tosbaga.right(90)
                                                tosbaga.forward(45)
                                    if (len(self.lineEdit_3.text()) != 0) and (self.lineEdit_3.text() != "0"):
                                        if (self.comboBox_2.currentIndex() == 0):
                                            cizim.konum = [-100, 80]
                                            tosbaga.penup()
                                            tosbaga.setposition(cizim.konum[0], cizim.konum[1])
                                            tosbaga.pendown()
                                            tosbaga.right(90)
                                            tosbaga.forward(110)
                                            tosbaga.left(90)
                                            tosbaga.forward(205)
                                        else:
                                            cizim.konum = [-100, 80]
                                            tosbaga.penup()
                                            tosbaga.setposition(cizim.konum[0], cizim.konum[1])
                                            tosbaga.pendown()
                                            tosbaga.right(90)
                                            tosbaga.forward(95)
                                            tosbaga.right(90)
                                            tosbaga.forward(120)
                                            tosbaga.left(90)
                                            tosbaga.forward(230)
                                            tosbaga.left(90)
                                            tosbaga.forward(51)
                                else:
                                    if (len(self.lineEdit_4.text()) == 0) or (self.lineEdit_4.text() == "0"):
                                        if (len(self.lineEdit_5.text()) != 0) and (self.lineEdit_5.text() != "0"):
                                            if (self.comboBox_4.currentIndex() == 1):
                                                tosbaga.penup()
                                                cizim.konum = [-170, -145]
                                                tosbaga.pendown()
                                                if (len(self.lineEdit_3.text()) != 0) and (
                                                    self.lineEdit_3.text() != "0"):
                                                    if (self.comboBox_2.currentIndex() == 0):
                                                        cizim.size = 1
                                                    else:
                                                        cizim.size = 2
                                                else:
                                                    cizim.size = 1
                                                cizim.toplayici(tosbaga)
                                                tosbaga.left(90)
                                                tosbaga.forward(225)
                                                tosbaga.right(90)
                                                tosbaga.forward(45)
                                            else:
                                                tosbaga.penup()
                                                cizim.konum = [-170, -195]
                                                tosbaga.pendown()
                                                if (len(self.lineEdit_3.text()) != 0) and (
                                                    self.lineEdit_3.text() != "0"):
                                                    if (self.comboBox_2.currentIndex() == 0):
                                                        cizim.size = 0
                                                    else:
                                                        cizim.size = 1
                                                else:
                                                    cizim.size = 0
                                                cizim.toplayici(tosbaga)
                                                tosbaga.left(90)
                                                tosbaga.forward(225)
                                                tosbaga.right(90)
                                                tosbaga.forward(45)
                                        else:
                                            tosbaga.penup()
                                            cizim.konum = [-170, -195]
                                            tosbaga.pendown()
                                            if (len(self.lineEdit_3.text()) != 0) and (self.lineEdit_3.text() != "0"):
                                                if (self.comboBox_2.currentIndex() == 0):
                                                    cizim.size = 0
                                                else:
                                                    cizim.size = 1
                                            else:
                                                cizim.size = 0
                                            cizim.toplayici(tosbaga)
                                            tosbaga.left(90)
                                            tosbaga.forward(225)
                                            tosbaga.right(90)
                                            tosbaga.forward(45)
                                    else:
                                        if (self.comboBox_3.currentIndex() == 0):
                                            if (len(self.lineEdit_5.text()) != 0) and (self.lineEdit_5.text() != "0"):
                                                if (self.comboBox_4.currentIndex() == 1):
                                                    tosbaga.penup()
                                                    cizim.konum = [-170, -145]
                                                    tosbaga.pendown()
                                                    if (len(self.lineEdit_3.text()) != 0) and (
                                                                self.lineEdit_3.text() != "0"):
                                                        if (self.comboBox_2.currentIndex() == 0):
                                                            cizim.size = 1
                                                        else:
                                                            cizim.size = 2
                                                    else:
                                                        cizim.size = 1
                                                    cizim.toplayici(tosbaga)
                                                    tosbaga.forward(20)
                                                    tosbaga.left(90)
                                                    tosbaga.forward(175)
                                                    tosbaga.right(90)
                                                    tosbaga.forward(25)
                                                else:
                                                    tosbaga.penup()
                                                    cizim.konum = [-170, -145]
                                                    tosbaga.pendown()
                                                    if (len(self.lineEdit_3.text()) != 0) and (
                                                                self.lineEdit_3.text() != "0"):
                                                        if (self.comboBox_2.currentIndex() == 0):
                                                            cizim.size = 0
                                                        else:
                                                            cizim.size = 1
                                                    else:
                                                        cizim.size = 0
                                                    cizim.toplayici(tosbaga)
                                                    tosbaga.forward(20)
                                                    tosbaga.left(90)
                                                    tosbaga.forward(175)
                                                    tosbaga.right(90)
                                                    tosbaga.forward(25)
                                            else:
                                                tosbaga.penup()
                                                cizim.konum = [-170, -145]
                                                tosbaga.pendown()
                                                if (len(self.lineEdit_3.text()) != 0) and (self.lineEdit_3.text() != "0"):
                                                    if (self.comboBox_2.currentIndex() == 0):
                                                        cizim.size = 0

                                                    else:
                                                        cizim.size = 1
                                                else:
                                                    cizim.size = 0
                                                cizim.toplayici(tosbaga)
                                                tosbaga.forward(20)
                                                tosbaga.left(90)
                                                tosbaga.forward(175)
                                                tosbaga.right(90)
                                                tosbaga.forward(25)
                                            cizim.konum = [69, 70]
                                            tosbaga.penup()
                                            tosbaga.setposition(cizim.konum[0], cizim.konum[1])
                                            tosbaga.pendown()
                                            tosbaga.right(90)
                                            tosbaga.forward(125)
                                            tosbaga.right(90)
                                            tosbaga.forward(255)
                                            tosbaga.left(90)
                                            tosbaga.forward(90)
                                            tosbaga.left(90)
                                            tosbaga.forward(20)
                                        else:
                                            if (len(self.lineEdit_5.text()) != 0) and (self.lineEdit_5.text() != "0"):
                                                if (self.comboBox_4.currentIndex() == 1):
                                                    tosbaga.penup()
                                                    cizim.konum = [-170, -195]
                                                    tosbaga.pendown()
                                                    if (len(self.lineEdit_3.text()) != 0) and (
                                                                self.lineEdit_3.text() != "0"):
                                                        if (self.comboBox_2.currentIndex() == 0):
                                                            cizim.size = 0
                                                        else:
                                                            cizim.size = 1
                                                    else:
                                                        cizim.size = 0
                                                    cizim.toplayici(tosbaga)
                                                    tosbaga.left(90)
                                                    tosbaga.forward(225)
                                                    tosbaga.right(90)
                                                    tosbaga.forward(45)
                                                else:
                                                    tosbaga.penup()
                                                    cizim.konum = [-170, -195]
                                                    tosbaga.pendown()
                                                    if (len(self.lineEdit_3.text()) != 0) and (
                                                        self.lineEdit_3.text() != "0"):
                                                        if (self.comboBox_2.currentIndex() == 1):
                                                            cizim.size = 0
                                                            cizim.toplayici(tosbaga)
                                                            tosbaga.left(90)
                                                            tosbaga.forward(225)
                                                            tosbaga.right(90)
                                                            tosbaga.forward(45)
                                            else:
                                                tosbaga.penup()
                                                cizim.konum = [-170, -195]
                                                tosbaga.pendown()
                                                if (len(self.lineEdit_3.text()) != 0) and (self.lineEdit_3.text() != "0"):
                                                    if (self.comboBox_2.currentIndex() == 1):
                                                        cizim.size = 0
                                                        cizim.toplayici(tosbaga)
                                                        tosbaga.left(90)
                                                        tosbaga.forward(225)
                                                        tosbaga.right(90)
                                                        tosbaga.forward(45)
                                                else:
                                                    cizim.size = 0
                                                    cizim.toplayici(tosbaga)
                                                    tosbaga.left(90)
                                                    tosbaga.forward(225)
                                                    tosbaga.right(90)
                                                    tosbaga.forward(45)

                                    if (len(self.lineEdit_3.text()) != 0) and (self.lineEdit_3.text() != "0"):
                                        if (self.comboBox_2.currentIndex() == 0):
                                            cizim.konum = [-100, 80]
                                            tosbaga.penup()
                                            tosbaga.setposition(cizim.konum[0], cizim.konum[1])
                                            tosbaga.pendown()
                                            tosbaga.right(90)
                                            tosbaga.forward(110)
                                            tosbaga.left(90)
                                            tosbaga.forward(205)
                                        else:
                                            cizim.konum = [-100, 80]
                                            tosbaga.penup()
                                            tosbaga.setposition(cizim.konum[0], cizim.konum[1])
                                            tosbaga.pendown()
                                            tosbaga.right(90)
                                            tosbaga.forward(95)
                                            tosbaga.right(90)
                                            tosbaga.forward(120)
                                            tosbaga.left(90)
                                            tosbaga.forward(180)
                                            tosbaga.left(90)
                                            tosbaga.forward(51)
                            else:
                                if (len(self.lineEdit_4.text()) != 0) and (self.lineEdit_4.text() != "0"):
                                    if (self.comboBox_3.currentIndex() == 0):
                                        if (len(self.lineEdit_5.text()) != 0) and (self.lineEdit_5.text() != "0"):
                                            if (self.comboBox_4.currentIndex() == 1):
                                                tosbaga.penup()
                                                cizim.konum = [-170, -145]
                                                tosbaga.pendown()
                                                if (len(self.lineEdit_3.text()) != 0) and (
                                                    self.lineEdit_3.text() != "0"):
                                                    if (self.comboBox_2.currentIndex() == 0):
                                                        cizim.size = 2
                                                    else:
                                                        cizim.size = 3
                                                else:
                                                    cizim.size = 2
                                                cizim.toplayici(tosbaga)
                                                tosbaga.forward(20)
                                                tosbaga.left(90)
                                                tosbaga.forward(175)
                                                tosbaga.right(90)
                                                tosbaga.forward(25)
                                            else:
                                                tosbaga.penup()
                                                cizim.konum = [-170, -145]
                                                tosbaga.pendown()
                                                if (len(self.lineEdit_3.text()) != 0) and (
                                                    self.lineEdit_3.text() != "0"):
                                                    if (self.comboBox_2.currentIndex() == 0):
                                                        cizim.size = 1
                                                    else:
                                                        cizim.size = 2
                                                else:
                                                    cizim.size = 1
                                                cizim.toplayici(tosbaga)
                                                tosbaga.forward(20)
                                                tosbaga.left(90)
                                                tosbaga.forward(175)
                                                tosbaga.right(90)
                                                tosbaga.forward(25)
                                        else:
                                            tosbaga.penup()
                                            cizim.konum = [-170, -145]
                                            tosbaga.pendown()
                                            if (len(self.lineEdit_3.text()) != 0) and (self.lineEdit_3.text() != "0"):
                                                if (self.comboBox_2.currentIndex() == 0):
                                                    cizim.size = 1
                                                else:
                                                    cizim.size = 2
                                            else:
                                                cizim.size = 1
                                            cizim.toplayici(tosbaga)
                                            tosbaga.forward(20)
                                            tosbaga.left(90)
                                            tosbaga.forward(175)
                                            tosbaga.right(90)
                                            tosbaga.forward(25)
                                        cizim.konum = [69, 70]
                                        tosbaga.penup()
                                        tosbaga.setposition(cizim.konum[0], cizim.konum[1])
                                        tosbaga.pendown()
                                        tosbaga.right(90)
                                        tosbaga.forward(125)
                                        tosbaga.right(90)
                                        tosbaga.forward(255)
                                        tosbaga.left(90)
                                        tosbaga.forward(90)
                                        tosbaga.left(90)
                                        tosbaga.forward(20)
                                        if (len(self.lineEdit_3.text()) != 0) and (self.lineEdit_3.text() != "0"):
                                            if (self.comboBox_2.currentIndex() == 0):
                                                cizim.konum = [-100, 80]
                                                tosbaga.penup()
                                                tosbaga.setposition(cizim.konum[0], cizim.konum[1])
                                                tosbaga.pendown()
                                                tosbaga.right(90)
                                                tosbaga.forward(110)
                                                tosbaga.left(90)
                                                tosbaga.forward(205)

                                            else:
                                                cizim.konum = [-100, 80]
                                                tosbaga.penup()
                                                tosbaga.setposition(cizim.konum[0], cizim.konum[1])
                                                tosbaga.pendown()
                                                tosbaga.right(90)
                                                tosbaga.forward(95)
                                                tosbaga.right(90)
                                                tosbaga.forward(120)
                                                tosbaga.left(90)
                                                tosbaga.forward(230)
                                                tosbaga.left(90)
                                                tosbaga.forward(51)

                                    else:
                                        if (len(self.lineEdit_5.text()) != 0) and (self.lineEdit_5.text() != "0"):
                                            if (self.comboBox_4.currentIndex() == 1):
                                                tosbaga.penup()
                                                cizim.konum = [-170, -145]
                                                tosbaga.pendown()
                                                if (len(self.lineEdit_3.text()) != 0) and (
                                                    self.lineEdit_3.text() != "0"):
                                                    if (self.comboBox_2.currentIndex() == 0):
                                                        cizim.size = 1
                                                    else:
                                                        cizim.size = 2
                                                else:
                                                    cizim.size = 1
                                                cizim.toplayici(tosbaga)
                                                tosbaga.left(90)
                                                tosbaga.forward(175)
                                                tosbaga.right(90)
                                                tosbaga.forward(45)
                                            else:
                                                tosbaga.penup()
                                                cizim.konum = [-170, -195]
                                                tosbaga.pendown()
                                                if (len(self.lineEdit_3.text()) != 0) and (
                                                    self.lineEdit_3.text() != "0"):
                                                    if (self.comboBox_2.currentIndex() == 0):
                                                        cizim.size = 0
                                                    else:
                                                        cizim.size = 1
                                                else:
                                                    cizim.size = 0
                                                cizim.toplayici(tosbaga)
                                                tosbaga.left(90)
                                                tosbaga.forward(175)
                                                tosbaga.right(90)
                                                tosbaga.forward(45)
                                        else:
                                            tosbaga.penup()
                                            cizim.konum = [-170, -195]
                                            tosbaga.pendown()
                                            if (len(self.lineEdit_3.text()) != 0) and (self.lineEdit_3.text() != "0"):
                                                if (self.comboBox_2.currentIndex() == 0):
                                                    cizim.size = 0
                                                else:
                                                    cizim.size = 1
                                            else:
                                                cizim.size = 0
                                            cizim.toplayici(tosbaga)
                                            tosbaga.left(90)
                                            tosbaga.forward(175)
                                            tosbaga.right(90)
                                            tosbaga.forward(45)
                                        if (len(self.lineEdit_3.text()) != 0) and (self.lineEdit_3.text() != "0"):
                                            if (self.comboBox_2.currentIndex() == 0):
                                                cizim.konum = [-100, 80]
                                                tosbaga.penup()
                                                tosbaga.setposition(cizim.konum[0], cizim.konum[1])
                                                tosbaga.pendown()
                                                tosbaga.right(90)
                                                tosbaga.forward(110)
                                                tosbaga.left(90)
                                                tosbaga.forward(205)
                                            else:
                                                cizim.konum = [-100, 80]
                                                tosbaga.penup()
                                                tosbaga.setposition(cizim.konum[0], cizim.konum[1])
                                                tosbaga.pendown()
                                                tosbaga.right(90)
                                                tosbaga.forward(95)
                                                tosbaga.right(90)
                                                tosbaga.forward(120)
                                                tosbaga.left(90)
                                                tosbaga.forward(180)
                                                tosbaga.left(90)
                                                tosbaga.forward(51)
#---------------------------------------------------------------------------------------şeklin sonundaki toplayıcı çizimi için--------
                            cizim.konum = [105, 70]
                            if ((len(self.lineEdit_2.text()) != 0) and (self.lineEdit_2.text() != "0")) or (
                                        (len(self.lineEdit_4.text()) != 0) and (self.lineEdit_4.text() != "0")):
                                if ((self.comboBox.currentIndex() == 0) or (self.comboBox_3.currentIndex() == 0)):

                                    if ((len(self.lineEdit_3.text()) != 0) and (self.lineEdit_3.text() != "0")):
                                        if (self.comboBox_2.currentIndex() == 0):

                                            if ((len(self.lineEdit_5.text()) != 0) and (self.lineEdit_5.text() != "0")):
                                                if (self.comboBox_4.currentIndex() == 0):
                                                    cizim.size = 3
                                                    cizim.toplayici(tosbaga)
                                                else:
                                                    cizim.size = 2
                                                    cizim.toplayici(tosbaga)
                                            else:
                                                cizim.size = 2
                                                cizim.toplayici(tosbaga)
                                        else:
                                            if ((len(self.lineEdit_5.text()) != 0) and (self.lineEdit_5.text() != "0")):
                                                if (self.comboBox_4.currentIndex() == 0):

                                                    cizim.size = 2
                                                    cizim.toplayici(tosbaga)
                                                else:
                                                    cizim.size = 1
                                                    cizim.toplayici(tosbaga)
                                            else:
                                                cizim.size = 1
                                                cizim.toplayici(tosbaga)
                                    else:
                                        if ((len(self.lineEdit_5.text()) != 0) and (self.lineEdit_5.text() != "0")):
                                            if (self.comboBox_4.currentIndex() == 0):

                                                cizim.size = 2
                                                cizim.toplayici(tosbaga)
                                            else:
                                                cizim.size = 1
                                                cizim.toplayici(tosbaga)
                                        else:
                                            cizim.size = 1
                                            cizim.toplayici(tosbaga)
                                else:
                                    if ((len(self.lineEdit_3.text()) != 0) and (self.lineEdit_3.text() != "0")):
                                        if (self.comboBox_2.currentIndex() == 0):

                                            if ((len(self.lineEdit_5.text()) != 0) and (self.lineEdit_5.text() != "0")):
                                                cizim.size = 2
                                                cizim.toplayici(tosbaga)
                                            else:
                                                cizim.size = 1
                                                cizim.toplayici(tosbaga)
                                        else:
                                            if ((len(self.lineEdit_5.text()) != 0) and (self.lineEdit_5.text() != "0")):
                                                if (self.comboBox_4.currentIndex() == 0):

                                                    cizim.size = 2
                                                    cizim.toplayici(tosbaga)
                                                else:
                                                    cizim.size = 1
                                                    cizim.toplayici(tosbaga)
                                            else:
                                                cizim.size = 1
                                                cizim.toplayici(tosbaga)
                            else:
                                if ((len(self.lineEdit_5.text()) != 0) and (self.lineEdit_5.text() != "0")):
                                    if (self.comboBox_4.currentIndex() == 0):

                                        cizim.size = 1
                                        cizim.toplayici(tosbaga)
                                    else:
                                        cizim.size = 0
                                        cizim.toplayici(tosbaga)
                                else:
                                    cizim.size = 0
                                    cizim.toplayici(tosbaga)

                            cizim.konum = [-400, 100]
                            tosbaga.penup()
                            tosbaga.setposition(cizim.konum[0], cizim.konum[1])
                            tosbaga.pendown()
                            tosbaga.right(90)
                            tosbaga.forward(420)
                            tosbaga.left(90)
                            tosbaga.forward(737)
                            tosbaga.left(90)
                            tosbaga.forward(380)

        wn.mainloop()
#------------------------------------------------------------------------------------------------------------------------------
def isaretKontrol(test):
    durum = True
    for i in range(0, len(test)):
        if (test[i] == "-" or test[i] == "+"):
            durum = False
            break
    return durum

def ilkkontrol(test):
    durum = True
    for i in range(1, len(test)):
        if (test[i] == "-" or test[i] == "+"):
            durum = False
            break;
    return durum

def harfkontrol(test):
    durum = True
    sayilar = "+-.0123456789"
    noktasay = 0
    for i in range(0, len(test)):
        for j in range(0, len(sayilar)):
            if(test[i] == "."):
                noktasay = noktasay + 1
                if(noktasay <= 1):
                    break
                elif(noktasay == 2):
                    durum = False
                    break
            if (test[i] == sayilar[j]):
                break
            elif ((test[i] != sayilar[j]) and (j == (len(sayilar)) - 1)):
                durum = False
                break
            elif (test[i] != sayilar[j]):
                continue
        if (not durum):
            break
    return durum
#------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())