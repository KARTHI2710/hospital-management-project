

from PyQt5 import QtCore, QtGui, QtWidgets
import main
from PyQt5.QtWidgets import QMessageBox


class Ui_LoginForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(798, 596)
        Form.showMaximized() 
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(37)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../hospitalmanagement/images/rdpl.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_18.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_18.setMaximumSize(QtCore.QSize(248, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setStyleSheet("QLineEdit\n"
"{\n"
"font-size: 15px;\n"
"    font-weight: 400;\n"
"    color: #212529;\n"
"    background-color: #ffffff;\n"
"    background-clip: padding-box;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 20px;\n"
"    padding:0px 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"border:1px solid #3F4254;\n"
"}\n"
"\n"
"")
        self.lineEdit_18.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_18.setFrame(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.verticalLayout.addWidget(self.lineEdit_18)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_19.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_19.setMaximumSize(QtCore.QSize(248, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setStyleSheet("QLineEdit\n"
"{\n"
"font-size: 15px;\n"
"    font-weight: 400;\n"
"    color: #212529;\n"
"    background-color: #ffffff;\n"
"    background-clip: padding-box;\n"
"    border: 1px solid #ced4da;\n"
"    border-radius: 20px;\n"
"    padding:0px 10px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"border:1px solid #3F4254;\n"
"}\n"
"\n"
"")
        self.lineEdit_19.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_19.setFrame(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.verticalLayout.addWidget(self.lineEdit_19)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButton_4.setMaximumSize(QtCore.QSize(165, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #0DBCC0;\n"
"    border: 0;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    border-radius: 4px;\n"
"color: #ffffff;\n"
"border: 0;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: #089598;\n"
"}\n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_4.setText(_translate("Form", "Login"))
        #self.pushButton_4.clicked.connect(lambda: self.checklogin(Form))

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.checklogin)
       # self.main_window = None
   
    def checklogin(self):
        username=self.ui.lineEdit_18.text()
        password=self.ui.lineEdit_19.text()
        if (username == '' and password == ''):
                           
            #if not self.main_window:
            self.main_window = main.MainWindow()  # Create the main window if it doesn't exist
            self.close() 
            self.main_window.show()  # Show the main window
            
        #         main_window=main.MainWindow()
        #       #  self.ui.close()
        #         main_window.show() 
        else:
             QMessageBox.warning(self.ui,"Warning","Please enter correct login or password")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
    login_window=LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
