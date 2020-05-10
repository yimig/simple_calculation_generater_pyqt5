# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'peppi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 709)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:rgb(138, 186, 245)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(800, 600))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(20, 10, 20, 20)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 76))
        self.widget_3.setAutoFillBackground(False)
        self.widget_3.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setStyleSheet("font-family:Microsoft Yahei;\n"
"font-size:20pt;")
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget_6)
        self.label_2.setStyleSheet("font-family:Microsoft Yahei;\n"
"color: rgb(88, 146, 203);\n"
"font-size:20pt;")
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.ed_class = QtWidgets.QLineEdit(self.widget_6)
        self.ed_class.setStyleSheet("font-family:Microsoft Yahei;\n"
"color: rgb(18, 123, 191);\n"
"font-size:20pt;")
        self.ed_class.setObjectName("ed_class")
        self.gridLayout_5.addWidget(self.ed_class, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.widget_6, 0, 1, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.btn_generate = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_generate.sizePolicy().hasHeightForWidth())
        self.btn_generate.setSizePolicy(sizePolicy)
        self.btn_generate.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_generate.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(119, 199, 110);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:15pt;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(63, 180, 101);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(119, 199, 110);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.btn_generate.setObjectName("btn_generate")
        self.gridLayout_6.addWidget(self.btn_generate, 0, 0, 1, 1)
        self.btn_submit = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_submit.sizePolicy().hasHeightForWidth())
        self.btn_submit.setSizePolicy(sizePolicy)
        self.btn_submit.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_submit.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(232, 92, 90);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:15pt;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(223, 46, 35);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(232, 92, 90);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.btn_submit.setObjectName("btn_submit")
        self.gridLayout_6.addWidget(self.btn_submit, 0, 1, 1, 1)
        self.btn_check = QtWidgets.QPushButton(self.widget_7)
        self.btn_check.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_check.sizePolicy().hasHeightForWidth())
        self.btn_check.setSizePolicy(sizePolicy)
        self.btn_check.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_check.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(88, 146, 203);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:15pt;\n"
