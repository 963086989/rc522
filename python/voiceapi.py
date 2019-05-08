# coding:utf-8

import requests
import time
import hashlib
import base64
from configparser import ConfigParser

class Voice(object):
    def __init__(self, filename):
        self.conf = ConfigParser()
        self.conf.read(filename)
        #  合成webapi接口地址
        self.__URL = "http://api.xfyun.cn/v1/service/v1/tts"
        #  音频编码(raw合成的音频格式pcm、wav,lame合成的音频格式MP3)
        self.__AUE = "lame"
        #  应用APPID（必须为webapi类型应用，并开通语音合成服务，参考帖子如何创建一个webapi应用：http://bbs.xfyun.cn/forum.php?mod=viewthread&tid=36481
        self._APPID = self.conf.get("voice", "appid")
        #  接口密钥（webapi类型应用开通合成服务后，控制台--我的应用---语音合成---相应服务的apikey）
        self._API_KEY = self.conf.get("voice", "apikey")
        self.name = self.conf.get("voice", "name")

    # 组装http请求头
    def getHeader(self):
        curTime = str(int(time.time()))
        param = "{\"aue\":\"" + self.__AUE + "\",\"auf\":\"audio/L16;rate=16000\",\"voice_name\":\"" + self.name+ "\",\"engine_type\":\"intp65\"}"
        paramBase64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')
        m2 = hashlib.md5()
        m2.update((self._API_KEY + curTime + paramBase64).encode('utf-8'))
        checkSum = m2.hexdigest()

        header = {
            'X-CurTime': curTime,
            'X-Param': paramBase64,
            'X-Appid': self._APPID,
            'X-CheckSum': checkSum,
            'X-Real-Ip': '127.0.0.1',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        }
        print(header)
        return header

    def getBody(self, text):
        data = {'text': text}
        return data

    def writeFile(self, file, content):
        with open(file, 'wb') as f:
            f.write(content)
        f.close()

    def getVoice(self, text):
        r = requests.post(self.__URL, headers=self.getHeader(), data=self.getBody(text))

        contentType = r.headers['Content-Type']
        if contentType == "audio/mpeg":
            sid = r.headers['sid']
            if self.__AUE == "raw":
                #   合成音频格式为pcm、wav并保存在audio目录下
                self.writeFile("audio/" + self.name + ".wav", r.content)
            else:
                #   合成音频格式为mp3并保存在audio目录下
                self.writeFile("audio/" + self.name + ".mp3", r.content)
            print("success, name = " + self.name)
            return True
        else:
            #   错误码链接：https://www.xfyun.cn/document/error-code （code返回错误码时必看）
            print(r.text)
            return False

if __name__ == "__main__":
    voice = Voice("spsb.conf")
    voice.getVoice("真的要离开了吗？")
