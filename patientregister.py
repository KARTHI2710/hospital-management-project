

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox
import sqlite3
import datetime

class Ui_addpatientForm(object):
    def setupUi(self, Form):
        self.f=Form
        self.conn = sqlite3.connect("patient_data.db")
        #Form.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)
        Form.showMaximized() 
        self.cursor = self.conn.cursor()
        Form.setObjectName("Form")
        Form.resize(746, 512)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(-1, -1, 30, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(9)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox.setStyleSheet("QComboBox\n"
"\n"
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
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 7, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #5E6278;")
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 3, 1, 1)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_24.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_24.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_24.setFont(font)
        self.lineEdit_24.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_24.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_24.setFrame(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout_2.addWidget(self.lineEdit_24, 4, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #5E6278;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: #5E6278;")
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 5, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_3.setMaximumSize(QtCore.QSize(165, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 8, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setEnabled(True)
        self.label.setMinimumSize(QtCore.QSize(5, 5))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setSizeIncrement(QtCore.QSize(3, 3))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: #181C32;")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #5E6278;")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 3, 1, 1)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_30.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_30.setMaximumSize(QtCore.QSize(250, 16777215))
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
        self.gridLayout_2.addWidget(self.lineEdit_30, 4, 1, 1, 1)
        self.lineEdit_28 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_28.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_28.setMaximumSize(QtCore.QSize(250, 16777215))
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
        self.gridLayout_2.addWidget(self.lineEdit_28, 4, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_2.setMaximumSize(QtCore.QSize(165, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 8, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #5E6278;")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #5E6278;")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_31.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_31.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_31.setFont(font)
        self.lineEdit_31.setStyleSheet("QLineEdit\n"
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
        self.lineEdit_31.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_31.setFrame(True)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.gridLayout_2.addWidget(self.lineEdit_31, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #5E6278;")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: #5E6278;")
        self.label_32.setObjectName("label_32")
        self.gridLayout_2.addWidget(self.label_32, 5, 1, 1, 1)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_27.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_27.setMaximumSize(QtCore.QSize(250, 16777215))
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
        self.gridLayout_2.addWidget(self.lineEdit_27, 2, 2, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_25.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_25.setMaximumSize(QtCore.QSize(250, 16777215))
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
        self.gridLayout_2.addWidget(self.lineEdit_25, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #5E6278;")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #5E6278;")
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 2, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 70))
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.listWidget.setStyleSheet("width:10px;\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 7, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox_2.setStyleSheet("QComboBox\n"
"\n"
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
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 2, 3, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox_3.setStyleSheet("QComboBox\n"
"\n"
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
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_2.addWidget(self.comboBox_3, 6, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox_4.setStyleSheet("QComboBox\n"
"\n"
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
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_2.addWidget(self.comboBox_4, 6, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.fetch_latest_patient_number()
        latest_patient_number = self.fetch_latest_patient_number()
        next_patient_number = self.generate_next_patient_number(latest_patient_number)
        self.lineEdit_25.setText(next_patient_number)

        self.fetch_latest_accession_number()
        latest_accession_number = self.fetch_latest_accession_number()
        next_accession_number = self.generate_next_accession_number(latest_accession_number)


        # Populate comboBox_25 with data from the database
        refdr_data = self.fetch_refdr_from_database()
        self.comboBox_3.addItems(refdr_data)

        selecttest_data = self.fetch_selecttest_from_database()
        self.comboBox_4.addItems(selecttest_data)

        self.pushButton.clicked.connect(self.add_selected_test_to_list)

                
        refdr_data = self.fetch_refdr_from_database()
        self.populate_refdrdropdown(self.comboBox_3, refdr_data)  # Use your populate function
        
        # Populate comboBox_26 with data from the database
        selecttest_data = self.fetch_selecttest_from_database()
        self.populate_testdropdown(self.comboBox_4, selecttest_data)


    def add_selected_test_to_list(self):
        selected_test = self.comboBox_4.currentText()
        if selected_test:
                self.listWidget.addItem(selected_test)


    def fetch_latest_patient_number(self):
        try:
            self.cursor.execute("SELECT MAX(uhid) FROM patients")
            latest_test_number = self.cursor.fetchone()[0]
            return latest_test_number
        except Exception as e:
            print("Error fetching latest patient number:", str(e))
            return None

    def generate_next_patient_number(self, latest_patient_number):
        if latest_patient_number is None:
            return "P00001"

        prefix = "P"
        numeric_part = int(latest_patient_number[1:])  # Convert the numeric part to integer
        next_numeric_part = numeric_part + 1
        next_patient_number = f"{prefix}{next_numeric_part:05}"  # Format as "T00001"
        return next_patient_number
    
    def fetch_latest_accession_number(self):
        try:
            self.cursor.execute("SELECT MAX(accession) FROM patients")
            latest_test_number = self.cursor.fetchone()[0]
            return latest_test_number
        except Exception as e:
            print("Error fetching latest patient number:", str(e))
            return None
    
    
    def generate_next_accession_number(self, latest_accession_number):
        if latest_accession_number is None:
            return "100001"
    
        numeric_part = int(latest_accession_number)
        next_numeric_part = numeric_part + 1
        next_accession_number = str(next_numeric_part).zfill(6)
        return next_accession_number
    
    def save_accession_data(self):
        try:
            DoctorCode = self.generate_next_accession_number()
            # ... rest of your save_test_data function ...

        except Exception as e:
            print("Error:", str(e))
    
    
    def save_patient_data(self):
        try:
            DoctorCode = self.generate_next_patient_number()
            # ... rest of your save_test_data function ...

        except Exception as e:
            print("Error:", str(e))
    
    
    
    def fetch_refdr_from_database(self):
    # Connect to your database
      connection = sqlite3.connect("patient_data.db")
      cursor = connection.cursor()
  
      # Fetch categories from the "category" table
      cursor.execute("SELECT * FROM refdr")
      refdr = cursor.fetchall()
     
      # Close the connection
      connection.close()
  
      return [refdrs[1] for refdrs in refdr]
    
      
    def fetch_selecttest_from_database(self):
       connection = sqlite3.connect("patient_data.db")
       cursor = connection.cursor()
  
       # Fetch data from the "tests" table
       cursor.execute("SELECT * FROM tests")
       tests = cursor.fetchall()

       # Print the fetched data for debugging
  
       connection.close()
  
       return [test[1] for test in tests]
    
    def populate_refdrdropdown(self, combo_box, data):
        combo_box.clear()
        combo_box.addItems(data)
    
    def populate_testdropdown(self, combo_box, data):
        combo_box.clear()
        combo_box.addItems(data) 
    

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "Mr"))
        self.comboBox.setItemText(1, _translate("Form", "Mrs"))
        self.comboBox.setItemText(2, _translate("Form", "Others"))
        self.pushButton.setText(_translate("Form", "Add"))
        self.label_11.setText(_translate("Form", "Mobile"))
        self.label_5.setText(_translate("Form", "UHID"))
        self.label_31.setText(_translate("Form", "Ref Dr"))
        self.pushButton_3.setText(_translate("Form", "Save"))
        self.label.setText(_translate("Form", "Add Patient"))
        self.label_8.setText(_translate("Form", "Gender"))
        self.pushButton_2.setText(_translate("Form", "Close"))
        self.label_7.setText(_translate("Form", "Patient Name"))
        self.label_10.setText(_translate("Form", "DOB"))
        self.label_6.setText(_translate("Form", "Title"))
        self.label_32.setText(_translate("Form", "Select Test"))
        self.label_9.setText(_translate("Form", "Age"))
        self.label_12.setText(_translate("Form", "Email ID"))
        self.comboBox_2.setItemText(0, _translate("Form", "Male"))
        self.comboBox_2.setItemText(1, _translate("Form", "Female"))
        self.comboBox_2.setItemText(2, _translate("Form", "Others"))
        self.pushButton_3.clicked.connect(self.save_patient_data)
        self.pushButton_2.clicked.connect(Form.close)


    
    def clear_input_fields(self):
        self.lineEdit_25.clear()
     #  self.lineEdit_29.clear()
        self.lineEdit_27.clear()
        self.lineEdit_31.clear()
        self.lineEdit_30.clear()
      #  self.lineEdit_20.clear()
        self.lineEdit_24.clear()
        self.lineEdit_28.clear()
        self.comboBox_3.clear()
        self.comboBox_4.clear()



    def save_patient_data(self):
     

     try:
        uhid = self.lineEdit_25.text()
        title = self.comboBox.currentText()
        patientname = self.lineEdit_27.text()
        dob = self.lineEdit_31.text()
        age = self.lineEdit_30.text()
        gender = self.comboBox_2.currentText()
        mobile = self.lineEdit_24.text()
        email = self.lineEdit_28.text()
        refdr = self.comboBox_3.currentText()
        selected_test = self.comboBox_4.currentText()
        
        # Uncomment the code to fetch the latest accession number
        latest_accession_number = self.fetch_latest_accession_number()
        accession = self.generate_next_accession_number(latest_accession_number)

        # Insert patient data into the database
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.strftime("%d%m%Y")

        self.cursor.execute("INSERT INTO patients (uhid, title, patientname, dob, age, gender, mobile, email, date, refdr, selected_test, accession) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (uhid, title, patientname, dob, age, gender, mobile, email, current_date, refdr, selected_test,accession))
        self.conn.commit()

      
        self.f.close()
        # Clear the input fields after saving
        self.clear_input_fields()
       
        
     except sqlite3.Error as e:
        print("Error:", str(e))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_addpatientForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
