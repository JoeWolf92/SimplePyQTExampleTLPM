import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_PMexample import Ui_MainWindow

from datetime import datetime
from ctypes import cdll,c_long, c_ulong, c_uint32,byref,create_string_buffer,c_bool,c_char_p,c_int,c_int16,c_double, sizeof, c_voidp
from TLPM import TLPM
import time

class PMexample(QtWidgets.QMainWindow):
    def __init__(self):
        super(PMexample, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.show()
    
    def initUI(self):
        self.ui.powerButton.clicked.connect(self.clickedPowerButton)

    def clickedPowerButton(self):
        tlPM = TLPM()
        deviceCount = c_uint32()
        tlPM.findRsrc(byref(deviceCount))
        resourceName = create_string_buffer(1024)

        for i in range(0, deviceCount.value):
            tlPM.getRsrcName(c_int(i), resourceName)
            break

        tlPM.open(resourceName, c_bool(True), c_bool(True))

        message = create_string_buffer(1024)
        tlPM.getCalibrationMsg(message)
        power = c_double()
        tlPM.measPower(byref(power))
        tlPM.close()
        
        self.ui.powerLabel.setText(str(power.value))
        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = PMexample()
    MainWindow.show()
    sys.exit(app.exec_())
