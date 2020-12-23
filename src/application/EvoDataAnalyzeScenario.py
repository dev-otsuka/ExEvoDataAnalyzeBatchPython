import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from domain.service.scraping.TopPage import *
from domain.service.scraping.DetailPage import *
from domain.service.dataStore.SlotDataManage import *


class EvoDataAnalyzeScenario:

    def execute(self):
        # スクレイピング
        slotEntityList = self.scraping()
        # データ管理
        update(slotEntityList)

    def scraping(self):
        slotBaseDataList =  getSlotBaseDataList()
        return getSlotDetailDataList(slotBaseDataList)
