import dataclasses
from infrastructure.utility.Trim import *

@dataclasses.dataclass(frozen=True)
class BigBonusCount:
    value: int

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
class SingleDaySummaryData:
    bigBonusCount: BigBonusCount
    regularBonusCount: RegularBonusCount
    totalPlayCount: TotalPlayCount
    maxPayout: MaxPayout
    totalAverage: TotalAverage
    bigBonusAverage: BigBonusAverage
    regularBonusAverage: RegularBonusAverage

    def __init__(self, bigBonusCount: BigBonusCount, regularBonusCount: RegularBonusCount, totalPlayCount: TotalPlayCount, maxPayout: MaxPayout, totalAverage: TotalAverage, bigBonusAverage: BigBonusAverage, regularBonusAverage: RegularBonusAverage):
        self.bigBonusCount = Trim.execute(bigBonusCount)
        self.regularBonusCount = Trim.execute(regularBonusCount)
        self.totalPlayCount = Trim.execute(totalPlayCount)
        self.maxPayout = Trim.execute(maxPayout)
        self.totalAverage = Trim.execute(totalAverage)
        self.bigBonusAverage = Trim.execute(bigBonusAverage)
        self.regularBonusAverage = Trim.execute(regularBonusAverage)

