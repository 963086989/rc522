# coding:utf-8

import subprocess


def playsuccess():
    subprocess.Popen(['mpg123', '-q', 'audio/success.mp3']).wait()

# 播放最新的语音
def playmusic():
    subprocess.Popen(['mpg123', '-q', 'audio/x_xiaoyuan.mp3']).wait()

# 播放出现错误的语音
def playerror():
    subprocess.Popen(['mpg123', '-q', 'audio/error.mp3']).wait()

# 播放测试语音
def playtest():
    subprocess.Popen(['mpg123', '-q', 'audio/test.mp3']).wait()

# 播放没有注册语音
def playunregister():
    subprocess.Popen(['mpg123', '-q', 'audio/unregister.mp3']).wait()

def playbay():
    subprocess.Popen(['mpg123', '-q', 'audio/baybay.mp3']).wait()

def playshebude():
    subprocess.Popen(['mpg123', '-q', 'audio/shebude.mp3']).wait()

def playjiushebude():
    subprocess.Popen(['mpg123', '-q', 'audio/jiushebude.mp3']).wait()

def playxcl():
    subprocess.Popen(['mpg123', '-q', 'audio/xcl.mp3']).wait()