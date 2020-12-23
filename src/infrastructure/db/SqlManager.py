
def getFindSlotFromSlotId(slotId):
    return """
      SELECT * 
      FROM slot
      WHERE slot_id = {slot_id};
    """.format(slot_id = slotId).strip()

def getFindSlotFromAllData(slotId, slotName, coinLendingKind):
    return """
      SELECT * 
      FROM slot
      WHERE slot_id = {slot_id}
      AND slot_name = '{slot_name}'
      AND coin_lending_kind = '{coin_lending_kind}';
    """.format(slot_id = slotId, slot_name = slotName, coin_lending_kind = coinLendingKind).strip()


def getRegistSlot(slotId, slotName, coinLendingKind):
    return """
      INSERT INTO
      slot VALUES('',{slot_id}, 1, '{slot_name}', '{coin_lending_kind}');
    """.format(slot_id = slotId, slot_name = slotName, coin_lending_kind = coinLendingKind).strip()
