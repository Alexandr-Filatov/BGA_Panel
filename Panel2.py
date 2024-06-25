# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Panel2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 749)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.Panel = QtWidgets.QWidget()
        self.Panel.setStyleSheet("")
        self.Panel.setObjectName("Panel")
        self.widget_3 = QtWidgets.QWidget(self.Panel)
        self.widget_3.setGeometry(QtCore.QRect(630, 30, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 25px;")
        self.widget_3.setObjectName("widget_3")
        self.fogLights = QtWidgets.QLabel(self.widget_3)
        self.fogLights.setGeometry(QtCore.QRect(5, 5, 60, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fogLights.sizePolicy().hasHeightForWidth())
        self.fogLights.setSizePolicy(sizePolicy)
        self.fogLights.setMinimumSize(QtCore.QSize(40, 40))
        self.fogLights.setMaximumSize(QtCore.QSize(60, 60))
        self.fogLights.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"padding: 5px;")
        self.fogLights.setText("")
        self.fogLights.setPixmap(QtGui.QPixmap("icons/fog_ligfht_off.png"))
        self.fogLights.setScaledContents(True)
        self.fogLights.setObjectName("fogLights")
        self.rollBase = QtWidgets.QWidget(self.Panel)
        self.rollBase.setGeometry(QtCore.QRect(750, 0, 250, 250))
        self.rollBase.setStyleSheet("border-radius: 125px;\n"
"background-color: rgb(255, 255, 255);")
        self.rollBase.setObjectName("rollBase")
        self.rollAnimation = QtWidgets.QWidget(self.rollBase)
        self.rollAnimation.setGeometry(QtCore.QRect(10, 10, 230, 230))
        self.rollAnimation.setStyleSheet("QWidget{\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.499 rgba(227, 227, 227, 255), stop:0.5 rgba(0, 0, 0, 255));\n"
"border-radius: 115px;\n"
"}")
        self.rollAnimation.setObjectName("rollAnimation")
        self.label_2 = QtWidgets.QLabel(self.rollAnimation)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 130, 130))
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border-radius: 20px;\n"
"padding: 8px;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icons/BGA_front.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.speed_3 = QtWidgets.QLabel(self.rollAnimation)
        self.speed_3.setGeometry(QtCore.QRect(75, 180, 80, 50))
        self.speed_3.setStyleSheet("\n"
"font: 30pt \"BankGothic Lt BT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.speed_3.setAlignment(QtCore.Qt.AlignCenter)
        self.speed_3.setObjectName("speed_3")
        self.rollCanvas = QtWidgets.QWidget(self.rollBase)
        self.rollCanvas.setGeometry(QtCore.QRect(5, 5, 240, 240))
        self.rollCanvas.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 120px;")
        self.rollCanvas.setObjectName("rollCanvas")
        self.rollCanvas.raise_()
        self.rollAnimation.raise_()
        self.widget_5 = QtWidgets.QWidget(self.Panel)
        self.widget_5.setGeometry(QtCore.QRect(50, 300, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 25px;")
        self.widget_5.setObjectName("widget_5")
        self.wheelsPump = QtWidgets.QLabel(self.widget_5)
        self.wheelsPump.setGeometry(QtCore.QRect(5, 5, 60, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wheelsPump.sizePolicy().hasHeightForWidth())
        self.wheelsPump.setSizePolicy(sizePolicy)
        self.wheelsPump.setMinimumSize(QtCore.QSize(40, 40))
        self.wheelsPump.setMaximumSize(QtCore.QSize(60, 60))
        self.wheelsPump.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"padding: 8px;")
        self.wheelsPump.setText("")
        self.wheelsPump.setPixmap(QtGui.QPixmap("icons/wheel_pump_off.png"))
        self.wheelsPump.setScaledContents(True)
        self.wheelsPump.setObjectName("wheelsPump")
        self.widget_7 = QtWidgets.QWidget(self.Panel)
        self.widget_7.setGeometry(QtCore.QRect(880, 390, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 25px;")
        self.widget_7.setObjectName("widget_7")
        self.powerBatState = QtWidgets.QLabel(self.widget_7)
        self.powerBatState.setGeometry(QtCore.QRect(5, 5, 60, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerBatState.sizePolicy().hasHeightForWidth())
        self.powerBatState.setSizePolicy(sizePolicy)
        self.powerBatState.setMinimumSize(QtCore.QSize(40, 40))
        self.powerBatState.setMaximumSize(QtCore.QSize(60, 60))
        self.powerBatState.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"padding: 8px;")
        self.powerBatState.setText("")
        self.powerBatState.setPixmap(QtGui.QPixmap("icons/power_bat_state_80_percent.png"))
        self.powerBatState.setScaledContents(True)
        self.powerBatState.setObjectName("powerBatState")
        self.widget_2 = QtWidgets.QWidget(self.Panel)
        self.widget_2.setGeometry(QtCore.QRect(465, 30, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 25px;")
        self.widget_2.setObjectName("widget_2")
        self.highBeams = QtWidgets.QLabel(self.widget_2)
        self.highBeams.setGeometry(QtCore.QRect(5, 5, 60, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.highBeams.sizePolicy().hasHeightForWidth())
        self.highBeams.setSizePolicy(sizePolicy)
        self.highBeams.setMinimumSize(QtCore.QSize(40, 40))
        self.highBeams.setMaximumSize(QtCore.QSize(60, 60))
        self.highBeams.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"padding: 5px;")
        self.highBeams.setText("")
        self.highBeams.setPixmap(QtGui.QPixmap("icons/high_beam_off.png"))
        self.highBeams.setScaledContents(True)
        self.highBeams.setObjectName("highBeams")
        self.layoutWidget = QtWidgets.QWidget(self.Panel)
        self.layoutWidget.setGeometry(QtCore.QRect(13, 600, 971, 72))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.speedSlider = QtWidgets.QSlider(self.layoutWidget)
        self.speedSlider.setOrientation(QtCore.Qt.Vertical)
        self.speedSlider.setObjectName("speedSlider")
        self.horizontalLayout.addWidget(self.speedSlider)
        self.lowBeamsBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.lowBeamsBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.lowBeamsBtn.setObjectName("lowBeamsBtn")
        self.horizontalLayout.addWidget(self.lowBeamsBtn)
        self.highBeamsBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.highBeamsBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.highBeamsBtn.setObjectName("highBeamsBtn")
        self.horizontalLayout.addWidget(self.highBeamsBtn)
        self.fogLigghtsBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.fogLigghtsBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.fogLigghtsBtn.setObjectName("fogLigghtsBtn")
        self.horizontalLayout.addWidget(self.fogLigghtsBtn)
        self.battery12Btn = QtWidgets.QPushButton(self.layoutWidget)
        self.battery12Btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.battery12Btn.setObjectName("battery12Btn")
        self.horizontalLayout.addWidget(self.battery12Btn)
        self.wheelPumpBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.wheelPumpBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.wheelPumpBtn.setObjectName("wheelPumpBtn")
        self.horizontalLayout.addWidget(self.wheelPumpBtn)
        self.chargePowerBatBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.chargePowerBatBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.chargePowerBatBtn.setObjectName("chargePowerBatBtn")
        self.horizontalLayout.addWidget(self.chargePowerBatBtn)
        self.powerBatStateBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.powerBatStateBtn.setEnabled(True)
        self.powerBatStateBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.powerBatStateBtn.setObjectName("powerBatStateBtn")
        self.horizontalLayout.addWidget(self.powerBatStateBtn)
        self.widget_4 = QtWidgets.QWidget(self.Panel)
        self.widget_4.setGeometry(QtCore.QRect(880, 480, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 25px;")
        self.widget_4.setObjectName("widget_4")
        self.battery12 = QtWidgets.QLabel(self.widget_4)
        self.battery12.setGeometry(QtCore.QRect(5, 5, 60, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.battery12.sizePolicy().hasHeightForWidth())
        self.battery12.setSizePolicy(sizePolicy)
        self.battery12.setMinimumSize(QtCore.QSize(40, 40))
        self.battery12.setMaximumSize(QtCore.QSize(60, 60))
        self.battery12.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"padding: 8px;")
        self.battery12.setText("")
        self.battery12.setPixmap(QtGui.QPixmap("icons/battery_12V_state_OK.png"))
        self.battery12.setScaledContents(True)
        self.battery12.setObjectName("battery12")
        self.widget = QtWidgets.QWidget(self.Panel)
        self.widget.setGeometry(QtCore.QRect(300, 30, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 25px;")
        self.widget.setObjectName("widget")
        self.lowBeams = QtWidgets.QLabel(self.widget)
        self.lowBeams.setGeometry(QtCore.QRect(5, 5, 60, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lowBeams.sizePolicy().hasHeightForWidth())
        self.lowBeams.setSizePolicy(sizePolicy)
        self.lowBeams.setMinimumSize(QtCore.QSize(40, 40))
        self.lowBeams.setMaximumSize(QtCore.QSize(60, 60))
        self.lowBeams.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"padding:5px;")
        self.lowBeams.setText("")
        self.lowBeams.setPixmap(QtGui.QPixmap("icons/low_beam_off.png"))
        self.lowBeams.setScaledContents(True)
        self.lowBeams.setAlignment(QtCore.Qt.AlignCenter)
        self.lowBeams.setObjectName("lowBeams")
        self.widget_6 = QtWidgets.QWidget(self.Panel)
        self.widget_6.setGeometry(QtCore.QRect(880, 300, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 25px;")
        self.widget_6.setObjectName("widget_6")
        self.chargePowerBat = QtWidgets.QLabel(self.widget_6)
        self.chargePowerBat.setGeometry(QtCore.QRect(5, 5, 60, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chargePowerBat.sizePolicy().hasHeightForWidth())
        self.chargePowerBat.setSizePolicy(sizePolicy)
        self.chargePowerBat.setMinimumSize(QtCore.QSize(40, 40))
        self.chargePowerBat.setMaximumSize(QtCore.QSize(60, 60))
        self.chargePowerBat.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"padding: 8px;")
        self.chargePowerBat.setText("")
        self.chargePowerBat.setPixmap(QtGui.QPixmap("icons/charge_power_bat_off.png"))
        self.chargePowerBat.setScaledContents(True)
        self.chargePowerBat.setObjectName("chargePowerBat")
        self.tangBase = QtWidgets.QWidget(self.Panel)
        self.tangBase.setGeometry(QtCore.QRect(0, 0, 250, 250))
        self.tangBase.setStyleSheet("border-radius: 125px;\n"
"background-color: rgb(255, 255, 255);")
        self.tangBase.setObjectName("tangBase")
        self.tangAnimation = QtWidgets.QWidget(self.tangBase)
        self.tangAnimation.setGeometry(QtCore.QRect(10, 10, 230, 230))
        self.tangAnimation.setStyleSheet("QWidget{\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.499 rgba(227, 227, 227, 255), stop:0.5 rgba(0, 0, 0, 255));\n"
"border-radius: 115px;\n"
"}")
        self.tangAnimation.setObjectName("tangAnimation")
        self.speed_2 = QtWidgets.QLabel(self.tangAnimation)
        self.speed_2.setGeometry(QtCore.QRect(75, 180, 80, 50))
        self.speed_2.setStyleSheet("\n"
"font: 30pt \"BankGothic Lt BT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.speed_2.setAlignment(QtCore.Qt.AlignCenter)
        self.speed_2.setObjectName("speed_2")
        self.label = QtWidgets.QLabel(self.tangAnimation)
        self.label.setGeometry(QtCore.QRect(25, 50, 180, 130))
        self.label.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border-radius: 20px;\n"
"padding: 8px;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/BGA_Side.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tangCanvas = QtWidgets.QWidget(self.tangBase)
        self.tangCanvas.setGeometry(QtCore.QRect(5, 5, 240, 240))
        self.tangCanvas.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 120px;")
        self.tangCanvas.setObjectName("tangCanvas")
        self.tangCanvas.raise_()
        self.tangAnimation.raise_()
        self.circularSpeedBase = QtWidgets.QFrame(self.Panel)
        self.circularSpeedBase.setGeometry(QtCore.QRect(300, 150, 400, 400))
        self.circularSpeedBase.setStyleSheet("background-color: rgba(255, 255, 255, 255);\n"
"border-radius: 160px;")
        self.circularSpeedBase.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularSpeedBase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularSpeedBase.setObjectName("circularSpeedBase")
        self.circularSpeedProgress = QtWidgets.QFrame(self.circularSpeedBase)
        self.circularSpeedProgress.setGeometry(QtCore.QRect(5, 5, 390, 390))
        self.circularSpeedProgress.setStyleSheet("QFrame{\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:0 rgba(170, 0, 0, 0), stop:0.00632911 rgba(0, 255, 0, 0), stop:0.998734 rgba(60, 255, 0, 255));\n"
"    border-radius:155px;\n"
"}")
        self.circularSpeedProgress.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularSpeedProgress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularSpeedProgress.setObjectName("circularSpeedProgress")
        self.circularBg = QtWidgets.QFrame(self.circularSpeedBase)
        self.circularBg.setGeometry(QtCore.QRect(5, 5, 390, 390))
        self.circularBg.setStyleSheet("QFrame{\n"
"    background-color: rgba(0, 0, 0, 255);\n"
"    border-radius:155px;\n"
"}")
        self.circularBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg.setObjectName("circularBg")
        self.container = QtWidgets.QFrame(self.circularSpeedBase)
        self.container.setGeometry(QtCore.QRect(30, 30, 340, 340))
        self.container.setStyleSheet("QFrame{\n"
"    border-radius: 130px;\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.layoutWidget_2 = QtWidgets.QWidget(self.container)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40, 40, 261, 261))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.speed = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("BankGothic Lt BT")
        font.setPointSize(68)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.speed.setFont(font)
        self.speed.setStyleSheet("font: 68pt \"BankGothic Lt BT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 255);\n"
"")
        self.speed.setAlignment(QtCore.Qt.AlignCenter)
        self.speed.setObjectName("speed")
        self.verticalLayout.addWidget(self.speed)
        self.kmH = QtWidgets.QLabel(self.layoutWidget_2)
        self.kmH.setStyleSheet("\n"
"font: 20pt \"BankGothic Lt BT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 255);\n"
"")
        self.kmH.setAlignment(QtCore.Qt.AlignCenter)
        self.kmH.setObjectName("kmH")
        self.verticalLayout.addWidget(self.kmH)
        self.kmH.raise_()
        self.speed.raise_()
        self.circularBg.raise_()
        self.circularSpeedProgress.raise_()
        self.container.raise_()
        self.tabWidget.addTab(self.Panel, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.speed_3.setText(_translate("MainWindow", "0"))
        self.lowBeamsBtn.setText(_translate("MainWindow", "Сет ближний"))
        self.highBeamsBtn.setText(_translate("MainWindow", "Свет дальний"))
        self.fogLigghtsBtn.setText(_translate("MainWindow", "Туман"))
        self.battery12Btn.setText(_translate("MainWindow", "Батарея 12"))
        self.wheelPumpBtn.setText(_translate("MainWindow", "Подкачка"))
        self.chargePowerBatBtn.setText(_translate("MainWindow", "Зарядка"))
        self.powerBatStateBtn.setText(_translate("MainWindow", "Батарея"))
        self.speed_2.setText(_translate("MainWindow", "0"))
        self.speed.setText(_translate("MainWindow", "0"))
        self.kmH.setText(_translate("MainWindow", "км/ч"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Panel), _translate("MainWindow", "Panel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Diagnostic"))
import rsc2_rc
