# encoding=utf-8

from spsb import IC
from weatherapi import Weather
from voiceapi import Voice
from configparser import ConfigParser
import requests
from example import *


# 全局参数
url = "http://104.225.144.48:8080/openDoor"
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
    print("3、切换设备")
    print("q、退出")
    return input("输入：")


# 刷卡功能，其实就是往后台mac与卡号.暂时不加密。
def shuaka():
    success, icData = ic.shuaka()
    print("你的IC卡号为："+icData)
    data = {"mac":device[1], "ic":icData}
    print(data)
    response = requests.post(url, data=data)
    # 如果请求成功
    if (response.status_code == 200):
        # 判断是否能开门
        responseJson = response.json()
        # 如果有开门权限,开门播报语音
        if (responseJson['quanxian']):
            welcome = responseJson['user']['name']+"你好，欢迎进入"+responseJson['room']['name']
            print(welcome)
            voice.getVoice(welcome)
            playmusic()
        # 没有开门权限
        else:
            # 判断是不是，设备没有注册
            if (responseJson['Macregist'] == False):
                error = "设备没有注册"
                voice.getVoice(error)  # 播放语音
                playmusic()
                print(error)

            # 是不是，IC没有注册
            if (responseJson['ICregist'] == False):
                error = "IC没有注册"
                voice.getVoice(error)  # 播放语音
                playmusic()
                print(error)

            # 如果都注册了
            if (responseJson['ICregist'] and responseJson['Macregist']):
                error = responseJson['user']['name']+"你好，你没有进入"+responseJson['room']['name']+"的权限，请向管理员申请。"
                voice.getVoice(error)  # 播放语音
                playmusic()
                print(error)
    # 如果请求的网络错误了
    else:
        playerror()

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


def yubaotianqi():
    weatherstr = weather.getWeather()
    print(weatherstr)
    voice.getVoice(weatherstr)
    playmusic()


if __name__ == "__main__":
    while True:
        choce = menu()
        if (choce == '1'):
            shuaka()
        elif (choce == '2'):
            yubaotianqi()
        elif (choce == '3'):
            qiehuanshebei()
        elif (choce == 'q'):
            break
        else:
            print('输入错误，重新输入')