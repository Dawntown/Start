# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:17:20 2017

@author: xchen
"""

import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PIL import Image#, ImageFilter

qtCreatorFile = "CourseAssignment.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.loadedPicsList = []
        self.showingPicIndex = 0
        self.picFrame = [825, 550]
        
        self.loadPicBtn.clicked.connect(self.LoadFile)
        self.picResourseListView.clicked.connect(self.SlctItems)
        self.clearPicBtn.clicked.connect(self.ClearFile)
        self.checkPicBtn.clicked.connect(self.ShowPic)
        self.deletePicBtn.clicked.connect(self.DltPic)
        self.closePicBtn.clicked.connect(self.ClsPic)
        
    def FreshPRListView(self):
        model = QStandardItemModel(self.picResourseListView)
        for pic in self.loadedPicsList:
            picItem = QStandardItem(pic)
            picItem.setCheckable(True)
            model.appendRow(picItem)
        self.picResourseListView.setModel(model)
        self.picResourseListView.show()
        
        
    def LoadFile(self):
        loadPics, ok = QFileDialog.getOpenFileNames(self,
                                                    "选取图片",
                                                    "./",
                                                    "All Files (*);;Text Files(*.txt)")
        self.loadedPicsList += loadPics
        self.FreshPRListView()
        
    def ClearFile(self):
        self.loadedPicsList = []
        self.FreshPRListView()
        
    def SlctItems(self):
        self.slcdItems = []
        items = self.picResourseListView.selectedIndexes()
        for it in items:
            self.slcdItems.append(self.loadedPicsList[it.row()])
            
    def ShowPic(self):
        if self.slcdItems:
            pic = Image.open(self.slcdItems[self.showingPicIndex])
            w, h = pic.size
            scale = min((self.picFrame[0]/w, self.picFrame[0]/h))
            pic.thumbnail((w*scale, h*scale))
            pic = QPixmap()
            self.picViewLabel.setPixmap(QPixmap(pic))
            self.showingPicIndex = (self.showingPicIndex + 1) % len(self.slcdItems)
        else:
            QMessageBox.warning( self, "PyQT", "warning", QMessageBox.Yes, QMessageBox.No )
    
    def DltPic(self):
        for i in self.slcdItems:
            self.loadedPicsList.remove(i)
        self.FreshPRListView()
        
    def ClsPic():
        pass
            

            
            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())