"}\n"
"/*\n"
"QPushButton:hover\n"
"{\n"
"    \n"
"    background-color: rgb(18, 123, 191);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(88, 146, 203);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"*/")
        self.btn_check.setObjectName("btn_check")
        self.gridLayout_6.addWidget(self.btn_check, 0, 2, 1, 1)
        self.gridLayout_7.addWidget(self.widget_7, 0, 2, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.widget_5)
        self.label.setStyleSheet("font-family:Microsoft Yahei;\n"
"color: rgb(88, 146, 203);\n"
"font-size:20pt;")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.ed_name = QtWidgets.QLineEdit(self.widget_5)
        self.ed_name.setStyleSheet("font-family:Microsoft Yahei;\n"
"color: rgb(18, 123, 191);\n"
"font-size:20pt;")
        self.ed_name.setObjectName("ed_name")
        self.gridLayout_4.addWidget(self.ed_name, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.widget_5, 0, 0, 1, 1)
        self.gridLayout_7.setColumnStretch(0, 2)
        self.gridLayout_7.setColumnStretch(1, 2)
        self.gridLayout_7.setColumnStretch(2, 1)
        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)
        self.wd_content = QtWidgets.QWidget(self.widget)
        self.wd_content.setAutoFillBackground(False)
        self.wd_content.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.wd_content.setObjectName("wd_content")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.wd_content)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.widget_8 = QtWidgets.QWidget(self.wd_content)
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_9 = QtWidgets.QWidget(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setMinimumSize(QtCore.QSize(50, 50))
        self.widget_9.setAutoFillBackground(False)
        self.widget_9.setStyleSheet("")
        self.widget_9.setObjectName("widget_9")
        self.gridLayout_3.addWidget(self.widget_9, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_8)
        self.label_3.setStyleSheet("color: rgb(119, 199, 110);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_8)
        self.lineEdit_3.setStyleSheet("color: rgb(63, 180, 101);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(50, 50))
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"    border-radius:25px;\n"
"    background-color: rgb(88, 146, 203);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:15pt;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"    \n"
"    background-color: rgb(18, 123, 191);\n"
"}\n"
"")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 3, 1, 1)
        self.gridLayout_21.addWidget(self.widget_8, 0, 0, 1, 1)
        self.widget_26 = QtWidgets.QWidget(self.wd_content)
        self.widget_26.setObjectName("widget_26")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.widget_26)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.widget_27 = QtWidgets.QWidget(self.widget_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_27.sizePolicy().hasHeightForWidth())
        self.widget_27.setSizePolicy(sizePolicy)
        self.widget_27.setMinimumSize(QtCore.QSize(50, 50))
        self.widget_27.setAutoFillBackground(False)
        self.widget_27.setStyleSheet("")
        self.widget_27.setObjectName("widget_27")
        self.gridLayout_18.addWidget(self.widget_27, 0, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.widget_26)
        self.label_24.setStyleSheet("color: rgb(119, 199, 110);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.label_24.setObjectName("label_24")
        self.gridLayout_18.addWidget(self.label_24, 0, 1, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.widget_26)
        self.lineEdit_14.setStyleSheet("color: rgb(63, 180, 101);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_18.addWidget(self.lineEdit_14, 0, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.widget_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QtCore.QSize(50, 50))
        self.label_25.setStyleSheet("QLabel\n"
"{\n"
"    border-radius:25px;\n"
"    background-color: rgb(88, 146, 203);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:15pt;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"    \n"
"    background-color: rgb(18, 123, 191);\n"
"}")
        self.label_25.setText("")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_18.addWidget(self.label_25, 0, 3, 1, 1)
        self.gridLayout_21.addWidget(self.widget_26, 0, 1, 1, 1)
        self.widget_10 = QtWidgets.QWidget(self.wd_content)
        self.widget_10.setObjectName("widget_10")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.widget_10)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.widget_15 = QtWidgets.QWidget(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy)
        self.widget_15.setMinimumSize(QtCore.QSize(50, 50))
        self.widget_15.setAutoFillBackground(False)
        self.widget_15.setStyleSheet("")
        self.widget_15.setObjectName("widget_15")
        self.gridLayout_12.addWidget(self.widget_15, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget_10)
        self.label_12.setStyleSheet("color: rgb(119, 199, 110);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.label_12.setObjectName("label_12")
        self.gridLayout_12.addWidget(self.label_12, 0, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget_10)
        self.lineEdit_8.setStyleSheet("color: rgb(63, 180, 101);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_12.addWidget(self.lineEdit_8, 0, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(50, 50))
        self.label_13.setStyleSheet("QLabel\n"
"{\n"
"    border-radius:25px;\n"
"    background-color: rgb(88, 146, 203);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:15pt;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"    \n"
"    background-color: rgb(18, 123, 191);\n"
"}")
        self.label_13.setText("")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_12.addWidget(self.label_13, 0, 3, 1, 1)
        self.gridLayout_21.addWidget(self.widget_10, 1, 0, 1, 1)
        self.widget_30 = QtWidgets.QWidget(self.wd_content)
        self.widget_30.setObjectName("widget_30")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.widget_30)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.widget_31 = QtWidgets.QWidget(self.widget_30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_31.sizePolicy().hasHeightForWidth())
        self.widget_31.setSizePolicy(sizePolicy)
        self.widget_31.setMinimumSize(QtCore.QSize(50, 50))
        self.widget_31.setAutoFillBackground(False)
        self.widget_31.setStyleSheet("")
        self.widget_31.setObjectName("widget_31")
        self.gridLayout_20.addWidget(self.widget_31, 0, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.widget_30)
        self.label_28.setStyleSheet("color: rgb(119, 199, 110);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.label_28.setObjectName("label_28")
        self.gridLayout_20.addWidget(self.label_28, 0, 1, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.widget_30)
        self.lineEdit_16.setStyleSheet("color: rgb(63, 180, 101);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_20.addWidget(self.lineEdit_16, 0, 2, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.widget_30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setMinimumSize(QtCore.QSize(50, 50))
        self.label_29.setStyleSheet("QLabel\n"
"{\n"
"    border-radius:25px;\n"
"    background-color: rgb(88, 146, 203);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:15pt;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"    \n"
"    background-color: rgb(18, 123, 191);\n"
"}")
        self.label_29.setText("")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_20.addWidget(self.label_29, 0, 3, 1, 1)
        self.gridLayout_21.addWidget(self.widget_30, 1, 1, 1, 1)
        self.widget_16 = QtWidgets.QWidget(self.wd_content)
        self.widget_16.setObjectName("widget_16")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.widget_16)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.widget_17 = QtWidgets.QWidget(self.widget_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy)
        self.widget_17.setMinimumSize(QtCore.QSize(50, 50))
        self.widget_17.setAutoFillBackground(False)
        self.widget_17.setStyleSheet("")
        self.widget_17.setObjectName("widget_17")
        self.gridLayout_13.addWidget(self.widget_17, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget_16)
        self.label_14.setStyleSheet("color: rgb(119, 199, 110);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.label_14.setObjectName("label_14")
        self.gridLayout_13.addWidget(self.label_14, 0, 1, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget_16)
        self.lineEdit_9.setStyleSheet("color: rgb(63, 180, 101);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_13.addWidget(self.lineEdit_9, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QtCore.QSize(50, 50))
        self.label_15.setStyleSheet("QLabel\n"
"{\n"
"    border-radius:25px;\n"
"    background-color: rgb(88, 146, 203);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:15pt;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"    \n"
"    background-color: rgb(18, 123, 191);\n"
"}")
        self.label_15.setText("")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_13.addWidget(self.label_15, 0, 3, 1, 1)
        self.gridLayout_21.addWidget(self.widget_16, 2, 0, 1, 1)
        self.widget_28 = QtWidgets.QWidget(self.wd_content)
        self.widget_28.setObjectName("widget_28")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.widget_28)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.widget_29 = QtWidgets.QWidget(self.widget_28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_29.sizePolicy().hasHeightForWidth())
        self.widget_29.setSizePolicy(sizePolicy)
        self.widget_29.setMinimumSize(QtCore.QSize(50, 50))
        self.widget_29.setAutoFillBackground(False)
        self.widget_29.setStyleSheet("")
        self.widget_29.setObjectName("widget_29")
        self.gridLayout_19.addWidget(self.widget_29, 0, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.widget_28)
        self.label_26.setStyleSheet("color: rgb(119, 199, 110);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.label_26.setObjectName("label_26")
        self.gridLayout_19.addWidget(self.label_26, 0, 1, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.widget_28)
        self.lineEdit_15.setStyleSheet("color: rgb(63, 180, 101);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_19.addWidget(self.lineEdit_15, 0, 2, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.widget_28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMinimumSize(QtCore.QSize(50, 50))
        self.label_27.setStyleSheet("QLabel\n"
"{\n"
"    border-radius:25px;\n"
"    background-color: rgb(88, 146, 203);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:15pt;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"    \n"
"    background-color: rgb(18, 123, 191);\n"
"}")
        self.label_27.setText("")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_19.addWidget(self.label_27, 0, 3, 1, 1)
        self.gridLayout_21.addWidget(self.widget_28, 2, 1, 1, 1)
        self.widget_18 = QtWidgets.QWidget(self.wd_content)
        self.widget_18.setObjectName("widget_18")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.widget_18)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.widget_19 = QtWidgets.QWidget(self.widget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy)
        self.widget_19.setMinimumSize(QtCore.QSize(50, 50))
        self.widget_19.setAutoFillBackground(False)
        self.widget_19.setStyleSheet("")
        self.widget_19.setObjectName("widget_19")
        self.gridLayout_14.addWidget(self.widget_19, 0, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget_18)
        self.label_16.setStyleSheet("color: rgb(119, 199, 110);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.label_16.setObjectName("label_16")
        self.gridLayout_14.addWidget(self.label_16, 0, 1, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget_18)
        self.lineEdit_10.setStyleSheet("color: rgb(63, 180, 101);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_14.addWidget(self.lineEdit_10, 0, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QtCore.QSize(50, 50))
        self.label_17.setStyleSheet("QLabel\n"
"{\n"
"    border-radius:25px;\n"
"    background-color: rgb(88, 146, 203);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:15pt;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"    \n"
"    background-color: rgb(18, 123, 191);\n"
"}")
        self.label_17.setText("")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_14.addWidget(self.label_17, 0, 3, 1, 1)
        self.gridLayout_21.addWidget(self.widget_18, 3, 0, 1, 1)
        self.widget_22 = QtWidgets.QWidget(self.wd_content)
        self.widget_22.setObjectName("widget_22")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.widget_22)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.widget_23 = QtWidgets.QWidget(self.widget_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy)
        self.widget_23.setMinimumSize(QtCore.QSize(50, 50))
        self.widget_23.setAutoFillBackground(False)
        self.widget_23.setStyleSheet("")
        self.widget_23.setObjectName("widget_23")
        self.gridLayout_16.addWidget(self.widget_23, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.widget_22)
        self.label_20.setStyleSheet("color: rgb(119, 199, 110);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.label_20.setObjectName("label_20")
        self.gridLayout_16.addWidget(self.label_20, 0, 1, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget_22)
        self.lineEdit_12.setStyleSheet("color: rgb(63, 180, 101);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_16.addWidget(self.lineEdit_12, 0, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.widget_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QtCore.QSize(50, 50))
        self.label_21.setStyleSheet("QLabel\n"
"{\n"
"    border-radius:25px;\n"
"    background-color: rgb(88, 146, 203);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:15pt;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"    \n"
"    background-color: rgb(18, 123, 191);\n"
"}")
        self.label_21.setText("")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_16.addWidget(self.label_21, 0, 3, 1, 1)
        self.gridLayout_21.addWidget(self.widget_22, 3, 1, 1, 1)
        self.widget_20 = QtWidgets.QWidget(self.wd_content)
        self.widget_20.setObjectName("widget_20")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.widget_20)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.widget_21 = QtWidgets.QWidget(self.widget_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy)
        self.widget_21.setMinimumSize(QtCore.QSize(50, 50))
        self.widget_21.setAutoFillBackground(False)
        self.widget_21.setStyleSheet("")
        self.widget_21.setObjectName("widget_21")
        self.gridLayout_15.addWidget(self.widget_21, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.widget_20)
        self.label_18.setStyleSheet("color: rgb(119, 199, 110);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.label_18.setObjectName("label_18")
        self.gridLayout_15.addWidget(self.label_18, 0, 1, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget_20)
        self.lineEdit_11.setStyleSheet("color: rgb(63, 180, 101);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_15.addWidget(self.lineEdit_11, 0, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.widget_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMinimumSize(QtCore.QSize(50, 50))
        self.label_19.setStyleSheet("QLabel\n"
"{\n"
"    border-radius:25px;\n"
"    background-color: rgb(88, 146, 203);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:15pt;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"    \n"
"    background-color: rgb(18, 123, 191);\n"
"}")
        self.label_19.setText("")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_15.addWidget(self.label_19, 0, 3, 1, 1)
        self.gridLayout_21.addWidget(self.widget_20, 4, 0, 1, 1)
        self.widget_24 = QtWidgets.QWidget(self.wd_content)
        self.widget_24.setObjectName("widget_24")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.widget_24)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.widget_25 = QtWidgets.QWidget(self.widget_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_25.sizePolicy().hasHeightForWidth())
        self.widget_25.setSizePolicy(sizePolicy)
        self.widget_25.setMinimumSize(QtCore.QSize(50, 50))
        self.widget_25.setAutoFillBackground(False)
        self.widget_25.setStyleSheet("")
        self.widget_25.setObjectName("widget_25")
        self.gridLayout_17.addWidget(self.widget_25, 0, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.widget_24)
        self.label_22.setStyleSheet("color: rgb(119, 199, 110);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.label_22.setObjectName("label_22")
        self.gridLayout_17.addWidget(self.label_22, 0, 1, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget_24)
        self.lineEdit_13.setStyleSheet("color: rgb(63, 180, 101);\n"
"font-family:Microsoft Yahei;\n"
"font-size:15pt;\n"
"font-weight:bold;")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_17.addWidget(self.lineEdit_13, 0, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.widget_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setMinimumSize(QtCore.QSize(50, 50))
        self.label_23.setStyleSheet("QLabel\n"
"{\n"
"    border-radius:25px;\n"
"    background-color: rgb(88, 146, 203);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family:Microsoft Yahei;\n"
"    font-size:15pt;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"    \n"
"    background-color: rgb(18, 123, 191);\n"
"}")
        self.label_23.setText("")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_17.addWidget(self.label_23, 0, 3, 1, 1)
        self.gridLayout_21.addWidget(self.widget_24, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.wd_content, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 5)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setStyleSheet("background-color: rgb(119, 199, 110);\n"
"border-top:5px solid #3FB465;\n"
"border-top-right-radius:30px;\n"
"border-top-left-radius:30px;")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 1)
        self.gridLayout_2.setRowStretch(0, 6)
        self.gridLayout_2.setRowStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "班级："))
        self.btn_generate.setText(_translate("MainWindow", "生成试题"))
        self.btn_submit.setText(_translate("MainWindow", "提交"))
        self.btn_check.setText(_translate("MainWindow", "查看答案"))
        self.label.setText(_translate("MainWindow", "姓名："))
        self.label_3.setText(_translate("MainWindow", "?? + ?? = "))
        self.label_24.setText(_translate("MainWindow", "?? + ?? = "))
        self.label_12.setText(_translate("MainWindow", "?? + ?? = "))
        self.label_28.setText(_translate("MainWindow", "?? + ?? = "))
        self.label_14.setText(_translate("MainWindow", "?? + ?? = "))
        self.label_26.setText(_translate("MainWindow", "?? + ?? = "))
        self.label_16.setText(_translate("MainWindow", "?? + ?? = "))
        self.label_20.setText(_translate("MainWindow", "?? + ?? = "))
        self.label_18.setText(_translate("MainWindow", "?? + ?? = "))
        self.label_22.setText(_translate("MainWindow", "?? + ?? = "))
