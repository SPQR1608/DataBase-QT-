# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dillerDescription.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dillerDescriprion(object):
    def setupUi(self, dillerDescriprion):
        dillerDescriprion.setObjectName("dillerDescriprion")
        dillerDescriprion.resize(718, 485)
        self.centralwidget = QtWidgets.QWidget(dillerDescriprion)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 350, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 250, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 300, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.dillerName = QtWidgets.QLineEdit(self.centralwidget)
        self.dillerName.setGeometry(QtCore.QRect(220, 60, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dillerName.setFont(font)
        self.dillerName.setReadOnly(True)
        self.dillerName.setObjectName("dillerName")
        self.dillerAgent = QtWidgets.QLineEdit(self.centralwidget)
        self.dillerAgent.setGeometry(QtCore.QRect(220, 110, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dillerAgent.setFont(font)
        self.dillerAgent.setReadOnly(True)
        self.dillerAgent.setObjectName("dillerAgent")
        self.dillerContry = QtWidgets.QLineEdit(self.centralwidget)
        self.dillerContry.setGeometry(QtCore.QRect(220, 260, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dillerContry.setFont(font)
        self.dillerContry.setReadOnly(True)
        self.dillerContry.setObjectName("dillerContry")
        self.dillerAddres = QtWidgets.QLineEdit(self.centralwidget)
        self.dillerAddres.setGeometry(QtCore.QRect(220, 210, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dillerAddres.setFont(font)
        self.dillerAddres.setReadOnly(True)
        self.dillerAddres.setObjectName("dillerAddres")
        self.dillerId = QtWidgets.QLineEdit(self.centralwidget)
        self.dillerId.setGeometry(QtCore.QRect(220, 360, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dillerId.setFont(font)
        self.dillerId.setReadOnly(True)
        self.dillerId.setObjectName("dillerId")
        self.dillerTel = QtWidgets.QLineEdit(self.centralwidget)
        self.dillerTel.setGeometry(QtCore.QRect(220, 310, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dillerTel.setFont(font)
        self.dillerTel.setReadOnly(True)
        self.dillerTel.setObjectName("dillerTel")
        self.saveChanges = QtWidgets.QPushButton(self.centralwidget)
        self.saveChanges.setEnabled(False)
        self.saveChanges.setGeometry(QtCore.QRect(430, 400, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.saveChanges.setFont(font)
        self.saveChanges.setObjectName("saveChanges")
        self.dillerPos = QtWidgets.QLineEdit(self.centralwidget)
        self.dillerPos.setGeometry(QtCore.QRect(220, 160, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dillerPos.setFont(font)
        self.dillerPos.setReadOnly(True)
        self.dillerPos.setObjectName("dillerPos")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(440, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.drugName = QtWidgets.QLabel(self.centralwidget)
        self.drugName.setGeometry(QtCore.QRect(540, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.drugName.setFont(font)
        self.drugName.setObjectName("drugName")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(130, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.activateChanges = QtWidgets.QCheckBox(self.centralwidget)
        self.activateChanges.setGeometry(QtCore.QRect(30, 410, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.activateChanges.setFont(font)
        self.activateChanges.setObjectName("activateChanges")
        dillerDescriprion.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(dillerDescriprion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 718, 21))
        self.menubar.setObjectName("menubar")
        dillerDescriprion.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(dillerDescriprion)
        self.statusbar.setObjectName("statusbar")
        dillerDescriprion.setStatusBar(self.statusbar)

        self.retranslateUi(dillerDescriprion)
        QtCore.QMetaObject.connectSlotsByName(dillerDescriprion)

    def retranslateUi(self, dillerDescriprion):
        _translate = QtCore.QCoreApplication.translate
        dillerDescriprion.setWindowTitle(_translate("dillerDescriprion", "Описание поставщика"))
        self.label.setText(_translate("dillerDescriprion", "Название"))
        self.label_2.setText(_translate("dillerDescriprion", "Представитель"))
        self.label_3.setText(_translate("dillerDescriprion", "Должность"))
        self.label_4.setText(_translate("dillerDescriprion", "Адрес"))
        self.label_5.setText(_translate("dillerDescriprion", "Идентификатор"))
        self.label_6.setText(_translate("dillerDescriprion", "Страна"))
        self.label_7.setText(_translate("dillerDescriprion", "Телефон"))
        self.saveChanges.setText(_translate("dillerDescriprion", "Сохранить изменения"))
        self.label_8.setText(_translate("dillerDescriprion", "Препарат :   "))
        self.drugName.setText(_translate("dillerDescriprion", "TextLabel"))
        self.label_9.setText(_translate("dillerDescriprion", "Поставщик"))
        self.activateChanges.setToolTip(_translate("dillerDescriprion", "Включение режима редактирования"))
        self.activateChanges.setText(_translate("dillerDescriprion", "Режим редактирования"))

