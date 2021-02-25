import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_PMexample import Ui_MainWindow 

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

# add functionality



MainWindow.show()
sys.exit(app.exec_())

