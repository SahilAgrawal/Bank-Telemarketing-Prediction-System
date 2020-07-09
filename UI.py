import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from predict import BTM
from about import About


class Ui_Frame(object):
    

    #######################################################################################
    
    # prediction.py were import and their function were called

    def open_predict(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = BTM()
        self.ui.predict_ui(self.window)
        self.window.show()
     
    #######################################################################################
    
    # about.py were import and their function were called.
    def open_about(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = About()
        self.ui.about_ui(self.window)
        self.window.show()
        
    #######################################################################################

    def setupUi(self, From):
        # Frame.setObjectName("Frame")
        Frame.resize(1080, 700)
        Frame.setMaximumSize(QtCore.QSize(1080, 700))    
        Frame.setStyleSheet("background-color: rgb(41, 40, 38);")
        Frame.setWindowTitle("Bank Telemarketing Interpretation System")
    
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(310, 50, 471, 371))
        self.label_2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#f9d342;\">Welcome </span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#f9d342;\">to </span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#f9d342;\">Bank Telemarketing</span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#f9d342;\">Interpretation</span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#f9d342;\">System</span></p></body></html>")
       
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 590, 151, 61))
        self.pushButton.setText(" About")
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton.clicked.connect(self.open_about)
     
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(810, 590, 221, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setText("Predication of Client")
        self.pushButton_2.clicked.connect(self.open_predict)

    
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(330, 450, 421, 41))
        self.label_3.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; text-decoration: underline; color:#ffffff;\">SISTec/B.Tech/CS/2019/5/Project 1/51</span></p></body></html>")
    

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

