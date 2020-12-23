import requests, sys, os
from bs4 import BeautifulSoup

from domain.valueObject.SlotBaseData import *
from infrastructure.utility import Trim

TOP_PAGE_URL = "https://daidata.goraggio.com/100231/all_list?ps=S&hist_num=0"

def getSlotBaseDataList():

    # 結果格納配列
    resultArray = []

    # 全台データ
    html = requests.get(TOP_PAGE_URL)
    htmlObject = BeautifulSoup(html.content, "lxml")

    allSlotTable = htmlObject.select_one("table", class_="sorter tablesorter")
    tableBody = allSlotTable.find("tbody")

    for singleSlotData in tableBody.find_all("tr"):
        # 台番号取得
        id = SlotId(Trim.execute(singleSlotData.select_one("a", class_="Text-UnderLine").text))
        siteUrl = SlotDetailSiteUrl(Trim.execute(singleSlotData.select_one("a", class_="Text-UnderLine").get('href')))
        lendingKind = CoinLendingKind(Trim.execute(singleSlotData.find_all("td")[2].text))
        name = SlotName(Trim.execute(singleSlotData.find_all("td")[3].text))

        resultArray.append(SlotBaseData(id, name, lendingKind, siteUrl))

    return resultArray