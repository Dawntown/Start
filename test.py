# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SalesTaxCalc(object):
    
    def setupUi(self, SalesTaxCalc):
        SalesTaxCalc.setObjectName("SalesTaxCalc")
        SalesTaxCalc.setEnabled(True)
        SalesTaxCalc.resize(262, 290)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SalesTaxCalc.sizePolicy().hasHeightForWidth())
        SalesTaxCalc.setSizePolicy(sizePolicy)
        SalesTaxCalc.setMinimumSize(QtCore.QSize(262, 290))
        SalesTaxCalc.setMaximumSize(QtCore.QSize(262, 290))
        SalesTaxCalc.setMouseTracking(False)
        SalesTaxCalc.setAcceptDrops(True)
        SalesTaxCalc.setWindowOpacity(1.0)
        
        self.centralwidget = QtWidgets.QWidget(SalesTaxCalc)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 221, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.priceLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.priceLabel.setFont(font)
        self.priceLabel.setMouseTracking(False)
        self.priceLabel.setObjectName("priceLabel")
        self.horizontalLayout.addWidget(self.priceLabel)
        
        self.priceTextEdit = QtWidgets.QTextEdit('0', self.horizontalLayoutWidget)
        self.priceTextEdit.setObjectName("priceTextEdit")
        self.horizontalLayout.addWidget(self.priceTextEdit)
        
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 70, 221, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        
        self.taxRateLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.taxRateLabel.setFont(font)
        self.taxRateLabel.setObjectName("taxRateLabel")
        self.horizontalLayout_2.addWidget(self.taxRateLabel)
        
        self.taxRateDBSpinBox = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.taxRateDBSpinBox.setMaximum(99.99)
        self.taxRateDBSpinBox.setSingleStep(1.0)
        self.taxRateDBSpinBox.setObjectName("taxRateDBSpinBox")
        self.horizontalLayout_2.addWidget(self.taxRateDBSpinBox)
        
        
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 120, 181, 25))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        
        self.calcTaxButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.calcTaxButton.setObjectName("calcTaxButton")
        self.verticalLayout.addWidget(self.calcTaxButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 160, 221, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, -20, 204, 78))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        SalesTaxCalc.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SalesTaxCalc)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 262, 21))
        self.menubar.setObjectName("menubar")
        SalesTaxCalc.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SalesTaxCalc)
        self.statusbar.setObjectName("statusbar")
        SalesTaxCalc.setStatusBar(self.statusbar)

        self.retranslateUi(SalesTaxCalc)
        QtCore.QMetaObject.connectSlotsByName(SalesTaxCalc)

    def retranslateUi(self, SalesTaxCalc):
        _translate = QtCore.QCoreApplication.translate
        SalesTaxCalc.setWindowTitle(_translate("SalesTaxCalc", "Test Tool"))
        self.priceLabel.setText(_translate("SalesTaxCalc", "Price"))
        self.taxRateLabel.setText(_translate("SalesTaxCalc", "Tax Rate"))
        self.calcTaxButton.setText(_translate("SalesTaxCalc", "Calculate"))
        self.label.setText(_translate("SalesTaxCalc", "Sales Tax Calculator"))

