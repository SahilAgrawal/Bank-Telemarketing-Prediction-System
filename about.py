from PyQt5 import QtCore, QtGui, QtWidgets


class About(object):
    def about_ui(self, BTM):
        BTM.setWindowTitle("Bank Telemarketing Interpretation System")
        # BTM.setObjectName("BTM")
        BTM.resize(1080, 600)
        BTM.setStyleSheet("background-color:#d6eaff; font:14pt \"Lalezar-Regular\";border: 19px ;border-radius:45px; ")
        BTM.setMaximumSize(QtCore.QSize(1080, 600))
        self.label1 = QtWidgets.QLabel(BTM)
        self.label1.setGeometry(QtCore.QRect(70, 90, 881, 191))
        # self.label1.setStyleSheet("background-color:#d0e1f9;font:14pt \"Lalezar-Regular\";border: 19px ;border-radius:45px; ")
        self.label1.setText("<html><head/><body><p><span style=\" font-size:16pt;\">• This Application will help the person working in the banking sector and </span></p><p><span style=\" font-size:16pt;\">   predicticting the customers who are interested in investing in some policy </span></p><p><span style=\" font-size:16pt;\">by contacting them through two different means of communication</span></p><p><span style=\" font-size:16pt;\">    i.e telephone or cellular.</span></p></body></html>")
        
        self.label2 = QtWidgets.QLabel(BTM)
        self.label2.setGeometry(QtCore.QRect(70, 270, 881, 201))
        self.label2.setText("<html><head/><body><p align=\"justify\"><span style=\" font-size:16pt;\">• The objective of this project is to find the best strategies to improve</span></p><p align=\"justify\"><span style=\" font-size:16pt;\">    for the marketing campaign, so that the financial institution have a</span></p><p align=\"justify\"><span style=\" font-size:16pt;\">   greater effectiveness for future marketing campaigns.</span></p><p align=\"justify\"><br/></p></body></html>")
        # self.label2.setStyleSheet("background-color:#d0e1f9;font:14pt \"Lalezar-Regular\";border: 19px ;border-radius:45px; ")

        self.label_3 = QtWidgets.QLabel(BTM)
        self.label_3.setGeometry(QtCore.QRect(70, 410, 881, 171))
        self.label_3.setText("<html><head/><body><p><span style=\" font-size:16pt;\">• We have to analyze the last marketing campaign the bank performed </span></p><p><span style=\" font-size:16pt;\">and identify the patterns that will help us find conclusions in order</span></p><p><span style=\" font-size:16pt;\">to develop future strategies.</span></p></body></html>")
        # self.label_3.setStyleSheet("background-color:#d0e1f9;font:14pt \"Lalezar-Regular\";border: 19px ;border-radius:45px; ")

        self.label = QtWidgets.QLabel(BTM)
        self.label.setGeometry(QtCore.QRect(70, 10, 400, 71))
        # self.label.setStyleSheet("background-color:#d0e1f9;font:14pt \"Lalezar-Regular\";border: 19px ;border-radius:45px; ")
        self.label.setText("<html><head/><body><p><span style=\" font-size:20pt; text-decoration: underline;\"> ABOUT OF APPLICATION </span></p></body></html>")
     
# if __name__ == '__main__':
        
#         import sys
#         app = QtWidgets.QApplication(sys.argv)
#         Frame = QtWidgets.QMainWindow()
#         ui = About()
#         ui.about_ui(Frame)
#         Frame.show()
#         sys.exit(app.exec_())