import requests
from bs4 import BeautifulSoup

url = "https://daidata.goraggio.com/100231/all_list?ps=S&hist_num=0"

# 全台データ
allDataHtml = requests.get(url)
allDataObject = BeautifulSoup(allDataHtml.content, "html.parse")

for individualContents in allDataObject.find_all("a", class_="Text-UnderLine"):
    print(individualContents.text)