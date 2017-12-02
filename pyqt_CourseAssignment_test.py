# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:17:20 2017

@author: xchen
"""

import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QStringListModel
from pyqt_CA_SplashScreen import SplashScreen

qtCreatorFile = "CourseAssignment.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.loadedPicsList = []
        self.slcdItems = []
        self.showingPicIndex = 0
        self.picFrame = [825, 550]
        
        self.loadPicBtn.clicked.connect(self.LoadFile)
        self.picResourseListView.clicked.connect(self.SlctItems)
        self.clearPicBtn.clicked.connect(self.ClearFile)
        self.checkPicBtn.clicked.connect(self.ShowPic)
        self.deletePicBtn.clicked.connect(self.DltPic)
        self.closePicBtn.clicked.connect(self.ClsPic)
        
    def FreshPRListView(self):
        strmodel = QStringListModel()
        strmodel.setStringList(self.loadedPicsList)
        self.picResourseListView.setModel(strmodel)
        self.picResourseListView.show()
        
        
    def LoadFile(self):
        loadPics, ok = QFileDialog.getOpenFileNames(self,
                                                    "选取图片",
                                                    "./",
                                                    "Image files (*.jpg *.gif *.png *bmp *tiff)")
        self.loadedPicsList += loadPics
        self.FreshPRListView()
        
    def ClearFile(self):
        self.loadedPicsList = []
        self.FreshPRListView()
        
    def SlctItems(self):
        self.slcdItems = []
        modelIndexes = self.picResourseListView.selectedIndexes()
        for i in range(len(modelIndexes)):
            self.slcdItems.append(modelIndexes[i].data())
            
    def ShowPic(self):
        if self.slcdItems:
            pic = QPixmap()
            pic.load(self.slcdItems[self.showingPicIndex])
            self.picViewLabel.setPixmap(pic)
            self.showingPicIndex = (self.showingPicIndex + 1) % len(self.slcdItems)
        else:
            QMessageBox.warning( self, "注意", "请选择想要查看的照片", QMessageBox.Yes, QMessageBox.No )
    
    def DltPic(self):
        for i in self.slcdItems:

            self.slcdItems.remove(i)
            self.loadedPicsList.remove(i)
        self.FreshPRListView()
        
    def ClsPic(self):
        pic = QPixmap()
        pic.load('E:/Python/GUIlearning/Start/Welcome.png')
        self.picViewLabel.setPixmap(pic)
        self.slcdItems = []
        self.FreshPRListView()
            

            
            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    splash = SplashScreen()
    splash.effect()
    app.processEvents()   #＃设置启动画面不影响其他效果
    window = MyApp()
    window.show()
    splash.finish(window)  
    sys.exit(app.exec_())