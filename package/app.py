# importing libraries
from select import select
from tkinter import Label
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
from package.window import notifications
from config import *
  
  
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

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()
        
    #This method updates the UI by increasing current follower count by num
    def updateUI(self, num):
        self.current +=num
        self.goal.setText(str(self.current)+ "/" +str(self.maxGoal) + self.configuration.goal_unit)
        self.bar1.setValue(self.maxPercent(self.current,self.maxGoal))
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
  
  
def run():
    app = QApplication(sys.argv)

    window = Window()
    window.setWindowTitle(window.configuration.goal_name)
    window.setStyleSheet("background-color: "+window.configuration.background_color+";")
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    run()