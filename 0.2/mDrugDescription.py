# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drugDescription.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DrugDescription(object):
    def setupUi(self, DrugDescription):
        DrugDescription.setObjectName("DrugDescription")
        DrugDescription.resize(728, 463)
        self.centralwidget = QtWidgets.QWidget(DrugDescription)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 320, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 220, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 270, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.drugId = QtWidgets.QLineEdit(self.centralwidget)
        self.drugId.setEnabled(True)
        self.drugId.setGeometry(QtCore.QRect(210, 30, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugId.setFont(font)
        self.drugId.setMouseTracking(True)
        self.drugId.setReadOnly(True)
        self.drugId.setObjectName("drugId")
        self.drugName = QtWidgets.QLineEdit(self.centralwidget)
        self.drugName.setEnabled(True)
        self.drugName.setGeometry(QtCore.QRect(210, 80, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugName.setFont(font)
        self.drugName.setMouseTracking(True)
        self.drugName.setReadOnly(True)
        self.drugName.setObjectName("drugName")
        self.drugCount = QtWidgets.QLineEdit(self.centralwidget)
        self.drugCount.setEnabled(True)
        self.drugCount.setGeometry(QtCore.QRect(210, 230, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugCount.setFont(font)
        self.drugCount.setMouseTracking(True)
        self.drugCount.setReadOnly(True)
        self.drugCount.setObjectName("drugCount")
        self.drugUse = QtWidgets.QLineEdit(self.centralwidget)
        self.drugUse.setEnabled(True)
        self.drugUse.setGeometry(QtCore.QRect(210, 180, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugUse.setFont(font)
        self.drugUse.setMouseTracking(True)
        self.drugUse.setReadOnly(True)
        self.drugUse.setObjectName("drugUse")
        self.drugSelPrice = QtWidgets.QLineEdit(self.centralwidget)
        self.drugSelPrice.setEnabled(True)
        self.drugSelPrice.setGeometry(QtCore.QRect(210, 330, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugSelPrice.setFont(font)
        self.drugSelPrice.setMouseTracking(True)
        self.drugSelPrice.setReadOnly(True)
        self.drugSelPrice.setObjectName("drugSelPrice")
        self.drugPurchPrice = QtWidgets.QLineEdit(self.centralwidget)
        self.drugPurchPrice.setEnabled(True)
        self.drugPurchPrice.setGeometry(QtCore.QRect(210, 280, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugPurchPrice.setFont(font)
        self.drugPurchPrice.setMouseTracking(True)
        self.drugPurchPrice.setReadOnly(True)
        self.drugPurchPrice.setObjectName("drugPurchPrice")
        self.drugDiller = QtWidgets.QLineEdit(self.centralwidget)
        self.drugDiller.setEnabled(True)
        self.drugDiller.setGeometry(QtCore.QRect(210, 130, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drugDiller.setFont(font)
        self.drugDiller.setMouseTracking(True)
        self.drugDiller.setReadOnly(True)
        self.drugDiller.setObjectName("drugDiller")
        self.activateChanges = QtWidgets.QCheckBox(self.centralwidget)
        self.activateChanges.setGeometry(QtCore.QRect(20, 390, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.activateChanges.setFont(font)
        self.activateChanges.setObjectName("activateChanges")
        self.saveChanges = QtWidgets.QPushButton(self.centralwidget)
        self.saveChanges.setGeometry(QtCore.QRect(480, 390, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveChanges.setFont(font)
        self.saveChanges.setEnabled(False)
        self.saveChanges.setObjectName("saveChanges")
        self.drugSpecific = QtWidgets.QTextBrowser(self.centralwidget)
        self.drugSpecific.setGeometry(QtCore.QRect(430, 50, 261, 141))
        self.drugSpecific.setObjectName("drugSpecific")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(460, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(520, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.drugSickness = QtWidgets.QTextBrowser(self.centralwidget)
        self.drugSickness.setGeometry(QtCore.QRect(430, 250, 261, 101))
        self.drugSickness.setObjectName("drugSickness")
        DrugDescription.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DrugDescription)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 21))
        self.menubar.setObjectName("menubar")
        DrugDescription.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DrugDescription)
        self.statusbar.setObjectName("statusbar")
        DrugDescription.setStatusBar(self.statusbar)

        self.retranslateUi(DrugDescription)
        QtCore.QMetaObject.connectSlotsByName(DrugDescription)

    def retranslateUi(self, DrugDescription):
        _translate = QtCore.QCoreApplication.translate
        DrugDescription.setWindowTitle(_translate("DrugAdd", "Описание препарата"))
        self.label.setText(_translate("DrugAdd", "Идентификатор"))
        self.label_2.setText(_translate("DrugAdd", "Название"))
        self.label_3.setText(_translate("DrugAdd", "Поставщик"))
        self.label_4.setText(_translate("DrugAdd", "Категория"))
        self.label_5.setText(_translate("DrugAdd", "Цена реализации"))
        self.label_6.setText(_translate("DrugAdd", "Количество"))
        self.label_7.setText(_translate("DrugAdd", "Цена закупочная"))
        self.activateChanges.setToolTip(_translate("DrugAdd", "Включение режима редактирования"))
        self.activateChanges.setText(_translate("DrugAdd", "Режим редактирования"))
        self.saveChanges.setText(_translate("DrugAdd", "Сохранить изменения"))
        self.label_8.setText(_translate("DrugAdd", "Описание препарата"))
        self.label_9.setText(_translate("DrugAdd", "Болезни"))

