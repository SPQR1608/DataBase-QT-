import sys

from PyQt5 import QtWidgets

import mData

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = mData.App()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
    #mDB = mDataBase()
    #query = "UPDATE test SET testcol1 = 'tesqwasdfe564' WHERE idtest = 3 "
    #query = "INSERT INTO test(testcol1) VALUES ('testasdq')"
    #rw = mDB.update(query)