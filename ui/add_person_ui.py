# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_person_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(309, 282)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 3, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.doubleSpinBox.setPrefix("")
        self.doubleSpinBox.setMinimum(0.0)
        self.doubleSpinBox.setMaximum(1000000000.0)
        self.doubleSpinBox.setSingleStep(10.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 4, 3, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 5, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.horizontalWidget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setMaxLength(11)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.horizontalLayout.addWidget(self.lineEdit_1)
        self.label_4 = QtWidgets.QLabel(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.horizontalLayout.setStretch(0, 1)
        self.gridLayout.addWidget(self.horizontalWidget, 1, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit, self.lineEdit_1)
        Form.setTabOrder(self.lineEdit_1, self.lineEdit_2)
        Form.setTabOrder(self.lineEdit_2, self.doubleSpinBox)
        Form.setTabOrder(self.doubleSpinBox, self.lineEdit_3)
        Form.setTabOrder(self.lineEdit_3, self.pushButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "添加会员"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "当前最高卡号：0"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><img src=\":/main/充值.png\" width=\"30\" height=\"30\"/><span style=\" font-size:20pt; font-weight:600; vertical-align:super;\">充值金额</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><img src=\":/main/充值.png\" width=\"30\" height=\"30\"/><span style=\" font-size:20pt; font-weight:600; vertical-align:super;\">会员类型</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "添加"))
        self.label.setText(_translate("Form", "<html><head/><body><p><img src=\":/main/姓名.png\" width=\"30\" height=\"30\"/><span style=\" font-size:20pt; font-weight:600; vertical-align:super;\">姓名</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><img src=\":/main/卡号.png\" width=\"30\" height=\"30\"/><span style=\" font-size:20pt; font-weight:600; vertical-align:super;\">卡号</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><img src=\":/main/电话.png\" width=\"30\" height=\"30\"/><span style=\" font-size:20pt; font-weight:600; vertical-align:super;\">手机号</span></p></body></html>"))
        self.label_4.setText(_translate("Form", " 0/11位"))
import images_rc
