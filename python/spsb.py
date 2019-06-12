#coding:utf-8
import signal
import time
import sys
from pirc522 import RFID

class IC(object):
    def __init__(self):
        self.run = True
        self.rdr = RFID()
    
    def __del__(self):
        self.rdr.cleanup()
        print("over")
    
    def shuaka(self):
        self.rdr.wait_for_tag()
        (error, data) = self.rdr.request()
        if not error:
            print(data)
            print("\nDetected: " + format(data, "02x"))
            (error, uid) = self.rdr.anticoll()
            if not error:
                print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
                data = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
                return True, data

    def getData(self):
        while True:
            success, data = self.shuaka()
            if (success):
                return data
if __name__ == "__main__":
    ic = IC()
    print(ic.getData())
