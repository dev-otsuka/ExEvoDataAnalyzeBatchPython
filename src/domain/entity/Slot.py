import dataclasses
from domain.valueObject.SlotBaseData import *
from domain.valueObject.SingleDaySummaryData import *


@dataclasses.dataclass(frozen=True)
class Slot:
    slotBaseData: SlotBaseData
    singleDaySummaryData: SingleDaySummaryData