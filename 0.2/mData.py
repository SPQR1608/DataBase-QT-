from mDB import mDataBase
from PyQt5 import QtWidgets
from mErrorLog import ErrorLog
import mDesign
import mDrugAdd
import mDillerAdd
import mDrugDescription
import mDillerDescription
import mDrugAddDescription
import mFunctions

class App(QtWidgets.QMainWindow, mDesign.Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.mDB = mDataBase()
        self.mError = ErrorLog
        self.selectedCell = mTableWidget
        self.load_App()
        self.reloadTabBtn.clicked.connect(self.load_App)
        #self.tableWidget.cellClicked.connect(self.msg)
        self.drugAddDialog = drugApp(self)
        self.dillerAddDialog = dillerApp(self)
        self.drugDescrDialog = drugDescriptionApp(self)
        self.dillerDescrDialog = dillerDescriptionApp(self)
        self.drugAddDescriptionDialog = drugAddDescriptionApp(self)
        self.addDrugBtn.clicked.connect(self.addDrugBtn_clicked)
        self.addDillerBtn.clicked.connect(self.addDillerBtn_clicked)
        self.descriptBtn.clicked.connect(self.drugDescription_clicked)
        self.dillerBtn.clicked.connect(self.dillerDescription_clicked)
        self.addDescriptionBtn.clicked.connect(self.addDrugDescriptionBtn_clicked)

    def addDrugBtn_clicked(self):
        self.drugAddDialog.show()
        self.drugAddDialog.load_drugAddApp()

    def addDillerBtn_clicked(self):
        self.dillerAddDialog.show()
        self.dillerAddDialog.load_dillerAddApp()

    def addDrugDescriptionBtn_clicked(self):
        self.drugAddDescriptionDialog.show()
        self.drugAddDescriptionDialog.load_drugAddDescr()

    def drugDescription_clicked(self):
        try:
            drugID = self.selectedCell.viewClicked(self.tableWidget)
            data = (str(int(drugID[0]) + 1))
            query = "SELECT * FROM drug WHERE id_drug = '"+data+"'"
            row = self.mDB.select(query)
            if len(row) != 0 or str(row[0][0]) != 'None':
                self.drugDescrDialog.drugDescription(row)
                self.drugDescrDialog.show()
        except Exception as e:
            self.mError.ErrorMsg(self, 'Выберите строку')
            print(e)

    def dillerDescription_clicked(self):
        try:
            drugID = self.selectedCell.viewClicked(self.tableWidget)
            data = (str(int(drugID[0]) + 1))
            query = "SELECT dillers.id_diller, name, agent, post, adress, country, telefon, drug_name FROM dillers, drug WHERE drug.id_diller = '"+data+"' AND drug.id_diller = dillers.id_diller"
            row = self.mDB.select(query)
            if len(row) != 0 or str(row[0][0]) != 'None':
                self.dillerDescrDialog.dillerDescription(row)
            else:
                self.mError.ErrorMsg(self, 'Нет данных')
            self.dillerDescrDialog.show()
        except Exception as e:
            self.mError.ErrorMsg(self, 'Выберите строку')
            print(e)

    def load_App(self):
        colNames = []
        query = "SHOW COLUMNS FROM drug"
        rows = self.mDB.select(query)

        for i in range(0, len(rows)):
            colNames.append(rows[i][0])

        self.tableWidget.setColumnCount(len(colNames))
        self.tableWidget.setHorizontalHeaderLabels(colNames)

        query = "SELECT * FROM drug"
        rows = self.mDB.select(query)
        self.tableWidget.setRowCount(len(rows))
        row = 0
        for tup in rows:
            col = 0
            for item in tup:
                cellinfo = QtWidgets.QTableWidgetItem(str(item))
                self.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1

    '''
    def msg(self):
        row = self.view_clicked()
        rw = str(row[0])
        cl = str(row[1])
        nm = str(row[2])
        
        QtWidgets.QMessageBox.warning(
            self, 'Ошибка', rw+' '+cl+' '+nm,
            QtWidgets.QMessageBox.Yes
        )
    '''

class mTableWidget:
    def viewClicked(*table):
        tb = table[0]
        selectedCell = []
        selectedCell.append(tb.currentItem().row())
        col = tb.currentItem().column()
        selectedCell.append(col)
        selectedCell.append(tb.horizontalHeaderItem(col).text())
        return selectedCell

class drugApp(QtWidgets.QMainWindow, mDrugAdd.Ui_DrugAdd):
    def __init__(self, parent=None):
        super(drugApp, self).__init__(parent)
        self.mDB = mDataBase()
        self.mError = ErrorLog
        self.setupUi(self)
        self.drugAddBtn.clicked.connect(self.addDrugs)

    def load_drugAddApp(self):
        self.clearEdit()
        self.drugId.setText(mFunctions.load_ID('id_drug', 'drug'))

        query = "SELECT id_diller FROM dillers"
        rows = self.mDB.select(query)
        if len(rows) == 0 or str(rows[0][0]) == "None":
            self.drugDiller.addItem('Нет диллеров')
        else:
            for item in rows:
                self.drugDiller.addItem(str(item[0]))

    def addDrugs(self):
        try:
            drugID = self.drugId.text()
            drugName = self.drugName.text()
            drugDiller = self.drugDiller.currentText()
            drugUse = self.drugUse.text()
            drugCount = self.drugCount.text()
            drugPurchPrice = self.drugPurchPrice.text()
            drugSelPrice = self.drugSelPrice.text()

            query = "INSERT INTO drug(id_drug, drug_name, id_diller, id_use, kol_vo, price_zakup, price_real) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data = (drugID, drugName, drugDiller, drugUse, drugCount, drugPurchPrice, drugSelPrice)

            self.mDB.insert(query, data)

        except Exception as e:
            self.mError.ErrorMsg(self, 'Не все поля заполнены')
            print(e)

    def clearEdit(self):
        self.drugId.clear()
        self.drugName.clear()
        self.drugDiller.clear()
        self.drugUse.clear()
        self.drugCount.clear()
        self.drugPurchPrice.clear()
        self.drugSelPrice.clear()

class dillerApp(QtWidgets.QMainWindow, mDillerAdd.Ui_DillerAdd):
    def __init__(self, parent=None):
        super(dillerApp, self).__init__(parent)
        self.mDB = mDataBase()
        self.mError = ErrorLog
        self.setupUi(self)
        self.dillerAddBtn.clicked.connect(self.addDiller)

    def load_dillerAddApp(self):
        self.dillerId.setText(mFunctions.load_ID('id_diller', 'dillers'))

    def addDiller(self):
        try:
            dillerName = self.dillerName.text()
            dillerAgent = self.dillerAgent.text()
            dillerPos = self.dillerPos.text()
            dillerAddres = self.dillerAddres.text()
            dillerContry = self.dillerContry.text()
            dillerTel = self.dillerTel.text()
            dillerId = self.dillerId.text()

            query = "INSERT INTO dillers(id_diller, name, agent, post, adress, country, telefon) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data = (dillerId, dillerName, dillerAgent, dillerPos, dillerAddres, dillerContry, dillerTel)

            self.mDB.insert(query, data)

        except Exception as e:
            self.mError.ErrorMsg(self, 'Не все поля заполнены')
            print(e)

    def clearEdit(self):
        self.dillerName.clear()
        self.dillerAgent.clear()
        self.dillerPos.clear()
        self.dillerAddres.clear()
        self.dillerContry.clear()
        self.dillerTel.clear()
        self.dillerId.clear()

class drugAddDescriptionApp(QtWidgets.QMainWindow, mDrugAddDescription.Ui_drugAddDescription):
    def __init__(self, parent=None):
        super(drugAddDescriptionApp, self).__init__(parent)
        self.mDB = mDataBase()
        self.mError = ErrorLog
        self.selectedCell = mTableWidget
        self.setupUi(self)
        self.clearToAddBtn.clicked.connect(self.clearEdit)
        self.addDescriptionBtn.clicked.connect(self.addDrugDescrption)
        self.drugGroupTable.cellClicked.connect(self.drugGroupInfo)

    def load_drugAddDescr(self):
        colNames = []
        query = "SHOW COLUMNS FROM usedr"
        rows = self.mDB.select(query)
        colNames.append(rows[0][0])
        colNames.append(rows[2][0])

        self.drugGroupTable.setColumnCount(len(colNames))
        self.drugGroupTable.setHorizontalHeaderLabels(colNames)

        query = "SELECT id_use, drug_group FROM usedr"
        rows = self.mDB.select(query)
        self.drugGroupTable.setRowCount(len(rows))
        row = 0
        for tup in rows:
            col = 0
            for item in tup:
                cellinfo = QtWidgets.QTableWidgetItem(str(item))
                self.drugGroupTable.setItem(row, col, cellinfo)
                col += 1
            row += 1

    def addDrugDescrption(self):
        try:
            drugUseID = mFunctions.load_ID('id_use', 'usedr')
            drugSickID = mFunctions.load_ID('id_sick', 'sickness')
            drugGroup = self.drugGroup.text()
            drugUseCode = self.drugUseCode.text()
            drugGroupSpec = self.drugGroupSpec.toPlainText()
            drugGroupSick = self.drugGoupSick.toPlainText()

            query = "INSERT INTO usedr(id_use, use_code, drug_group, drug_specific) VALUES (%s, %s, %s, %s)"
            data = (drugUseID, drugUseCode, drugGroup, drugGroupSpec)
            self.mDB.insert(query, data)

            query = "INSERT INTO sickness(id_sick, sick_name, id_use) VALUES (%s, %s, %s)"
            data = (drugSickID, drugGroupSick, drugUseID)
            self.mDB.insert(query, data)

        except Exception as e:
            self.mError.ErrorMsg(self, 'Не все поля заполнены')
            print(e)

    def drugGroupInfo(self):
        try:
            drugGroupID = self.selectedCell.viewClicked(self.drugGroupTable)
            data = (str(int(drugGroupID[0]) + 1))
            query = "SELECT * FROM usedr, sickness WHERE usedr.id_use = '" + data + "'"
            row = self.mDB.select(query)
            print(str(row))
            self.drugGroup.setText(str(row[0][2]))
            self.drugUseCode.setText(str(row[0][1]))
            self.drugGroupSpec.setText(str(row[0][3]))
            self.drugGoupSick.setText(str(row[0][5]))
        except Exception as e:
            print(e)

    def clearEdit(self):
        self.drugGroup.clear()
        self.drugUseCode.clear()
        self.drugGroupSpec.clear()
        self.drugGoupSick.clear()

class drugDescriptionApp(QtWidgets.QMainWindow, mDrugDescription.Ui_DrugDescription):
    def __init__(self, parent=None):
        super(drugDescriptionApp, self).__init__(parent)
        self.mDB = mDataBase()
        self.mError = ErrorLog
        self.setupUi(self)
        self.activateChanges.clicked.connect(self.activateChangesChecked)
        self.saveChanges.clicked.connect(self.saveChangesBtn)

    def drugDescription(self, row):
        self.drugId.setText(str(row[0][0]))
        self.drugName.setText(str(row[0][1]))
        self.drugDiller.setText(str(row[0][2]))
        self.drugUse.setText(str(row[0][3]))
        self.drugCount.setText(str(row[0][4]))
        self.drugPurchPrice.setText(str(row[0][5]))
        self.drugSelPrice.setText(str(row[0][6]))

    def activateChangesChecked(self):
        if self.activateChanges.isChecked():
            self.drugName.setReadOnly(False)
            self.drugDiller.setReadOnly(False)
            self.drugUse.setReadOnly(False)
            self.drugCount.setReadOnly(False)
            self.drugPurchPrice.setReadOnly(False)
            self.drugSelPrice.setReadOnly(False)
            self.drugSickness.setReadOnly(False)
            self.drugSpecific.setReadOnly(False)
            self.saveChanges.setEnabled(True)
        else:
            self.drugName.setReadOnly(True)
            self.drugDiller.setReadOnly(True)
            self.drugUse.setReadOnly(True)
            self.drugCount.setReadOnly(True)
            self.drugPurchPrice.setReadOnly(True)
            self.drugSelPrice.setReadOnly(True)
            self.drugSickness.setReadOnly(True)
            self.drugSpecific.setReadOnly(True)
            self.saveChanges.setEnabled(False)

    def saveChangesBtn(self):
        try:
            drugID = self.drugId.text()
            drugName = self.drugName.text()
            drugDiller = self.drugDiller.text()
            drugUse = self.drugUse.text()
            drugCount = self.drugCount.text()
            drugPurchPrice = self.drugPurchPrice.text()
            drugSelPrice = self.drugSelPrice.text()

            query = "UPDATE drug SET drug_name = %s, id_diller = %s, id_use = %s, kol_vo = %s, price_zakup = %s, price_real = %s WHERE id_drug = %s"
            data = (drugName, drugDiller, drugUse, drugCount, drugPurchPrice, drugSelPrice, drugID)

            self.mDB.update(query, data)

        except Exception as e:
            self.mError.ErrorMsg(self, 'Не все поля заполнены')
            print(e)


class dillerDescriptionApp(QtWidgets.QMainWindow, mDillerDescription.Ui_dillerDescriprion):
    def __init__(self, parent=None):
        super(dillerDescriptionApp, self).__init__(parent)
        self.mDB = mDataBase()
        self.mError = ErrorLog
        self.setupUi(self)
        self.activateChanges.clicked.connect(self.activateChangesChecked)
        self.saveChanges.clicked.connect(self.saveChangesBtn)

    def dillerDescription(self, row):
        self.dillerName.setText(str(row[0][1]))
        self.dillerAgent.setText(str(row[0][2]))
        self.dillerPos.setText(str(row[0][3]))
        self.dillerAddres.setText(str(row[0][4]))
        self.dillerContry.setText(str(row[0][5]))
        self.dillerTel.setText(str(row[0][6]))
        self.dillerId.setText(str(row[0][0]))
        self.drugName.setText(str(row[0][7]))

    def activateChangesChecked(self):
        if self.activateChanges.isChecked():
            self.dillerName.setReadOnly(False)
            self.dillerAgent.setReadOnly(False)
            self.dillerPos.setReadOnly(False)
            self.dillerAddres.setReadOnly(False)
            self.dillerContry.setReadOnly(False)
            self.dillerTel.setReadOnly(False)
            self.saveChanges.setEnabled(True)
        else:
            self.dillerName.setReadOnly(True)
            self.dillerAgent.setReadOnly(True)
            self.dillerPos.setReadOnly(True)
            self.dillerAddres.setReadOnly(True)
            self.dillerContry.setReadOnly(True)
            self.dillerTel.setReadOnly(True)
            self.saveChanges.setEnabled(False)

    def saveChangesBtn(self):
        try:
            dillerName = self.dillerName.text()
            dillerAgent = self.dillerAgent.text()
            dillerPos = self.dillerPos.text()
            dillerAddres = self.dillerAddres.text()
            dillerContry = self.dillerContry.text()
            dillerTel = self.dillerTel.text()
            dillerId = self.dillerId.text()

            query = "UPDATE drug SET name = %s, agent = %s, post = %s, adress = %s, country = %s, telefon = %s WHERE id_diller = %s"
            data = (dillerName, dillerAgent, dillerPos, dillerAddres, dillerContry, dillerTel, dillerId)

            self.mDB.update(query, data)

        except Exception as e:
            self.mError.ErrorMsg(self, 'Не все поля заполнены')
            print(e)