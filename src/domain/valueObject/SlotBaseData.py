import dataclasses
from infrastructure.utility import Trim
from infrastructure.enum.CoinLendingKind import *


@dataclasses.dataclass(frozen=True)
class SlotId:
    value: int

@dataclasses.dataclass(frozen=True)
class SlotName:
    value: str

@dataclasses.dataclass(frozen=True)
class CoinLendingKind:
    value: str

@dataclasses.dataclass(frozen=True)
class SlotDetailSiteUrl:
    value: str

@dataclasses.dataclass(frozen=True)
class SlotBaseData:
    slotId: SlotId
    slotName: SlotName
    coinLendingKind: CoinLendingKind
    slotDetailSiteUrl: SlotDetailSiteUrl