import sys
from PyQt5 import QtWidgets, QtGui, QtCore,  uic

from Panel import Ui_MainWindow


counter = 0
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.icon_change)
        self.pushButton_2.clicked.connect(self.icon3_change)
        self.pushButton_3.clicked.connect(self.icon5_change)
        self.pushButton_4.clicked.connect(self.icon12_change)
        self.pushButton_5.clicked.connect(self.icon10_change)
        self.pushButton_6.clicked.connect(self.icon11_change)



        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(10)

    def progress(self):
        #global counter
        value = self.speedSlider.value()

        self.speedValue(value)
        self.speed.setText(str(round(self.speedSlider.value() * 0.4)))

        #if counter > 100:
        #    self.timer.stop()

        #counter += 1


    def icon_change(self):
        self.label.setPixmap(QtGui.QPixmap("icons/car-lights-light-svgrepo-on-com.png"))

    def icon3_change(self):
        self.label_3.setPixmap(QtGui.QPixmap("icons/car-lights-car-svgrepo-com (1).png"))

    def icon5_change(self):
        self.label_5.setPixmap(QtGui.QPixmap("icons/fog-light-fog-svgrepo-com (1).png"))

    def icon10_change(self):
        self.label_10.setPixmap(QtGui.QPixmap("icons/air-pump-pump-svgrepo-com (1).png"))

    def icon11_change(self):
        self.label_11.setPixmap(QtGui.QPixmap("icons/electric-charging-station-electric-energy-renewable-energy-svgrepo-com (2).png"))

    def icon12_change(self):
        self.label_12.setPixmap(QtGui.QPixmap("icons/battery-svgrepo-com (1).png"))


    def speedValue(self, value):
        styleSheet = """   
            QFrame{
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:0 rgba(170, 0, 0, 0), stop:0{STOP_1} rgba({COLOR_RED}, 255, 0, 0), stop:{STOP_2} rgba({COLOR_RED}, {COLOR_GREEN}, 0, 255));
                border-radius:150px;
            }
        """

        progress = (100 - value)/100.0
        progressColor = 2.55*value

        stop_1 =  str(progress - 0.001)
        color_red = str(progressColor)
        color_green = str(255 - progressColor)
        stop_2 = str(progress)

        newStyleSheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR_RED}", color_red).replace("{COLOR_GREEN}", color_green)

        self.circularSpeedProgress.setStyleSheet(newStyleSheet)

app = QtWidgets.QApplication(sys.argv)





#window = uic.loadUi("Panel.ui")
window  = MainWindow()
window.show()
app.exec()