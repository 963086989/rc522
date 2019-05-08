# encoding=utf-8

from spsb import IC
from weatherapi import Weather
from voiceapi import Voice
from example import *
import requests


# 全局参数
filename = "spsb.conf"
ic = IC()    #刷卡模块
weather = Weather(filename) # 天气模块
voice = Voice(filename) # 语音播报模块
search_url = "http://127.0.0.1:8080/spsb/search"
add_url = "http://127.0.0.1:8080/spsb/add"
del_url = "http://127.0.0.1:8080/spsb/del"


# 主程序
# 程序流程
# 三个功能，增加，删除，查询

def menu():
    print("1、刷卡")
    print("2、增加")
    print("3、删除")
    print("q、退出")
    return input("输入：")



def shuaka():
    # 获取刷卡数据
    id = ic.getData()
    # 查询数据
    r = requests.get(url=search_url, params={"data":id})
    if (r.status_code == 200):
        data = r.json()
        print(data)
        # 如果查询成功
        if (data["state"] == 1):
            string = data["user"]["name"]+"，你好。"+weather.getWeather()
            # 语音信息获取成功
            if (voice.getVoice(string)):
                # 播放最新合成的语音
                playmusic()
            else:
                # 播放出现错误的语音
                playerror()
        # 如果没有这个人
        else:
            playunregister()
    else:
        playerror()


def zhuce():
    # 获取刷卡数据
    id = ic.getData()
    name = input("输入姓名")
    # 调用注册接口
    r = requests.post(add_url, data={"data":id, "name":name})

    if (r.status_code == 200):
        data = r.json()
        print(data)
        # 注册成功
        if (data["state"] == 1):
            playsuccess()
        else:
            playerror()

def shanchu():
    id = ic.getData()
    yorn = input("(y/n):")
    if (yorn == "y"):
        r = requests.post(del_url, data={"data":id})
        if (r.status_code == 200):
            data = r.json()
            if (data["state"] == 1):
                playbay()
            else:
                print(data)
                playshebude()
        else:
            playerror()
    else:
        playjiushebude()







if __name__ == "__main__":
    while True:
        choce = menu()
        if (choce == "1"):
            print(choce)
            shuaka()
        elif (choce == "2"):
            zhuce()
        elif (choce == "3"):
            shanchu()
        elif (choce == "q"):
            playbay()
            break
        else:
            playxcl()




