# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 19:48:24 2017

@author: xchen
"""
from PyQt5 import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QScrollArea, QFrame, QGridLayout
from PyQt5.QtCore import QFileInfo, QMatrix
import pyqt_CourseAssignment_test.py
class QImageViewer(pyqt_CourseAssignment_test.py.MyApp):
    
    def __init__(self):
        self.imageAngle = 0
        pass
    
    
    # 打开预览
    def openActionTriggered(self):
        filename = QFileDialog.getOpenFileName(self, "Select image:", "./", "Image (*.png *.bmp *.jpg *.gif)")
        if filename.isEmpty():
            return
        im = QImage()
        if (~im.load(filename)):
            QMessageBox.information(self, "Error", "Open file error!")
            return
        
        pix = QPixmap()
        pix.fromImage(im)
        imSize = pix.size()
        
        self.picViewLabel.setPixmap(pix)
        self.picViewLabel.resize(imSize)
        
        self.setWindowTitle(QFileInfo(filename).fileName + "- imageView")
        
    # 关闭预览    
    def closeActionTriggered(self):
        self.picViewLabel.clear()
        self.picViewLabel.resize(200, 100)
        self.setWindowTitle("imageViewer")
        
    # 超过Label大小时有scroll可以调整位置    
    def setImageShowWidget(self):
        # self.picViewLabel()
        imScrollArea = QScrollArea()
        imScrollArea.setAlignment(Qt.AligCenter)
        imScrollArea.setFrameShape(QFrame.NoFrame)
        imScrollArea.setWidget(self.picViewLabel)
        
        mainLayout = QGridLayout()
        mainLayout.addWidget(imScrollArea, 0, 0)
        self.centralWidget.setLayout(mainLayout)
        
#    def getImageInfoList()
        
    # 左旋    
    def toLeftActionTriggered(self):
        self.imageAngle += 3
        self.imageAngle %= 4
        
        matrix = QMatrix()
        matrix.rotate(self.imageAngle * 90)
        
        image = QImage()
        image.load(self.loadedPicsList[0])
        imageRotate = image.transformed(matrix)
        
        pixmap = QPixmap()
        pixmap.fromImage(imageRotate)
        imageSize = pixmap.size()
        
        self.picViewLabel.resize(imageRotate.size())
        self.picViewLabel.setPixmap(pixmap)
        
        
    def toEnlargeActionTriggered(self):
        imgScaled = QImage()
        pixmap = QPixmap()
        image = QImage()
        imgRotate = QImage()
        matrix = QMatrix()
        
        image.load(self.loadedPicsList[0])
        matrix.rotate(imageAngle * 90)
        imgRotate = image.transformed(matrix)
        
        imgScaled = imgRotate.scaled(imageSize.width()*1.2,
                                     imageSize.height()*1.2,
                                     Qt.KeepAspectRatio)
        
        pixmap = QPixmap.fromImage(imgScaled)
        imageSize = pixmap.size()
        
        imageLabel.setPixmap(pixmap)
        imageLabel.resize(imageSize)
        
        
        
        
        
        
        
        
        