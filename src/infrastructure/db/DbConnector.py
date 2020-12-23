import os
import mysql.connector as mydb
from infrastructure.db.SqlManager import *

class DbConnector:
    connector = ""

    def __init__(self):
        self.connector = mydb.connect(
            host = "us-cdbr-east-02.cleardb.com",
            port = '3306',
            user = "bcf5fce91ff1e1",
            password = "55b4f5eb",
            database = "heroku_ed3a1672ba1a995",
            charset='utf8'
        )
        self.connector.ping(reconnect=True)

    def isExistSlotFromSlotId(self, slotId):
        cursor = self.connector.cursor()

        sql = getFindSlotFromSlotId(slotId)
        cursor.execute(sql)
        result = len(cursor.fetchall())

        if result >= 1:
            return True

        return False
    
    def getFindSlotFromSlotIdAndSlotName(self, slotId, slotName, coinLendingKind):
        cursor = self.connector.cursor()

        sql = getFindSlotFromAllData(slotId, slotName, coinLendingKind)
        cursor.execute(sql)
        result = len(cursor.fetchall())

        if result >= 1:
            return True

        return False


    def registSlot(self, slotId, slotName, cointLendingKind):
        cursor = self.connector.cursor()
        sql = getRegistSlot(slotId, slotName, cointLendingKind)
        cursor.execute(sql)
        self.connector.commit()

