# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:17:20 2017

@author: xchen
"""

import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "test.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calcTaxButton.clicked.connect(self.CalculateTax)
        
    def CalculateTax(self):
        self.price = int(self.priceTextEdit.toPlainText())
        self.tax = (self.taxRateDBSpinBox.value())
        self.totalPrice = self.price +((self.tax / 100)*self.price)
        self.totalPriceString = '含税总价为： ' + str(self.totalPrice)
        self.textBrowser.setText(self.totalPriceString)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())