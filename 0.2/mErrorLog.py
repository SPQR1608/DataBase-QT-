from PyQt5 import QtWidgets

class ErrorLog:
    def ErrorMsg(self, Message):
        QtWidgets.QMessageBox.warning(
            self, 'Ошибка', Message,
            QtWidgets.QMessageBox.Yes
        )