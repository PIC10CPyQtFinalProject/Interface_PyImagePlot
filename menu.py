# -*- coding: utf-8 -*-
"""@file hw10_menu.py
@brief PyQt Interface
@author: Shiyun Qiu & Siwen Tang
@date June 2, 2016

This program creates a PyQt interface for a data visualization research project.
Users can create montages, histograms and scatter plots without typing in commands.
There is no need to type in the whole paths of their photos manually.
They just need to click several buttons and finish their work.
"""


from PyQt4.QtGui import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QGridLayout, QMessageBox, QFileDialog, QPalette, QBrush, QPixmap, QVBoxLayout, QGroupBox
from PyQt4.QtCore import pyqtSignal, Qt
from montage_manager import Montages
import sys

class MainWidget(QWidget):
    """@class MainWidget
    @brief Main Window of the Interface
 
    This class is the main window of the interface. The menu are five options. The user
    can choose what kind of plots they would like to create by clicking the radio button
    and then click Enter.
    The user can quit the program by either clicking Quit or clicking the close button on
    the upper left corner.
    """
    def __init__(self, parent=None):
        """The constructor."""
        super(MainWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # local variable that records which radio button is clicked
        self.choice = 1
        # welcome message
        welcomeMsg = QLabel(self)
        welcomeMsg.setText("Welcome to the PyQt Interface!")
        welcomeMsg.setAlignment(Qt.AlignCenter)
        menu = QLabel(self)
        menu.setText("Menu")
        # create buttons & connect them with function btnClicked
        btn1 = QRadioButton(self)
        btn1.setText("1. Create montages recursively from given directory and sub-directories")
        btn1.setChecked(True)
        btn1.toggled.connect(lambda:self.btnClicked(1))        
        btn2 = QRadioButton(self)
        btn2.setText("2. Create montages from provided CSV files (split by categories or bins)")
        btn2.toggled.connect(lambda:self.btnClicked(2))
        btn3 = QRadioButton(self)
        btn3.setText("3. Create vertical montage from provided CSV file")
        btn3.toggled.connect(lambda:self.btnClicked(3))
        btn4 = QRadioButton(self)
        btn4.setText("4. Create image histogram from provided CSV file")
        btn4.toggled.connect(lambda:self.btnClicked(4))
        btn5 = QRadioButton(self)
        btn5.setText("5. Create scatter plot from provided CSV file")
        btn5.toggled.connect(lambda:self.btnClicked(5))
        quit = QPushButton(self)
        quit.setText("Quit")
        enter = QPushButton(self)
        enter.setText("Enter")
        instr = QPushButton(self)
        instr.setText("Instruction")
        self.setStyleSheet('QLabel {font-family: cursive, sans-serif; font-weight: 500; font-size: 16px; color: #A0522D;} QRadioButton {font-family: cursive, sans-serif; font-weight: 300; font-size: 16px; color: #8B4513;} QPushButton {font-family: cursive, sans-serif; font-weight: 500; font-size: 16px; color: #CD853F; }')
        welcomeMsg.setStyleSheet('QLabel {font-weight: 900;font-size: 20px;}')        
        # set layout
        mbox = QGridLayout(self)
        mbox.addWidget(welcomeMsg, 1, 1)
        mbox.addWidget(menu,2,1)
        mbox.addWidget(btn1,3,1)
        mbox.addWidget(btn2,4,1)
        mbox.addWidget(btn3,5,1)
        mbox.addWidget(btn4,6,1)
        mbox.addWidget(btn5,7,1)
        mbox.addWidget(quit,8,0)
        mbox.addWidget(enter,8,2)
        mbox.addWidget(instr,8,1)
        self.setLayout(mbox)
        # connect the click event with a function
        enter.clicked.connect(self.nextPage)
        quit.clicked.connect(self.close)
        instr.clicked.connect(self.instruction)
        # set background as transparent
        palette	= QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap()))
        self.setPalette(palette)       

    def nextPage(self):
        """Hide the main window and show another window where the plots are created"""
        self.hide()
        # pass the value of variable choice and create a new widget
        self.widget2 = SubWidget(self.choice)
        self.widget2.show()
        # when close the sub window , show the main window again
        self.widget2.closed.connect(self.show)
            
    def closeEvent(self, event):
        """When close the main window, pop out a confirming box"""
        quit_msg = "Are you sure you want to exit the program?"
        reply = QMessageBox.question(self, 'Message', 
                     quit_msg,QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()  
                  
    def btnClicked(self, val):
        """Record which radio button is clicked """
        self.choice = val
           
    def instruction(self):
        """Hide the main window and show the window of instructions"""
        self.hide()
        # pass the value of variable choice and create a new widget
        self.widget3 = SubWidget2(self.choice)
        self.widget3.show()
        # when close the sub window , show the main window again
        self.widget3.closed.connect(self.show)

class SubWidget(QWidget):
    """@class SubWidget
    @brief Another Window of the Interface
     
    This class is the other window of the interface. Users can choose the folder
    where their photos are stored, and the folder where they want to save their plots.
    After choosing these folders, users can create plots by simply clicking Create Plot.
    Users can return to the main window by clicking the close button on the upper left 
    corner of the window.
    """   
    # self-defined signal
    closed = pyqtSignal()
    
    def __init__(self, choice, parent = None):
        """The constructor."""
        super(SubWidget, self).__init__(parent)
        # assign the local variable option with the value of choice
        self.option = choice
        self.initUI()
        
    def initUI(self):
        # create a class object
        self.setStyleSheet('QPushButton {font-family: cursive, sans-serif; font-weight: 300; font-size: 14px; color: #CD853F; }') 
        self.montage = Montages()
        # create buttons
        createPath = QPushButton(self)
        createPath.setText("Choose the directory of your photos")
        createPath.clicked.connect(self.cPath)
        savePath = QPushButton(self)
        savePath.setText("Choose the directory to save your plot")
        savePath.clicked.connect(self.sPath)
        create = QPushButton(self)
        create.setText("Create plot")
        create.clicked.connect(self.createPlot)
        # set layout
        sbox = QGridLayout(self)
        sbox.addWidget(createPath, 1, 0)
        sbox.addWidget(savePath, 2, 0)
        sbox.addWidget(create, 3, 1)
        self.setLayout(sbox)
        # set background as transparent
        palette	= QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap()))
        self.setPalette(palette)
        
    def closeEvent(self, event):
        """Define signal closed"""
        self.closed.emit()
        event.accept()
        
    def cPath(self):
        """Save the path of the directory where pictures are stored"""
        self.srcPath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        
    def sPath(self):
        """Save the path of the directory where the montage should be stored"""
        self.destPath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        
    def createPlot(self):
        """Check user's choice and create the plot"""
        if self.option == 1:
           self.montage.input_data(src_path = self.srcPath, dest_path = self.destPath)
           self.montage.montages_from_directory()
 
