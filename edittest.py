from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_edittestForm(object):
    def setupUi(self, Form, testcode):
        self.f=Form
        self.conn = sqlite3.connect("patient_data.db")
        self.cursor = self.conn.cursor() 
        Form.setObjectName("Form")
        Form.resize(814, 534)
        Form.showMaximized() 
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(20, 50, -1, -1)
        self.gridLayout.setHorizontalSpacing(47)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #5E6278;")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #5E6278;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #5E6278;")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(Form)
        self.lineEdit_25.setMinimumSize(QtCore.QSize(200, 35))
        self.lineEdit_25.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_25.setFont(font)
        self.lineEdit_25.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_25.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_25.setFrame(True)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout.addWidget(self.lineEdit_25, 2, 0, 1, 1)
        self.lineEdit_27 = QtWidgets.QLineEdit(Form)
        self.lineEdit_27.setMinimumSize(QtCore.QSize(200, 35))
        self.lineEdit_27.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_27.setFont(font)
        self.lineEdit_27.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_27.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_27.setFrame(True)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout.addWidget(self.lineEdit_27, 2, 2, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(Form)
        self.lineEdit_26.setMinimumSize(QtCore.QSize(200, 35))
        self.lineEdit_26.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_26.setFont(font)
        self.lineEdit_26.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_26.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_26.setFrame(True)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout.addWidget(self.lineEdit_26, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 50, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButton_7.setMaximumSize(QtCore.QSize(165, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #0DBCC0;\n"
"    border: 0;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    border-radius: 4px;\n"
"color: #ffffff;\n"
"border: 0;\n"
"margin-right:10px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: #089598;\n"
"}\n"
"\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButton_6.setMaximumSize(QtCore.QSize(165, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton\n"
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
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setMinimumSize(QtCore.QSize(5, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setSizeIncrement(QtCore.QSize(3, 3))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: #181C32;\n"
"margin-top:10px;")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Testcode = testcode
        self.populate_test_data()


    def populate_test_data(self):
        if self.Testcode:
            # Fetch patient data for the specified patient_id
            test_data = self.fetch_test_data_by_id(self.Testcode)
            if test_data:
                # Populate the form fields with the patient data
                self.lineEdit_25.setText(str(test_data[0]))
                self.lineEdit_26.setText(test_data[1])  # Assuming the second item is the title
                self.lineEdit_27.setText(test_data[2])  # Assuming the third item is the patient name
                
                
    def fetch_test_data_by_id(self, Testcode):
        self.cursor.execute("SELECT * FROM tests WHERE Testcode=?", (Testcode,))
        test_data = self.cursor.fetchone()
        return test_data            
    

    def clear_input_fields_test(self):
        self.lineEdit_25.clear()
        self.lineEdit_26.clear()
        self.lineEdit_27.clear()

    def save_test_data(self):
        try:
            Testcode = self.lineEdit_25.text()
            TestName = self.lineEdit_26.text()
            specimentype = self.lineEdit_27.text()
            
    
            # Insert patient data into the database
            self.cursor.execute("UPDATE tests SET  TestName=?, specimentype=? WHERE Testcode=? ",
                                (TestName, specimentype,Testcode))
            self.conn.commit()
    
            # Clear the input fields after saving
            self.clear_input_fields_test()
            self.f.close()

        except Exception as e:
            print("Error:", str(e))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "Specimen Type"))
        self.label_5.setText(_translate("Form", "Test Code "))
        self.label_6.setText(_translate("Form", "Test Name"))
        self.pushButton_7.setText(_translate("Form", "Save"))
        self.pushButton_6.setText(_translate("Form", "Close"))
        self.label.setText(_translate("Form", "Add Test"))
        self.pushButton_7.clicked.connect(self.save_test_data)
        self.pushButton_6.clicked.connect(self.closeform)

    def closeform(self):
        self.f.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_edittestForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())