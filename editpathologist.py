

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import datetime
import sqlite3

class Ui_editpathologistForm(object):
    def setupUi(self, Form,pid):
        self.code=pid
        self.f=Form
        self.conn = sqlite3.connect("patient_data.db")
        self.cursor = self.conn.cursor()  
        Form.setObjectName("Form")
        Form.resize(846, 565)
        Form.showMaximized() 
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
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
"margin-top:15px;")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
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
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButton_5.setMaximumSize(QtCore.QSize(165, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 4, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 100, -1, 30)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("color: #5E6278;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(20, 29))
        self.pushButton.setMaximumSize(QtCore.QSize(117, 16777215))
        self.pushButton.setStyleSheet("QPushButton\n"
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
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #5E6278;")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #5E6278;")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #5E6278;")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_25.sizePolicy().hasHeightForWidth())
        self.lineEdit_25.setSizePolicy(sizePolicy)
        self.lineEdit_25.setMinimumSize(QtCore.QSize(100, 35))
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
        self.gridLayout.addWidget(self.lineEdit_25, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #5E6278;")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #5E6278;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEdit_28 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_28.setMinimumSize(QtCore.QSize(200, 35))
        self.lineEdit_28.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_28.setFont(font)
        self.lineEdit_28.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_28.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_28.setFrame(True)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout.addWidget(self.lineEdit_28, 3, 3, 1, 1)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_27.setMinimumSize(QtCore.QSize(200, 35))
        self.lineEdit_27.setMaximumSize(QtCore.QSize(400, 16777215))
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
        self.gridLayout.addWidget(self.lineEdit_27, 3, 2, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_26.setMinimumSize(QtCore.QSize(200, 35))
        self.lineEdit_26.setMaximumSize(QtCore.QSize(400, 16777215))
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
        self.gridLayout.addWidget(self.lineEdit_26, 3, 1, 1, 1)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_30.setMinimumSize(QtCore.QSize(200, 35))
        self.lineEdit_30.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_30.setFont(font)
        self.lineEdit_30.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_30.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_30.setFrame(True)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.gridLayout.addWidget(self.lineEdit_30, 6, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #5E6278;")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit.setStyleSheet("QLineEdit\n"
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
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 6, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_29.sizePolicy().hasHeightForWidth())
        self.lineEdit_29.setSizePolicy(sizePolicy)
        self.lineEdit_29.setMinimumSize(QtCore.QSize(200, 35))
        self.lineEdit_29.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_29.setFont(font)
        self.lineEdit_29.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_29.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_29.setFrame(True)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.verticalLayout.addWidget(self.lineEdit_29)
        self.gridLayout.addLayout(self.verticalLayout, 6, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 2)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)


        self.populate_pathologist_data()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.selectImage)
        self.pushButton_4.clicked.connect(self.save_pathologist_data)
        self.pushButton_5.clicked.connect(self.closeform)

    def closeform(self):
        self.f.close()


    def selectImage(self):
       options = QFileDialog.Options()
       options |= QFileDialog.ReadOnly
       options |= QFileDialog.HideNameFilterDetails
       options |= QFileDialog.DontUseNativeDialog

       file_path, _ = QFileDialog.getOpenFileName(self.f, "Select Image File", "", "Image Files (*.png *.jpg *.bmp *.gif);;All Files (*)", options=options)

       if file_path:
           # Set the selected image file path in the QLineEdit
           self.lineEdit.setText(file_path)


 

    def clear_input_fields(self):
        self.lineEdit_25.clear()
        self.lineEdit_28.clear()
        self.lineEdit_26.clear()
        self.lineEdit_27.clear()
        self.lineEdit_29.clear()
        self.lineEdit_30.clear()
        self.lineEdit.clear()

    def populate_pathologist_data(self):
        if self.code:
            # Fetch patient data for the specified patient_id
            pathologist_data = self.fetch_pathologist_data_by_id(self.code)
            if pathologist_data:
                # Populate the form fields with the patient data
                self.lineEdit_25.setText(str(pathologist_data[0]))
                self.lineEdit_26.setText(pathologist_data[1])  # Assuming the second item is the title
                self.lineEdit_27.setText(pathologist_data[2])  # Assuming the third item is the patient name
                self.lineEdit_28.setText(pathologist_data[3])
                self.lineEdit_29.setText(pathologist_data[4])
                self.lineEdit_30.setText(pathologist_data[5])
                self.lineEdit.setText(str(pathologist_data[7]))
                
                
    def fetch_pathologist_data_by_id(self, code):
        self.cursor.execute("SELECT * FROM pathologist WHERE DoctorCode=?", (code,))
        pathologist_data = self.cursor.fetchone()
        return pathologist_data    
        
     
    def save_pathologist_data(self):
        DoctorCode = self.lineEdit_25.text()
        DoctorName = self.lineEdit_26.text()
        Qualification = self.lineEdit_27.text()
        Specialisation = self.lineEdit_28.text()
        Address = self.lineEdit_29.text()
        signature = self.lineEdit.text()
        Mobile = self.lineEdit_30.text()
        
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.strftime("%d%m%Y")

        # Insert patient data into the database
        self.cursor.execute("UPDATE pathologist SET  DoctorName=?, Qualification=?, Specialisation=?, Address=?,  Mobile=?, signature=?,date = ? WHERE DoctorCode=?", 
                            ( DoctorName, Qualification, Specialisation, Address, Mobile,signature,current_date,DoctorCode))
        self.conn.commit()

        # Clear the input fields after saving
        self.clear_input_fields()
        self.f.close()



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Add Pathologist"))
        self.pushButton_4.setText(_translate("Form", "Save"))
        self.pushButton_5.setText(_translate("Form", "Close"))
        self.label_2.setText(_translate("Form", "Signature"))
        self.pushButton.setText(_translate("Form", "Add Signature"))
        self.label_8.setText(_translate("Form", "Specalization"))
        self.label_7.setText(_translate("Form", "Qualification"))
        self.label_9.setText(_translate("Form", "Address"))
        self.label_6.setText(_translate("Form", "Doctor Name"))
        self.label_5.setText(_translate("Form", "Doctor Code"))
        self.label_10.setText(_translate("Form", "Mobile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_editpathologistForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
