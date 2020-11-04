import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from domain.service.scraping.TopPage import *

class EvoDataAnalyzeScenario:

    def execute(self):
        # スクレイピング
        self.topPageScraping()

    def topPageScraping(self):
        getSlotBaseDataList()