class SubWidget2(QWidget):
    """@class SubWidget2
    @brief Window of User Instruction
     
    This class is the window of user instruction. It instructs the user how to use the interface.
    """  
    # self-defined signal
    closed = pyqtSignal()
    
    def __init__(self, choice, parent = None):
        """The constructor."""
        super(SubWidget2, self).__init__(parent)    
        self.initUI()
        
    def initUI(self):
        # title
        title = QLabel(self)
        title.setText("User Instruction")
        title.setAlignment(Qt.AlignCenter)
        # user instruction
        groupBox = QGroupBox()
        text = QLabel(self)
        text.setText("Create image montages and histograms from the interface:\nChoose option No. 1 to 5 on main interface.\nClick Enter to select the paths for input and output locations.\nEnjoy using the interface!")
        self.setStyleSheet("QLabel { color: #8B4513; font-size: 16px;font-family: cursive, sans-serif;}")    
        title.setStyleSheet("QLabel { color: #8B4513; font-weight: 600;}")
        # set layout
        sbox = QVBoxLayout(self)
        sbox.addWidget(text)
        groupBox.setLayout(sbox) 
        vBoxLayout = QVBoxLayout()
        vBoxLayout.addSpacing(15)
        vBoxLayout.addWidget(title)
        vBoxLayout.addWidget(groupBox)
        vBoxLayout.addSpacing(15)
        self.setLayout(vBoxLayout)
        # set background as transparent
        palette	= QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap()))
        self.setPalette(palette)
        
    def closeEvent(self, event):
        """define signal closed"""
        self.closed.emit()
        event.accept()
        
def main():
    app=QApplication([])
    widget1=MainWidget()
    widget1.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()