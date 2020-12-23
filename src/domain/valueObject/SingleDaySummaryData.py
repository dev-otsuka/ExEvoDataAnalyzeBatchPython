import dataclasses
from infrastructure.utility import Trim

@dataclasses.dataclass(frozen=True)
class BigBonusCount:
    value: str

@dataclasses.dataclass(frozen=True)
class RegularBonusCount:
    value: int

@dataclasses.dataclass(frozen=True)
class TotalPlayCount:
    value: int

@dataclasses.dataclass(frozen=True)
class MaxPayout:
    value: int

@dataclasses.dataclass(frozen=True)
class TotalAverage:
    value: str

@dataclasses.dataclass(frozen=True)
class BigBonusAverage:
    value: str

@dataclasses.dataclass(frozen=True)
class RegularBonusAverage:
    value: str

@dataclasses.dataclass(frozen=True)
class GraphTransition:
    value: str

@dataclasses.dataclass(frozen=True)
class SingleDaySummaryData:
    bigBonusCount: BigBonusCount
    regularBonusCount: RegularBonusCount
    totalPlayCount: TotalPlayCount
    maxPayout: MaxPayout
    totalAverage: TotalAverage
    bigBonusAverage: BigBonusAverage
    regularBonusAverage: RegularBonusAverage
    graphTransition: GraphTransition
