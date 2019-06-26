from mDB import mDataBase

def load_ID(idRow, table):
    try:
        mDB = mDataBase()
        query = "SELECT max(" + idRow +") FROM " + table + ""
        row = mDB.select(query)
        if len(row) == 0 or str(row[0][0]) == "None":
            rID = '1'
        else:
            rID = str(int(row[0][0]) + 1)
        return rID
    except Exception as e:
        print(e)
