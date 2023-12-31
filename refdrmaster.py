from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import sqlite3
import os
from addrefdr import Ui_addrefdrForm
from editrefdr import Ui_editrefdrForm


class Ui_refdrForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(832, 559)
        Form.showMaximized() 
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
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
"margin-top:10px;")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 50, -1, 30)
        self.gridLayout.setHorizontalSpacing(23)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_25.setMinimumSize(QtCore.QSize(200, 35))
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
        self.gridLayout.addWidget(self.lineEdit_25, 1, 0, 1, 1)
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
        self.gridLayout.addWidget(self.pushButton_5, 1, 3, 1, 1)
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
        self.gridLayout.addWidget(self.pushButton_4, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #5E6278;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #5E6278;")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_26.setMinimumSize(QtCore.QSize(200, 35))
        self.lineEdit_26.setMaximumSize(QtCore.QSize(250, 16777215))
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
        self.gridLayout.addWidget(self.lineEdit_26, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 4, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 380))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 4, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.fetch_and_display_refdr()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Refdr"))
        self.label.setText(_translate("Form", "RefDr Master"))
        self.pushButton_5.setText(_translate("Form", "Add RefDr"))
        self.pushButton_4.setText(_translate("Form", "search"))
        self.label_5.setText(_translate("Form", "Doctor Name"))
        self.label_6.setText(_translate("Form", "Doctor Code"))
        self.pushButton_5.clicked.connect(self.adddoctor_form)
        self.pushButton_4.clicked.connect(self.filter_refdr_data)



    def filter_refdr_data(self):
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,150)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,300)
        self.tableWidget.setColumnWidth(5,200)
        self.tableWidget.setColumnWidth(6,100)
        self.tableWidget.setColumnWidth(7,100)

        
        self.tableWidget.setHorizontalHeaderLabels(['DoctorCode','DoctorName','Qualification','Specification','Address','Mobile','Date','Actions'])
        #set header height
        vertical_header = self.tableWidget.verticalHeader()
        vertical_header.setDefaultSectionSize(40) 
       
        docname=self.lineEdit_25.text()
        code=self.lineEdit_26.text() 
        conn = sqlite3.connect('patient_data.db')
        cursor = conn.cursor()
        
        # Fetch reference data
        query="SELECT * FROM refdr where "
        parameters=[]



        if docname and code:
                query+='DoctorName like ? and DoctorCode like ?'
                parameters.extend(['%'+docname+'%','%'+code+'%'])
        elif docname:
                query+='DoctorName like ?'
                parameters.append('%'+docname+'%')
        elif code:
                query+='DoctorCode like ?'
                parameters.append('%'+code+'%')
        cursor.execute(query,parameters)
        
        refdr_data = cursor.fetchall()

        count=len(refdr_data)
        
        self.tableWidget.setRowCount(count)
        r=0
        c=0
        for row in refdr_data:
            c=0
            for col in row:
                self.tableWidget.setItem(r,c,QTableWidgetItem("   "+str(col)))
                c=c+1
            # Create a container widget to hold the "Edit" and "Delete" buttons
            button_container = QtWidgets.QWidget()
            button_layout = QtWidgets.QHBoxLayout(button_container)

            delete_button = QtWidgets.QPushButton()
            delete_button.setIcon(QtGui.QIcon(os.path.join('images', 'delete.png')))
            delete_button.setFixedSize(20, 20)
            delete_button.clicked.connect(lambda _, docid=row[0]: self.delete_refdr(docid))
            button_layout.addWidget(delete_button)

            edit_button = QtWidgets.QPushButton()
            edit_button.setIcon(QtGui.QIcon(os.path.join('images', 'edit.png')))  # Change to the correct icon
            edit_button.setFixedSize(20, 20)
            edit_button.clicked.connect(lambda _, docid=row[0]: self.edit_refdr(docid))
            button_layout.addWidget(edit_button)

            button_layout.setContentsMargins(0, 0, 0, 0)
            button_layout.setAlignment(QtCore.Qt.AlignCenter)

            # Set the container widget as a cell widget in the last column
            self.tableWidget.setCellWidget(r, c, button_container)
            r=r+1
        conn.close()

    def fetch_and_display_refdr(self):
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,150)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,300)
        self.tableWidget.setColumnWidth(5,200)
        self.tableWidget.setColumnWidth(6,100)
        self.tableWidget.setColumnWidth(7,100)

        
        self.tableWidget.setHorizontalHeaderLabels(['DoctorCode','DoctorName','Qualification','Specification','Address','Mobile','Date','Actions'])
        #set header height
        vertical_header = self.tableWidget.verticalHeader()
        vertical_header.setDefaultSectionSize(40) 


        conn=sqlite3.connect('patient_data.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM refdr")
        refdr_data = cursor.fetchall()
        count=len(refdr_data)
        
        self.tableWidget.setRowCount(count)
        r=0
        c=0
        for row in refdr_data:
            c=0
            for col in row:
                self.tableWidget.setItem(r,c,QTableWidgetItem("   "+str(col)))
                c=c+1
            # Create a container widget to hold the "Edit" and "Delete" buttons
            button_container = QtWidgets.QWidget()
            button_layout = QtWidgets.QHBoxLayout(button_container)

            delete_button = QtWidgets.QPushButton()
            delete_button.setIcon(QtGui.QIcon(os.path.join('images', 'delete.png')))
            delete_button.setFixedSize(20, 20)
            delete_button.clicked.connect(lambda _, docid=row[0]: self.delete_refdr(docid))
            button_layout.addWidget(delete_button)

            edit_button = QtWidgets.QPushButton()
            edit_button.setIcon(QtGui.QIcon(os.path.join('images', 'edit.png')))  # Change to the correct icon
            edit_button.setFixedSize(20, 20)
            edit_button.clicked.connect(lambda _, docid=row[0]: self.edit_refdr(docid))
            button_layout.addWidget(edit_button)

            button_layout.setContentsMargins(0, 0, 0, 0)
            button_layout.setAlignment(QtCore.Qt.AlignCenter)

            # Set the container widget as a cell widget in the last column
            self.tableWidget.setCellWidget(r, c, button_container)
            r=r+1
        conn.close()


    def delete_refdr(self, doc_code):
       
       # Connect to the database
       conn = sqlite3.connect('patient_data.db')
       cursor = conn.cursor()

       # Delete patient data from the database
       cursor.execute("DELETE FROM refdr WHERE DoctorCode = ?", (doc_code,))
       conn.commit()
      # self.tableWidget.clear()
       # Refresh the displayed patient data immediately after deletion
       self.fetch_and_display_refdr()


    def adddoctor_form(self):
        self.add_refdr_form = QtWidgets.QWidget()
        self.ui_addrefdr = Ui_addrefdrForm()
        self.ui_addrefdr.setupUi(self.add_refdr_form)
        self.add_refdr_form.show()
        self.ui_addrefdr.pushButton_4.clicked.connect(self.fetch_and_display_refdr)



    def edit_refdr(self, DoctorCode):
        self.edit_refdr_form = QtWidgets.QWidget()
        self.ui_edit_refdr = Ui_editrefdrForm()  # Replace with the correct class name
        self.ui_edit_refdr.setupUi(self.edit_refdr_form, DoctorCode)  # Pass the DoctorCode argument
        self.edit_refdr_form.show()

        # Fetch refdr data for the specified DoctorCode
        # refdr_data = self.fetch_refdr_data_by_id(DoctorCode)
        # if refdr_data:
        #     self.edit_refdr_form.refdr_data = refdr_data  
        
       # self.edit_refdr_form.show()
        
        self.ui_edit_refdr.pushButton_4.clicked.connect(self.fetch_and_display_refdr)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_refdrForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
