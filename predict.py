# import Libraries 

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


# when screen scale (100 to 175%)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons


# class of lables and text fields 
class BTM(object):



        # methods of lables and text fields 
        def predict_ui(self, BTM):
               
                # size on screen of the application
                BTM.setObjectName("BTM")
                BTM.resize(2080,960)
                BTM.setWindowTitle("Bank Telemarketing Interpretation System")
                BTM.setStyleSheet("background-color:#34495E;")
                # BTM.setMaximumSize(QtCore.QSize(2080, 1080))

                
                
                # Scroll area on screen

                self.scrollArea = QtWidgets.QScrollArea(BTM)
                self.scrollArea.setEnabled(True)
                
                self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1400, 1020))
                # self.scrollArea.setMaximumSize(QtCore.QSize(2201, 1080))
                self.scrollArea.setMouseTracking(True)
                # self.scrollArea.setStyleSheet(" background-color:#626d71;")
                self.scrollArea.setStyleSheet(" background-color:#d6eaff ;")
                # self.scrollArea.setStyleSheet(" background-color:#d6eaff ;")
                # self.scrollArea.setStyleSheet(" background-image: linear-gradient(black, yellow);")
                # self.scrollArea.setStyleSheet("background-image: url('1.jpg');")
                self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
                # self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
                self.scrollArea.setWidgetResizable(False)
                self.scrollArea.setObjectName("scrollArea")
                self.scrollAreaWidgetContents = QtWidgets.QWidget()
                self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1400, 1120))
                self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(1400, 1120))
                self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
                self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        #########################################################################################################################
     

                self.Client_Information = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.Client_Information.setGeometry(QtCore.QRect(10, 2, 1360, 91))
                # self.Client_Information.setMaximumSize(QtCore.QSize(1381, 556151))
                self.Client_Information.setStyleSheet("background-color: #476c8a;font: 24pt \"Grenze-MediumItalic\";border: 3px black; border-radius: 30px;")
                self.Client_Information.setText("                                 Informations of Client")
                

        #########################################################################################################################    

                self.IsClientInterested = QtWidgets.QLabel(BTM)
                self.IsClientInterested.setGeometry(QtCore.QRect(1405, 2, 500, 90))
                # self.IsClientInterested.setMaximumSize(QtCore.QSize(1381, 556151))
                self.IsClientInterested.setStyleSheet("background-color: #f9d342;color : #ffffff;font: 24pt \"Grenze-MediumItalic\";border: 3px solid white; border-radius: 30px;")
                self.IsClientInterested.setText("     Is Client Interested??")

        #########################################################################################################################

                self.otherInfo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.otherInfo.setGeometry(QtCore.QRect(10, 635, 1360, 51))
                self.otherInfo.setStyleSheet("background-color: #4279a3 ;font:14pt \"Lalezar-Regular\";border: 10px ;border-radius:15px;")
                self.otherInfo.setText(" Other Information")

        #########################################################################################################################

                self.PersonalInfo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.PersonalInfo.setGeometry(QtCore.QRect(10, 95, 1360, 51))
                self.PersonalInfo.setStyleSheet("background-color: #4279a3 ;font:14pt \"Lalezar-Regular\";border: 10px ;border-radius: 15px; ")
                self.PersonalInfo.setText(" Personal Information")

        #########################################################################################################################

                self.callInfo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.callInfo.setGeometry(QtCore.QRect(10, 420, 1360, 51))
                self.callInfo.setStyleSheet("background-color: #4279a3 ;font:14pt \"Lalezar-Regular\";border: 10px ;border-radius:15px; ")
                self.callInfo.setText(" Call Information")

        #########################################################################################################################
        # Line 
                
                # self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
                # self.line.setGeometry(QtCore.QRect(1372, 0, 8, 1120))
                # self.line.setStyleSheet("background-color:#ffffff;")

              

        #########################################################################################################################
        # """ Age """
                self.age = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.age.setGeometry(QtCore.QRect(50, 170, 201, 41))
                self.age.setStyleSheet("background-color:#8b9dc3; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                # self.age.setStyleSheet("background-image: linear-gradient(red, yellow);font:  11pt \"Barlow-Medium\";border: 15px ;border-radius:15px; ")
                self.age.setText(" Age")


                self.agetxt = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                self.agetxt.setGeometry(QtCore.QRect(290, 170, 121, 41))
                self.agetxt.setStyleSheet("background-color:#ffffff;font:  11pt \"Barlow-Medium\";border: 5px light black;border-radius:10px; ")
                self.agetxt.setPlaceholderText("Age")

        #########################################################################################################################
        #       """ Job """

                self.jobTxt = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
                self.jobTxt.setGeometry(QtCore.QRect(290, 230, 191, 41))
                self.jobTxt.setStyleSheet("background-color:#ffffff;font:  11pt \"Barlow-Medium\";border: 5px light black;border-radius:10px; ")
                self.jobTxt.addItem("Admin")
                self.jobTxt.addItem("Blue-collar")
                self.jobTxt.addItem("Enterpreneur")
                self.jobTxt.addItem("Housemaid")
                self.jobTxt.addItem("Management")
                self.jobTxt.addItem("Retired")
                self.jobTxt.addItem("Self-employed")
                self.jobTxt.addItem("Services")
                self.jobTxt.addItem("Student")
                self.jobTxt.addItem("Technician")
                self.jobTxt.addItem("Unemployed")
                self.jobTxt.addItem("Unknown")


                self.job = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.job.setGeometry(QtCore.QRect(50, 230, 201, 41))
                self.job.setStyleSheet("background-color:#8b9dc3; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                self.job.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.job.setText(" Job")

        #########################################################################################################################
        #       """ Marital """

                self.marital = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.marital.setGeometry(QtCore.QRect(50, 290, 201, 41))
                self.marital.setStyleSheet("background-color:#8b9dc3; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                self.marital.setText(" Marital")
        
                
                self.maritalTxt = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
                self.maritalTxt.setGeometry(QtCore.QRect(290, 290, 191, 41))
                self.maritalTxt.setStyleSheet("background-color:#ffffff;font:  11pt \"Barlow-Medium\";border: 5px light black;border-radius:10px; ")
                self.maritalTxt.addItem("Married")
                self.maritalTxt.addItem("Divorced")
                self.maritalTxt.addItem("Single")
                self.maritalTxt.addItem("Widow")

                
        #########################################################################################################################
        #       """ DAYS """

                self.day = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.day.setGeometry(QtCore.QRect(710, 510, 271, 41))
                self.day.setStyleSheet("background-color:#8b9dc3; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                self.day.setText(" Day of week ")

                
                self.dayTxt = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
                self.dayTxt.setGeometry(QtCore.QRect(1020, 510, 191, 41))
                self.dayTxt.setStyleSheet("background-color:#ffffff;font:  11pt \"Barlow-Medium\";border: 5px light black;border-radius:10px; ")
                self.dayTxt.addItem("Mon")
                self.dayTxt.addItem("Tue")
                self.dayTxt.addItem("Wed")
                self.dayTxt.addItem("Thu")
                self.dayTxt.addItem("Fri")

        #########################################################################################################################
        #       """ Month """

                self.month = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.month.setGeometry(QtCore.QRect(50, 500, 271, 41))
                self.month.setStyleSheet("background-color:#8b9dc3; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                self.month.setText(" Month")


                self.monthTxt = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
                self.monthTxt.setGeometry(QtCore.QRect(360, 500, 191, 41))
                self.monthTxt.setStyleSheet("background-color:#ffffff;font:  11pt \"Barlow-Medium\";border: 5px light black;border-radius:10px; ")
                self.monthTxt.addItem("Jan")
                self.monthTxt.addItem("Feb")
                self.monthTxt.addItem("Mar")
                self.monthTxt.addItem("Apr")
                self.monthTxt.addItem("May")
                self.monthTxt.addItem("Jun")
                self.monthTxt.addItem("Jul")
                self.monthTxt.addItem("Aug")
                self.monthTxt.addItem("Sep")
                self.monthTxt.addItem("Oct")
                self.monthTxt.addItem("Nov")
                self.monthTxt.addItem("Dec")


        #########################################################################################################################
        #       """ Education  """"      
          
                self.edu = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.edu.setGeometry(QtCore.QRect(50, 350, 201, 41))
                self.edu.setStyleSheet("background-color:#8b9dc3; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                self.edu.setText(" Education")


                self.eduTxt = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
                self.eduTxt.setGeometry(QtCore.QRect(290, 350, 191, 41))
                self.eduTxt.setStyleSheet("background-color:#ffffff;font:  11pt \"Barlow-Medium\";border: 5px light black;border-radius:10px; ")
                self.eduTxt.addItem("University Degree")
                self.eduTxt.addItem("Unknown")
                self.eduTxt.addItem("Professional Course")
                self.eduTxt.addItem("Illiterate")
                self.eduTxt.addItem("High.school")
                self.eduTxt.addItem("Basic.9y")
                self.eduTxt.addItem("Basic.6y")
                self.eduTxt.addItem("Basic.4y")
                
        #########################################################################################################################
        #       """ Default "Credit"  """

                self.credit = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.credit.setGeometry(QtCore.QRect(710, 170, 201, 41))
                self.credit.setStyleSheet("background-color:#8b9dc3; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                self.credit.setText(" Client\'s Credit")

                
                self.creditTxt = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
                self.creditTxt.setGeometry(QtCore.QRect(950, 170, 191, 41))
                self.creditTxt.setStyleSheet("background-color:#ffffff;font:  11pt \"Barlow-Medium\";border: 5px light black;border-radius:10px; ")
                self.creditTxt.setObjectName("creditTxt")
                self.creditTxt.addItem("Yes")
                self.creditTxt.addItem("No")
                self.creditTxt.addItem("Unknown")

        #########################################################################################################################
        #       """ Loan """

                self.loan = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.loan.setGeometry(QtCore.QRect(710, 290, 201, 41))
                self.loan.setStyleSheet("background-color:#8b9dc3; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                self.loan.setText(" Any Personal Loan")

                self.loanTxt = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
                self.loanTxt.setGeometry(QtCore.QRect(950, 290, 191, 41))
                self.loanTxt.setStyleSheet("background-color:#ffffff;font:  11pt \"Barlow-Medium\";border: 5px light black;border-radius:10px; ")
                self.loanTxt.addItem("Yes")
                self.loanTxt.addItem("No")
                self.loanTxt.addItem("Unknown")
        #########################################################################################################################

        #       """ House Loan """

                self.house = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.house.setGeometry(QtCore.QRect(710, 230, 201, 41))
                self.house.setStyleSheet("background-color:#8b9dc3; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                self.house.setText(" Any house loan")


                self.houseTxt = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
                self.houseTxt.setGeometry(QtCore.QRect(950, 230, 191, 41))
                self.houseTxt.setStyleSheet("background-color:#ffffff;font:  11pt \"Barlow-Medium\";border: 5px light black;border-radius:10px; ")
                self.houseTxt.addItem("Yes")
                self.houseTxt.addItem("No")
                self.houseTxt.addItem("Unknown")

        #########################################################################################################################
        #       """ Contact Type """

                self.contact = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.contact.setGeometry(QtCore.QRect(710, 350, 201, 41))
                self.contact.setStyleSheet("background-color:#8b9dc3; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                self.contact.setText(" Type of contact")


                self.contactTxt = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
                self.contactTxt.setGeometry(QtCore.QRect(950, 350, 191, 41))
                self.contactTxt.setStyleSheet("background-color:#ffffff;font:  11pt \"Barlow-Medium\";border: 5px light black;border-radius:10px; ")
                self.contactTxt.addItem("Cellular")
                self.contactTxt.addItem("Telephone")

        #########################################################################################################################
        #       """ Before campaign Previous """

                self.befCmp = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.befCmp.setGeometry(QtCore.QRect(50, 760, 501, 41))
                self.befCmp.setStyleSheet("background-color:#8b9dc3; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                self.befCmp.setText(" Number of contact were done before this campaign")

                
                
                self.befCmpTxt = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                self.befCmpTxt.setGeometry(QtCore.QRect(590, 760, 191, 41))
                self.befCmpTxt.setStyleSheet("background-color:#ffffff;font:  11pt \"Barlow-Medium\";border: 5px light black;border-radius:10px; ")
                self.befCmpTxt.setPlaceholderText("numeric")

        #########################################################################################################################
        #       """ During campaign """

                self.duringCampaign = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.duringCampaign.setGeometry(QtCore.QRect(50, 700, 501, 41))
                self.duringCampaign.setStyleSheet("background-color:#8b9dc3; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                self.duringCampaign.setText(" Number of contact performed during this campaign")

                self.duringCampaignTxt = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                self.duringCampaignTxt.setGeometry(QtCore.QRect(590, 700, 191, 41))
                self.duringCampaignTxt.setStyleSheet("background-color:#ffffff;font:  11pt \"Barlow-Medium\";border: 5px light black;border-radius:10px; ")
                self.duringCampaignTxt.setPlaceholderText("numeric")
                
        #########################################################################################################################
        #       """ outcome """

                self.outcome = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.outcome.setGeometry(QtCore.QRect(50, 880, 501, 41))
                self.outcome.setStyleSheet("background-color:#8b9dc3; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                # self.outcome.setStyleSheet("background-color:#f3b5998; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                self.outcome.setText(" Outcome of previous market campaign")

                
                self.outcomeTxt = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
                self.outcomeTxt.setGeometry(QtCore.QRect(590, 880, 191, 41))
                self.outcomeTxt.setStyleSheet("background-color:#ffffff;font:  11pt \"Barlow-Medium\";border: 5px light black;border-radius:10px; ")
                self.outcomeTxt.addItem("Success")
                self.outcomeTxt.addItem("Faliure")
                self.outcomeTxt.addItem("Nonexistent")



        #########################################################################################################################
        #       """ rating """

                self.rate = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.rate.setGeometry(QtCore.QRect(50, 940, 501, 41))
                self.rate.setStyleSheet("background-color:#8b9dc3; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                self.rate.setText(" Client\'s confidence index")


                self.rateTxt = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                self.rateTxt.setGeometry(QtCore.QRect(590, 940, 191, 41))
                self.rateTxt.setStyleSheet(" background-color:#ffffff;font:  11pt \"Barlow-Medium\";border: 15px ;border-radius:10px; ")
                self.rateTxt.setPlaceholderText("Monthly indicator")
        
        ##################################################################################################################
        #  call duration label
                self.callDur = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.callDur.setGeometry(QtCore.QRect(50, 560, 271, 41))
                self.callDur.setStyleSheet("background-color:#8b9dc3; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                self.callDur.setText(" Last call duration")
                

                self.callDurTxt = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                self.callDurTxt.setGeometry(QtCore.QRect(360, 560, 191, 41))
                self.callDurTxt.setStyleSheet("background-color:#ffffff;font:  11pt \"Barlow-Medium\";border: 5px light black;border-radius:10px; ")
                self.callDurTxt.setPlaceholderText("in seconds")
              
                
        ####################################################################################################################
        #Background Label 

                self.backOutput = QtWidgets.QLabel(BTM)
                self.backOutput.setGeometry(QtCore.QRect(1405, 95, 731, 1080))
                self.backOutput.setStyleSheet("background-color:#34495E;")
                self.backOutput.setText("")

        ###################################################################################################################
        # """ Output Label  """
                self.outputLabel = QtWidgets.QLabel(BTM)
                self.outputLabel.setGeometry(QtCore.QRect(1480, 400, 400, 100))
                self.outputLabel.setStyleSheet("background-color: #ffffff;font: 20pt \"Arial\";border: 5px light black;border-radius:10px;")
                self.outputLabel.setText("              ...............")
                
               
                
        ####################################################################################################################
        # submit Button 

                self.Submit  = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.Submit .setGeometry(QtCore.QRect(650, 1020, 130, 45))
                self.Submit .setStyleSheet("color:#ffffff;background-color: green;font: 11pt \"Arial\";border: 5px light black;border-radius:10px;")
                self.Submit .setText("Submit")

                # Function calling 'on_click'
                self.Submit .clicked.connect(self.on_click)


        ####################################################################################################################
        #  Pdays

                self.pdaysTxt = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                self.pdaysTxt.setGeometry(QtCore.QRect(590, 820, 191, 41))
                self.pdaysTxt.setStyleSheet("background-color:#ffffff; font:  11pt \"Barlow-Medium\";border: 15px ;border-radius:10px; ")
                self.pdaysTxt.setPlaceholderText("numeric")
        

                self.pdays = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.pdays.setGeometry(QtCore.QRect(50, 820, 501, 41))
                self.pdays.setStyleSheet("background-color:#8b9dc3; font:11pt \"Barlow-Medium\";  border: 15px; border-radius:15px;")
                self.pdays.setText(" Days passing of contact from previous to this campaign")
        
        
        #####################################################################################################################

        # Submit Button
        def on_click(self):
        #         check(self)


        # def check(self):

                self.outputLabel.setText("Working in progress......")
                self.outputLabel.setStyleSheet("background-color: white;font: 20pt \"Arial\";border: 5px light black;border-radius:10px;")
                """ Dictionary of all features """

                Jobs = {0: 'Admin',
                        1:'Blue-collar',
                        2:'Enterpreneur',
                        3:'Housemaid',
                        4:'Management',
                        5:'Retired',
                        6:'Self-employed',
                        7:'Services',
                        8:'Student',
                        9:'Technician',
                        10:'Unemployed',
                        11:'Unknown'}

                Maritals = {0:'Divorced',
                        1:'Married',
                        2:'Single',
                        3:'Widow'
                }

                Educations = {0:'Basic.4y',
                        1:'Basic.6y',
                        2:'Basic.9y',
                        3:'High.school',
                        4:'Illiterate',
                        5:'Professional Course',
                        6:'University Degree',
                        7:'Unknown'
                }

                Defaults = {0:'No',
                        2:'Yes',
                        1:'Unknown'
                }

                Housing = {0:'No',
                        2:'Yes',
                        1:'Unknown'

                }

                Loans = {0:'No',
                        2:'Yes',
                        1:'Unknown'
                }

                contacts = {0:'Cellular',
                        1:'Telephone'
                }
                
                Months = {0:'Apr',
                        1:'Aug',
                        2:'Dec',
                        3:'Jul',
                        4:'Jun',
                        5:'Mar',
                        6:'May',
                        7:'Nov',
                        8:'Oct',
                        9:'Sep',
                        10:'Jan',
                        11:'Feb'
                }

                Days = {0:'Fri',
                        1:'Mon',
                        2:'Thu',
                        3:'Tue',
                        4:'Wed'
                }

                pOutcome = {0:'Failure',
                        1:'Nonexistent',
                        2:'Success'}


                """ Fetch Data from GUI """

                Age = int(self.agetxt.text())
                
                Job = str(self.jobTxt.currentText())
                
                Marital = str(self.maritalTxt.currentText())
                
                Education = str(self.eduTxt.currentText())
                
                Default = str(self.creditTxt.currentText())
                
                HouseLoan = str(self.houseTxt.currentText())
                
                Loan = str(self.loanTxt.currentText())
                
                Contact = str(self.contactTxt.currentText())
                
                Month = str(self.monthTxt.currentText())
                
                Day = str(self.dayTxt.currentText())
                
                Duration = int(self.callDurTxt.text())
                
                Campaign = int(self.duringCampaignTxt.text())
                
                Pdays =  int(self.pdaysTxt.text())
                
                previous = int(self.befCmpTxt.text())
                
                Outcome = str(self.outcomeTxt.currentText())
                
                Rate = float(self.rateTxt.text())
                
                # if Age < 15 and Age > 100:
                

                features_ = [Jobs,Maritals,Educations,Defaults,Housing,Loans,contacts,Months,Days,pOutcome]

                input_stream = [Job,Marital,Education,Default,HouseLoan,Loan,Contact,Month,Day,Outcome]
                # for _ in input_stream:
                #         print(_)

                        
                #         i=0
                #         while i < 10:
                #                 for key,values in features_[i].items():
                #                         if input_stream[i] == values :
                #                                 lst.append(key)
                #                 i += 1
                #         print(lst)
                # else:
                #         print("No")
                
                lst = []
                for (_,i) in zip(features_,input_stream):
                        # print('inside ')
                        for key,value in _.items():
                                # print('dsakjfhkjdsahkjhfkjsafkdsakjfas')
                                # print(value,'   ',i)
                                if i == value:
                                        # print("cjeckadsfds")
                                        lst.append(key)
                                        # print(key)
                                        
                       
                        

                temp1 = [0,10,11,12,13,15]
                temp2 = [Age,Duration,Campaign,Pdays,previous,Rate]

                for (index,ele) in zip(temp1,temp2):
                        lst.insert(index,ele)
                # lst.insert(0,Age)
                # lst.append[10] = Duration
                # lst.append[11] = Campaign
                # lst.append[12] = Pdays
                # lst.append[13] = previous
                # lst.append[15] = Rate
                
                lst1 = []
                lst1.append(lst)
                print(lst1)

                
                import bank_final as f
                result = f.predict(lst1)
                print(result)
                if result == 1:
                        print("Yes")
                        self.outputLabel.setText("        Client interested.")
                        self.outputLabel.setStyleSheet("color:#ffffff;background-color: green;font: 20pt \"Arial\";border: 5px light black;border-radius:10px;")
                else:
                        print("No")
                        self.outputLabel.setText("      Client not interested.")
                        self.outputLabel.setStyleSheet("color:#ffffff;background-color: red;font: 20pt \"Arial\";border: 5px light black;border-radius:10px;")
                        
                
# if __name__ == '__main__':
        
#         import sys
#         app = QtWidgets.QApplication(sys.argv)
#         Frame = QtWidgets.QMainWindow()
#         ui = BTM()
#         ui.predict_ui(Frame)
#         Frame.show()
#         sys.exit(app.exec_())
