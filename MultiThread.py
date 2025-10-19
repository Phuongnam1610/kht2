from main import *
from PyQt5.QtCore import QThread
from file import *
tools=[]
threads=[]

devices = get_connected_devices()


def Ham(u):
        for i in tools:
            i.terminate()
        # for item in devicessl:
        for i in tools:
            i.u=u
            i.start()

def stoptool():
        for i in tools:
            i.terminate()


class MyThread(QThread,toolLQ):
    # Tạo một tín hiệu để gửi thông báo từ thread con đến thread chính

    def __init__(self,u,udid,index):
        super().__init__(udid=udid,index=index)
        self.u=u
        

    def run(self):
        self.main()


listtd=open("listtd.txt").readlines()
for i,v in enumerate(devices):
    a=MyThread(0,v,index=i)
    tools.append(a)