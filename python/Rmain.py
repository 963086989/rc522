# encoding=utf-8

from spsb1 import IC
from weatherapi import Weather
from voiceapi import Voice
from configparser import ConfigParser
import requests
from example import *


# 全局参数
url = "104.225.144.48:8080/openDoor"
filename = "spsb.conf"
ic = IC()    #刷卡模块
weather = Weather(filename) # 天气模块
voice = Voice(filename) # 语音播报模块
devices = None
device = None


# 初始化工作,读取全部设备，并且设定第一个为启动设备，如果没有设备列表，则打印错误。退出程序
conf = ConfigParser()
try:
    conf.read('devices.conf')
    devices = conf.items('devices')
    if (devices == []):
        raise Exception('没有一个设备')
    else:
        device = devices[0]
except Exception as e:
    print(e)
    exit(-1)


# 主程序，选择设备（虚拟设备）
def menu():
    print('虚拟设备，可以自由选择切换设备。')
    print("1、刷卡")
    print("2、预报本地天气")
    print("2、切换设备")
    print("q、退出")
    return input("输入：")


# 刷卡功能，其实就是往后台mac与卡号.暂时不加密。
def shuaka():
    icData = ic.shuaka()

    data = {"mac":device[1], "ic":icData}
    response = requests.post(url, data=data)
    responseJson = response.json()
    print(responseJson)

# 切换设备
def qiehuanshebei():
    global device
    print('当前选择的设备为：'+str(device))
    print('设备列表：')
    for i,temp in enumerate(devices):
        print(str(i)+' : '+temp[0]+" : "+temp[1])

    xz = input('请选择：')
    try:
        if (int(xz) < len(devices)):
            device = devices[int(xz)]
        else:
            raise Exception('选择错误')
    except Exception as e:
        print(e)



if __name__ == "__main__":
    print('当前设备为：' + device[0] + " : " + device[1])
    qiehuanshebei()
    print('当前设备为：' + device[0] + " : " + device[1])