import sys
from PyQt5 import QtWidgets, QtGui, QtCore,  uic

from Panel2 import Ui_MainWindow
import rsc_rc

counter = 0
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.lowBeamsBtn.clicked.connect(self.lowBeamIconChange)
        self.highBeamsBtn.clicked.connect(self.highBeamIconChange)
        self.fogLigghtsBtn.clicked.connect(self.fogLightIconChange)
        self.battery12Btn.clicked.connect(self.battery12IconChange)
        self.wheelPumpBtn.clicked.connect(self.wheelsPumpIconChange)
        self.chargePowerBatBtn.clicked.connect(self.chargePowerBatIconChange)
        self.powerBatStateBtn.clicked.connect(self.powerBatStateIconChange)



        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(10)

    def progress(self):
        #global counter
        value = self.speedSlider.value()
        angle = self.speedSlider.value()

        self.angleTangValue(angle)
        self.angleRollValue(angle)
        self.speedValue(value)
        self.speed.setText(str(round(self.speedSlider.value() * 0.4)))
        self.speed_2.setText(str(round(angle / 3)))
        self.speed_3.setText(str(round(angle / 3)))

        #if counter > 100:
        #    self.timer.stop()

        #counter += 1


    def lowBeamIconChange(self):
        self.lowBeams.setPixmap(QtGui.QPixmap("icons/low_beam_on.png"))

    def highBeamIconChange(self):
        self.highBeams.setPixmap(QtGui.QPixmap("icons/high_beam_on.png"))

    def fogLightIconChange(self):
        self.fogLights.setPixmap(QtGui.QPixmap("icons/fog_light_on.png"))

    def battery12IconChange(self):
        self.battery12.setPixmap(QtGui.QPixmap("icons/battery_12V_state_discharge.png"))

    def wheelsPumpIconChange(self):
        self.wheelsPump.setPixmap(QtGui.QPixmap("icons/wheels_pump_on.png"))

    def chargePowerBatIconChange(self):
        self.chargePowerBat.setPixmap(QtGui.QPixmap("icons/charge_power_bat_on.png"))

    def powerBatStateIconChange(self):
        self.powerBatState.setPixmap(QtGui.QPixmap("icons/power_bat_state_20_percent.png"))


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

    def angleTangValue(self, angle):
        styleSheetAngle = """
        QWidget{
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:{ANGLE}, stop:0.499 rgba(227, 227, 227, 255), stop:0.5 rgba(0, 0, 0, 255));
            border-radius: 115px;
        }
        """

        angleValue = str(angle/3)
        newAngleStyleSheet = styleSheetAngle.replace("{ANGLE}", angleValue)

        self.tangAnimation.setStyleSheet(newAngleStyleSheet)

    def angleRollValue(self, angle):
        styleSheetAngle = """
        QWidget{
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:{ANGLE}, stop:0.499 rgba(227, 227, 227, 255), stop:0.5 rgba(0, 0, 0, 255));
            border-radius: 115px;
        }
        """

        angleValue = str(360 -(angle/3))
        newAngleStyleSheet = styleSheetAngle.replace("{ANGLE}", angleValue)

        self.rollAnimation.setStyleSheet(newAngleStyleSheet)


app = QtWidgets.QApplication(sys.argv)





#window = uic.loadUi("Panel.ui")
window  = MainWindow()
window.show()
app.exec()