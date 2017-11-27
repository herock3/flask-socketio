from selenium import webdriver
import time
from flask import Flask
from datetime import datetime

app=Flask(__name__)

def getfigure():
    try:
        browser = webdriver.PhantomJS("E:/installer/python_lib/phantomjs/bin/phantomjs.exe")
        print("上证指数")
        url = "https://gupiao.baidu.com/"
        browser.get(url)
        browser.implicitly_wait(5)

        situation=[]
        # datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        # datetime=time.mktime(time.localtime())
        situation.append(str(datetime))
        figure = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/div[1]/div/span[1]')
        situation.append(str(figure.text))
        evaluate = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/div[1]/div/span[2]')
        situation.append(str(evaluate.text))
        # timeTuple = datetime.strptime(situation[0], '%Y-%m-%d %H:%M:%S')
        # year = str(situation[0])[0:4]
        # month = str(situation[0])[5:7]
        # day = str(situation[0])[8:10]
        # hour = str(situation[0])[11:13]
        # minute = str(situation[0])[14:16]
        # second = str(situation[0])[17:]
        # print(year + month + day + hour + minute + second)
        # t = datetime(int(year),int(month),int(day),int(hour),int(minute),int(second))
        index = situation[1]
        change_value = str(situation[2]).split('(')[0]
        change_ratio=str(situation[2]).split('(')[1].split('%')[0]
        data=[float(index),float(change_value),float(change_ratio)]
        print(data)
        return data
    except Exception as e:
        print("获取数据出现异常！将在一分钟之后重试……")
        print("Exception：" + str(e))
        time.sleep(60)
        getfigure()



def getdata():
    while True:
        list=getfigure()
        return list

if __name__ == '__main__':
    getfigure()
     # print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(list[0])))
    # print(time.mktime(time.localtime()))
    # print(time.time())
    # print(time.localtime())
    # situation=['2017-09-02 20:30:11',13]
    # timeTuple = datetime.strptime(situation[0], '%Y-%m-%d %H:%M:%S')
    # print(timeTuple)
    # year = str(situation[0])[0:4]
    # month = str(situation[0])[5:7]
    # day = str(situation[0])[8:10]
    # hour = str(situation[0])[11:13]
    # minute = str(situation[0])[14:16]
    # second = str(situation[0])[17:]
    # print(year+month+day+hour+minute+second)

    # print(len(list[0]))

    # print(year)