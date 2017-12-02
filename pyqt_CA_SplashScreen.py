# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:48:04 2017

@author: xchen
"""

# -*- coding:utf8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QColor, QFont
from PyQt5.QtWidgets import QSplashScreen, QApplication
import sys, time#, date
#from pyqt_CourseAssignment_test import MyApp
import random

class SplashScreen(QSplashScreen):
    def __init__(self):
        QSplashScreen.__init__(self)
        text = self.outPutContents()
        self.setPixmap(QPixmap("Startup.png"))#启动程序的图片
        self.setFont(QFont("方正细黑一简体", 11))
        self.showMessage(text,
                         Qt.AlignHCenter|Qt.AlignVCenter,
                         QColor(240, 255, 240))

    #效果 fade =1 淡入   fade= 2  淡出，  t sleep 时间 毫秒
    def effect(self):
        self.setWindowOpacity(0)
        t = 0
        while t <= 50:
            newOpacity = self.windowOpacity() + 0.02     #设置淡入
            if newOpacity > 1:
                break

            self.setWindowOpacity(newOpacity)
            self.show()
            t -= 1
            time.sleep(0.04)

        time.sleep(5)
        t = 0
        while t <= 50:
            newOpacity = self.windowOpacity() - 0.02         #设置淡出
            if newOpacity < 0:
                break

            self.setWindowOpacity(newOpacity)
            t += 1
            time.sleep(0.02)
            
    # 把系统时间转换为中文时间用于输出  
    def outPutContents(self):
        EYES = ("\n\n\n\n\n\n\n\n\n\n       眼睛会说话。\n\n——大山",
                "\n\n\n\n\n\n\n\n\n\n       眼睛是心灵的叛徒。\n\n——魏阿特",
                "\n\n\n\n\n\n\n\n\n\n       眼睛是内心索引。\n\n——安斯蒂",
                "\n\n\n\n\n\n\n\n\n\n       常作痛的眼睛宁愿挖掉。\n\n——《圣经》",
                "\n\n\n\n\n\n\n\n\n\n       恋人的眼睛比猫头鹰的还瞎。\n\n——克雷克",
                "\n\n\n\n\n\n\n\n\n\n       眼睛会泄露心中的秘密。\n\n——乔·爱略特",
                "\n\n\n\n\n\n\n\n\n\n       两只眼睛比一只眼睛看得清楚。\n\n——马勒",
                "\n\n\n\n\n\n\n\n\n\n       美会在凝视者的眼睛里。\n\n——刘·华莱士",
                "\n\n\n\n\n\n\n\n\n\n       黑夜给了我黑色的眼睛\n我却用它来寻找光明。\n\n——顾城",
                "\n\n\n\n\n\n\n\n\n\n       黑夜给了我黑色的眼睛，\n我却要用它去戴博士伦。\n\n——汪涵",
                "\n\n\n\n\n\n\n\n\n\n       青年们尽可以张开眼睛，\n用自己的判断力以决定自己的前途。\n\n——恽代英",
                "\n\n\n\n\n\n\n\n\n\n       指责人民有眼无珠的往往\n就是那些蒙住人民眼睛的人。\n\n——弥尔顿",
                "\n\n\n\n\n\n\n\n\n\n       多数人有眼睛，极少数人有理智。\n\n——查尔斯·丘吉尔",
                "\n\n\n\n\n\n\n\n\n\n       孩子的什么事都别想逃过母亲的眼睛。\n\n——倪萍")
        WEEK = {'Sun':'星期天',
                'Mon':'星期一',
                'Tue':'星期二',
                'Wed':'星期三',
                'Thu':'星期四',
                'Fri':'星期五',
                'Sat':'星期六'}

        datetimeList = time.strftime("%Y %m %d %H %M %a", time.localtime()).split()
        dateStr = "\n\n今天是 " + datetimeList[0] + "年 " + datetimeList[1] + "月 " + datetimeList[2] + "日 " + WEEK[datetimeList[5]] + ",\n"
        timeStr = "现在" + datetimeList[3] + "点" + datetimeList[4] + "分。\n\n                            很高兴见到你:P"
        greet = EYES[random.randint(0,14)] + dateStr + timeStr
        
        return greet
    
    # 绘制一定格式的文本输入到启动页面
    def drawText(self):
        self.setPen(QColor(255, 255, 255))
        pass
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.effect()
    app.processEvents()   #＃设置启动画面不影响其他效果
#    window.show()
#    splash.finish(window)      #启动画面完成启动
    sys.exit(app.exec_())
