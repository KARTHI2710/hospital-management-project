

from PyQt5 import QtCore, QtGui, QtWidgets
from patientmaster import  Ui_PatientMasterForm
from reportresult import Ui_reportresultForm
from refdrmaster import Ui_refdrForm
from testmaster import Ui_testmasterForm
from pathologistmaster import Ui_pathologistForm
#from login import Ui_LoginForm


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.showMaximized() 
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFront_Desk = QtWidgets.QMenu(self.menubar)
        self.menuFront_Desk.setObjectName("menuFront_Desk")
        self.menuMaster = QtWidgets.QMenu(self.menubar)
        self.menuMaster.setObjectName("menuMaster")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuLogout = QtWidgets.QMenu(self.menubar)
        self.menuLogout.setObjectName("menuLogout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRegistration_Summary = QtWidgets.QAction(MainWindow)
        self.actionRegistration_Summary.setObjectName("actionRegistration_Summary")
        self.actionRefDr_Master = QtWidgets.QAction(MainWindow)
        self.actionRefDr_Master.setObjectName("actionRefDr_Master")
        self.actionTest_Master = QtWidgets.QAction(MainWindow)
        self.actionTest_Master.setObjectName("actionTest_Master")
        self.actionReport_Master = QtWidgets.QAction(MainWindow)
        self.actionReport_Master.setObjectName("actionReport_Master")
        self.actionPathologist_Master = QtWidgets.QAction(MainWindow)
        self.actionPathologist_Master.setObjectName("actionPathologist_Master")
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        self.menuFront_Desk.addAction(self.actionRegistration_Summary)
        self.menuMaster.addAction(self.actionRefDr_Master)
        self.menuMaster.addAction(self.actionTest_Master)
        self.menuMaster.addAction(self.actionReport_Master)
        self.menuMaster.addAction(self.actionPathologist_Master)
        self.menuLogout.addAction(self.actionLogout)
        self.menubar.addAction(self.menuFront_Desk.menuAction())
        self.menubar.addAction(self.menuMaster.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuLogout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFront_Desk.setTitle(_translate("MainWindow", "Front Desk"))
        self.menuMaster.setTitle(_translate("MainWindow", "Master"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuLogout.setTitle(_translate("MainWindow", "Logout"))
        self.actionRegistration_Summary.setText(_translate("MainWindow", "Registration Summary"))
        self.actionRefDr_Master.setText(_translate("MainWindow", "RefDr Master"))
        self.actionTest_Master.setText(_translate("MainWindow", "Test Master"))
        self.actionReport_Master.setText(_translate("MainWindow", "Report Master"))
        self.actionPathologist_Master.setText(_translate("MainWindow", "Pathologist Master"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.patient_master_frame = QtWidgets.QFrame()
        self.patient_master_ui = Ui_PatientMasterForm()# patient master
        self.patient_master_ui.setupUi(self.patient_master_frame)
    
        self.add_refdr_frame = QtWidgets.QFrame()
        self.add_refdr_ui = Ui_refdrForm()# refdr master
        self.add_refdr_ui.setupUi(self.add_refdr_frame)
        
        self.add_testmaster_frame = QtWidgets.QFrame()
        self.add_testmaster_ui = Ui_testmasterForm()# Test master
        self.add_testmaster_ui.setupUi(self.add_testmaster_frame)
        
        self.reportformat_frame = QtWidgets.QFrame()
        self.reportformat_ui = Ui_reportresultForm()# report format
        self.reportformat_ui.setupUi(self.reportformat_frame)
        
        self.pathologist_frame = QtWidgets.QFrame()
        self.pathologist_ui = Ui_pathologistForm()# pathology
        self.pathologist_ui.setupUi(self.pathologist_frame)


        
        

        self.ui.actionRegistration_Summary.triggered.connect(self.show_patient_master_frame)
        self.ui.actionRefDr_Master.triggered.connect(self.show_refdr_frame)
        self.ui.actionTest_Master.triggered.connect(self.show_testmaster_frame) 
        self.ui.actionReport_Master.triggered.connect(self.show_reportformat_frame)
        self.ui.actionPathologist_Master.triggered.connect(self.show_pathologist_frame)
        self.ui.actionLogout.triggered.connect(self.show_logout_frame)
        
        # Create a QStackedWidget to manage the frames
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)
        
        
        
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        self.stacked_widget.addWidget(self.ui.centralwidget)
        self.stacked_widget.addWidget(self.patient_master_frame)
        self.stacked_widget.addWidget(self.add_refdr_frame)
        self.stacked_widget.addWidget(self.add_testmaster_frame)
        self.stacked_widget.addWidget(self.reportformat_frame)
        self.stacked_widget.addWidget(self.pathologist_frame)
        self.setCentralWidget(self.stacked_widget)
    
        self.show_patient_master_frame()


    def show_pathologist_frame(self):
        self.stacked_widget.setCurrentWidget(self.pathologist_frame)
    

    def show_patient_master_frame(self):
        self.stacked_widget.setCurrentWidget(self.patient_master_frame)
        
    def show_refdr_frame(self):
        self.stacked_widget.setCurrentWidget(self.add_refdr_frame)    

    def show_testmaster_frame(self):
        self.stacked_widget.setCurrentWidget(self.add_testmaster_frame) 
       
    def show_reportformat_frame(self):
         self.stacked_widget.setCurrentWidget(self.reportformat_frame)     

    def show_logout_frame(self):
        self.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()

    main_window=MainWindow()
    main_window.show()
    sys.exit(app.exec_())
