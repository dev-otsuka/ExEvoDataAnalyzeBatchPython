from enum import Enum

class SingleDaySummaryDataColumn(Enum):
    BigBonus = "BB"
    RegularBonus = "RB"
    PlayCountFromBeforeBonus = "スタート回数"
    TotalPlayCount = "累計スタート"
    MaxPayout = "最大持玉"
    TotalAverage = "合成確率"
    BigBonusAverage = "BB確率"
    RegularBonusAverage = "RB確率"
