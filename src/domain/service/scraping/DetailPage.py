import requests, sys, os, time, datetime, re
from bs4 import BeautifulSoup

from domain.valueObject.SlotBaseData import *
from domain.valueObject.SingleDaySummaryData import *
from domain.entity.Slot import *
from infrastructure.utility import Trim

def getSlotDetailDataList(slotBaseDataList):

    resultArray = []
    for slotBaseDataObject in slotBaseDataList:
        detailUrl = slotBaseDataObject.slotDetailSiteUrl.value

        html = requests.get(detailUrl)
        htmlObject = BeautifulSoup(html.content, "lxml")

        # BB/REG
        bigBonus = BigBonusCount(Trim.execute(htmlObject.select_one("td", class_="Text-Big25 Text-Red").text))
        regBonus = RegularBonusCount(Trim.execute(htmlObject.select_one("td", class_="Text-Big19 ").text))

        # Sum/Avg
        sumTable = htmlObject.find_all("table", class_="overviewTable3")[0]
        maxPayout = MaxPayout(Trim.execute(sumTable.find_all("tr")[0].find_all("td")[0].text))
        totalPlaycount = TotalPlayCount(Trim.execute(sumTable.find_all("tr")[0].find_all("td")[1].text))
        totalAverage = TotalAverage(Trim.execute(sumTable.find_all("tr")[1].find_all("td")[1].text))
        bigBonusAverage = BigBonusAverage(Trim.execute(sumTable.find_all("tr")[2].find_all("td")[0].text))
        regBonusAverage = RegularBonusAverage(Trim.execute(sumTable.find_all("tr")[2].find_all("td")[1].text))

        # script(detail payout graph data)
        ## search string
        now = datetime.datetime.now()
        now = now.strftime('%Y-%m-%d')

        detailGraphData = ""
        scriptList = htmlObject.find_all("script")
        for script in scriptList:
            scriptSplitArray = script.prettify().split(";")
            for singleScript in scriptSplitArray:
                if now in singleScript and "var data = [[[" in singleScript:
                    singleScript = singleScript.replace("var data = [[","")
                    singleScript = singleScript.replace("]]","")
                    detailGraphData = GraphTransition(Trim.execute(singleScript))

        singleDaySummaryData = SingleDaySummaryData(bigBonus, regBonus, maxPayout, totalPlaycount, totalAverage, bigBonusAverage, regBonusAverage, detailGraphData)

        resultArray.append(Slot(slotBaseDataObject, singleDaySummaryData))

    return resultArray

