from infrastructure.db.DbConnector import *

def update(slotEntityList):

    dbConnector = DbConnector()
    for slotEntity in slotEntityList:
        slotId = slotEntity.slotBaseData.slotId.value
        slotName = slotEntity.slotBaseData.slotName.value
        coinLendingKind = slotEntity.slotBaseData.coinLendingKind.value

        if dbConnector.isExistSlotFromSlotId(slotId) == False:
            ## slot登録
            dbConnector.registSlot(slotId, slotName, coinLendingKind)
