# importing libraries
from email.mime import image
import os
from select import select
from tkinter import Label
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5 import QtMultimedia
import requests
import sys
from config import *
from package.window.notifications import getDiamonds, getGifts, getLikes, getShares, getSubscribers, getFollowers, getUser, runAPI

class CustThread(QThread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        runAPI()

class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
        # setting title
        self.setWindowTitle("")
        self.configuration = Config()
        self.setGeometry(100, 100, 600, 400)
        self.current = self.configuration.starting_amount
        self.maxGoal = self.configuration.goal_amount
        self.labelA = QLabel(self)
        self.bar1 = QProgressBar(self)
        self.goal = QLabel(self)
        self.last_donor = QLabel(self)

        self.last_donor_pfp = QLabel(self)
        self.last_donor_counter = 0
        self.player = QtMultimedia.QMediaPlayer()

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

        # starting the thread
        self.thread = CustThread()
        self.thread.start()

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(self.configuration.update_interval*1000)
        self.timer.timeout.connect(self.updateUI)
        self.timer.start()
        
    #This method updates the UI by increasing current follower count by num
    def updateUI(self):
        self.current = eval(self.configuration.event_tracked[2])
        user = getUser()
        print(self.current)
        self.goal.setText(str(self.current)+ "/" +str(self.maxGoal) + " " + self.configuration.goal_unit)
        self.bar1.setValue(self.maxPercent(self.current,self.maxGoal))
        if(self.configuration.show_last):
            if(self.configuration.show_last is False):
                None
            elif(self.last_donor.text() != user[0] and user[0] != None):
                self.last_donor.setText(user[0] + " just " + self.configuration.action + "!")
                img = QImage()
                img.loadFromData(requests.get(user[1].avatar_url).content)

                out_img = QImage(96, 96, QImage.Format_ARGB32)
                out_img.fill(Qt.transparent)
                brush = QBrush(img)
                painter = QPainter(out_img)
                painter.setBrush(brush)
                painter.setPen(Qt.NoPen)
                painter.drawEllipse(0, 0, 96, 96)
                # closing painter event
                painter.end()
                self.last_donor_pfp.setPixmap(QPixmap(out_img).scaled(64,64))
                self.last_donor_pfp.resize(64, 64)
                self.last_donor_counter = self.configuration.intervals_last

                if(self.configuration.sound_on):
                    path = os.getcwd().replace("\\", "\\\\" )
                    url = QUrl.fromLocalFile(f"{path}\\package\\{self.configuration.sound_path}")
                    content = QtMultimedia.QMediaContent(url)
                    self.player.setMedia(content)
                    self.player.play()

            elif (self.last_donor_counter <= 0):
                self.last_donor.setText("")
                self.last_donor_pfp.setText("")
                self.last_donor_pfp.setStyleSheet("")
                self.last_donor_pfp.setPixmap(QPixmap())
                self.last_donor_counter = self.configuration.intervals_last

            else:
                self.last_donor_counter -= 1

        self.show()

    #if percent is larger than 100, return 100, else return actual percent
    def maxPercent(self, divisor, dividend):
        if(divisor>dividend):
            return 100
        return int(100*divisor/dividend)

    # method for widgets
    def UiComponents(self):
        # adding color effect to the top label
        self.labelA.setStyleSheet("QLabel { color : "+ self.configuration.goal_text_color +"; }")
        self.labelA.setText(self.configuration.goal_name)
        self.labelA.setFont(QFont(self.configuration.Font, 15, 200))
        self.labelA.setAlignment(Qt.AlignCenter)
        self.labelA.setGeometry(200, 70, 200, 30)
  
        # setting geometry to progress bar
        self.bar1.setGeometry(200, 100, 200, 30)
        # setting the value
        self.bar1.setValue(self.maxPercent(self.current,self.maxGoal))
        # setting alignment to center
        self.bar1.setAlignment(Qt.AlignCenter)
        # setting font and the size
        self.bar1.setFont(QFont(self.configuration.Font, 15))
        self.bar1.setStyleSheet("QProgressBar::chunk "
                          "{"
                          "background-color: "+self.configuration.bar_color+";"
                          "border-style: outset;"
                          "border-width: 2px;"
                          "border-radius: 10px;"
                          "border-color: beige;"
                          "font: bold 14px;"
                          "min-width: 10em;"
                          "padding: 6px;"
                          "}")

        #set goal text (ie "600/1000 Followers")
        self.goal.setText(str(self.current)+ "/" +str(self.maxGoal) + " " + self.configuration.goal_unit)
        self.goal.setFont(QFont(self.configuration.Font, 10, 30))
        self.goal.setAlignment(Qt.AlignCenter)
        self.goal.setGeometry(200, 130, 200, 30)
        self.goal.setStyleSheet("QLabel { color : "+self.configuration.goal_text_color+"; }")

        self.last_donor_pfp.setText("")
        self.last_donor_pfp.setFont(QFont(self.configuration.Font, 10, 30))
        self.last_donor_pfp.setAlignment(Qt.AlignCenter)
        self.last_donor_pfp.setGeometry(270, 160, 200, 40)
        self.last_donor_pfp.setStyleSheet("QLabel { color : "+self.configuration.goal_text_color+"; }")

        self.last_donor.setText("")
        self.last_donor.setFont(QFont(self.configuration.Font, 10, 30))
        self.last_donor.setAlignment(Qt.AlignCenter)
        self.last_donor.setGeometry(200, 220, 200, 40)
        self.last_donor.setStyleSheet("QLabel { color : "+self.configuration.goal_text_color+"; }")


def run():
    app = QApplication(sys.argv)

    window = Window()
    window.setWindowTitle(window.configuration.goal_name)
    window.setStyleSheet("background-color: "+window.configuration.background_color+";")
    window.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()