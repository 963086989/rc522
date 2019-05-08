import requests
from configparser import ConfigParser

class Weather(object):
    def __init__(self, filename):
        # 读取配置文件
        self.conf = ConfigParser()
        self.conf.read(filename)
        self.__KEY = self.conf.get("weather", "key")
        self.__URL = "https://restapi.amap.com/v3/weather/weatherInfo"
        self.__IPURL = "https://restapi.amap.com/v3/ip"
        # 默认的城市代码"411100"
        self.city = None
        # 默认读取当前时间的天气
        self.extensions = "base"

    # 获取本地的代码
    def getCity(self):
        params = {"key":self.__KEY}
        r = requests.get(self.__IPURL, params=params)
        if (r.status_code == 200):
            json = r.json()
            if (json["status"] == "1"):
                return json["adcode"]


    def flush(self, city = None):
        if (self.city == None):
            self.city = self.getCity()

        param = {
            "city": self.city,
            "key": self.__KEY,
            "extensions": self.extensions,
        }
        response = requests.get(self.__URL, params=param)
        data = response.json()
        if (data["status"] == "1") :
            self.data = data
            return True
        else:
            return False

    # 天气信息整理
    def getWeather(self):
        if (self.flush()):
            self.weather = \
                self.data['lives'][0]["province"]\
                + self.data['lives'][0]["city"]+"，现在是"\
                + self.data['lives'][0]["weather"]+"天，温度是"\
                + self.data['lives'][0]['temperature']+"度，"\
                + self.data['lives'][0]['winddirection']+"风"\
                + self.data['lives'][0]['windpower']+"级，湿度是"\
                + self.data['lives'][0]['humidity']+"，每天都要有好心情呀！"
            return self.weather
        else:
            return "天气获取失败"



if __name__ == "__main__":
    weather = Weather("spsb.conf")
    print (weather.getWeather())
