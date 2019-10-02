import requests
from bs4 import BeautifulSoup
from peewee import *
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

db = SqliteDatabase('air.db')
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Air(BaseModel):
    date = CharField()
    year = IntegerField()
    month = IntegerField()
    day = IntegerField()
    aqi = IntegerField()
    rank = CharField()
    pm25 = IntegerField()
    pm10 = IntegerField()
    so2 = IntegerField()
    co = FloatField()
    no2 = IntegerField()
    o3 = IntegerField()

    class Meta:
        db_table = 'air'


# db.create_tables([Air])

html = requests.get(url='https://www.aqistudy.cn/historydata/monthdata.php?city=%E5%8C%97%E4%BA%AC')
content = html.content
page = BeautifulSoup(content, 'html.parser')
linkaera = page.find('ul', class_="unstyled1")
links = linkaera.find_all('a')

for link in range(1, 10):
    if link >= 10:
        realink = 'https://www.aqistudy.cn/historydata/daydata.php?city=北京&month=2019' + str(link)
    else:
        realink = 'https://www.aqistudy.cn/historydata/daydata.php?city=北京&month=20190' + str(link)
    print(realink)
    browser = webdriver.Chrome()
    # browser.implicitly_wait(10)
    while True:

        browser.get(realink)
        time.sleep(2)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        lists = soup.find_all('tr')
        if len(lists) > 1:
            break

    for list in lists:
        items = list.find_all('td')
        if len(items) == 0:
            continue
        try:
            str1 = Air.get(Air.date == items[0].text)
            if str1 == 0:
                continue
        except:
            pass

        ddate = items[0].text.split('-')
        print(ddate)
        i = Air.create(date=items[0].text, year=ddate[0], month=ddate[1], day=ddate[2], aqi=items[1].text,
                       rank=items[2].text, pm25=items[3].text, pm10=items[4].text, so2=items[5].text, co=items[6].text,
                       no2=items[7].text, o3=items[8].text)
    browser.close()
