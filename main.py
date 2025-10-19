from adb import *
import numpy as np
pkgame="com.tepaylink.kiemhieptinh2mobile"
pkgame2="com.tepaylink.kiemhieptinh2mobile/org.cocos2dx.cpp.AppActivity"

class toolLQ():
    def __init__(self,udid,index):
        self.udid=udid    
        self.index=index
    



    def loadgame(self):
        closeGame(self.udid,pkgame)
        time.sleep(1)
        moGame(self.udid,pkgame2)
        time.sleep(8)
    
    def dungdi(self):
        for i in range(50):
            # click(self.udid, 856,110 ,"map")
            # if (findFor(self.udid, 5, "dichuyen.png", 0)!= 0):
                # for i in range(50):
                    sc=screen_capture(self.udid)
                    if(find2(sc,"loadgame.png",threshold=0.94)!=0):
                        time.sleep(5)
                        print('dang load')
                        continue
                    sc1=sc[41:52,829:880]
                    time.sleep(2)
                    sc2=screen_capture(self.udid)[18:65,802:896]
                    
                    if(find3(sc2,sc1,threshold=0.99)!=0):
                        print('da ket thuc di chuyen')
                        time.sleep(1)
                        return True
            # else:
                # findFor(self.udid, 1, "nutx.png", 1,threshold=0.85)    

        return False
                    
                    
                
    
    def phu(self):

        for i in range(5):
            if(findFor(self.udid, 1, "phu.png", 1)!= 0):
                time.sleep(10)
                if (findFor(self.udid, 5, "dailyphu.png", 0,threshold=0.8)!= 0):
                    return True
            else:
                click(self.udid,916 ,384 )
                time.sleep(1)
        return False
    
    def chuduocdiem(self):
        
        for i in range(5):
            click(self.udid, 856,110 ,"map")
            if (findFor(self.udid, 5, "dichuyen.png", 0)!= 0):
                click(self.udid, 575, 310,"chuduocdiem")
                self.dungdi()
                for i in range(3):
                    click(self.udid,814,212,"Thoai")
                    time.sleep(1)
                    if (findFor(self.udid, 1, "hanhtrang.png", 0)!= 0):
                        return self.bando()
                    
                return False
            else:
                findFor(self.udid, 1, "nutx.png", 1,threshold=0.85)    
    
    def vDL(self):
        self.tatauto()
        for i in range(5):
            click(self.udid, 856,110 ,"map")
            if (findFor(self.udid, 5, "dichuyen.png", 0)!= 0):
                click(self.udid, 133, 454,"giangtamthon")
                time.sleep(2)
                click(self.udid, 228,530 )
                time.sleep(2)
                click(self.udid, 575, 310,"chuduocdiem")
                self.dungdi()
                break
        
        return True
        
                    
    
    def update_value(self,o,y=1):
        vthang = (o - 1) // 5 + 1
        vtcot = (o - 1) % 5 + 1
        x=int(vtcot*54.8-(54.8/2))
        y=int(vthang*52.75-(52.75/2))
        return (x+496,y+153)
    def update_value2(self,o,y=1):
        vthang = (o - 1) // 5 + 1
        vtcot = (o - 1) % 5 + 1
        x=int(vtcot*54.8-(54.8/2))
        y=int(vthang*52.75-(52.75/2))
        return (x+494,y+43)
    
    def locdo(self):
        # y=False
        # for i in range(5):
        #     click(self.udid, 608, 515,"hanh trang")
        #     time.sleep(2)
        #     if (findFor(self.udid, 1, "hanhtrang.png", 0)!= 0):
        #         y=True
        # if(y==False):
        #     return False
        sc=screen_capture(self.udid)
        listcanxoa=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]        
        listnull=find2(sc[153:368,496:760],"otrong.png",threshold=0.75)
        listsdo=find2(sc[153:368,496:760],"sachdo.png",threshold=0.65)
        if(listnull!=0):            
            for i in listnull:
                vtcot=(i[0]+(54.8/2))/54.8
                vtcot=round(vtcot)
                print(vtcot)
                vthang=(i[1]+(52.75/2))/52.75
                vthang=round(vthang)
                print(vthang)
                o=(vthang - 1) * 5 + vtcot
                if(o in listcanxoa):
                    listcanxoa.remove(o)
        if(listsdo!=0):
            for i in listsdo:
                vtcot=(i[0]+(54.8/2))/54.8
                vtcot=round(vtcot)
                print(vtcot)
                vthang=(i[1]+(52.75/2))/52.75
                vthang=round(vthang)
                print(vthang)
                o=(vthang - 1) * 5 + vtcot
                if(o in listcanxoa):
                    listcanxoa.remove(o)
        print(listcanxoa)
        updated_arr = list(map(self.update_value, listcanxoa))
        print(updated_arr)
        return (updated_arr)
    
    def locdo2(self):
        sc=screen_capture(self.udid)
        listcanxoa=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]        
        listnull=find2(sc[43:368,494:760],"otrong.png",threshold=0.75)
        listsdo=find2(sc[43:368,494:760],"sachdo.png",threshold=0.65)
        if(listnull!=0):            
            for i in listnull:
                vtcot=(i[0]+(54.8/2))/54.8
                vtcot=round(vtcot)
                print(vtcot)
                vthang=(i[1]+(52.75/2))/52.75
                vthang=round(vthang)
                print(vthang)
                o=(vthang - 1) * 5 + vtcot
                if(o in listcanxoa):
                    listcanxoa.remove(o)
        if(listsdo!=0):

            for i in listsdo:
                vtcot=(i[0]+(54.8/2))/54.8
                vtcot=round(vtcot)
                print(vtcot)
                vthang=(i[1]+(52.75/2))/52.75
                vthang=round(vthang)
                print(vthang)
                o=(vthang - 1) * 5 + vtcot
                if(o in listcanxoa):
                    listcanxoa.remove(o)
        print(listcanxoa)
        updated_arr = list(map(self.update_value2, listcanxoa))
        print(updated_arr)
        return (updated_arr)

            
    def findC(self,image,count=5,c=1):
        if(findFor(self.udid,img=image,n=count,yclick=c)!=0):
            return True
        else:
            return False
 
    def bando(self):
        
        for i in range(5):
            click(self.udid, 116,357,"ban nhanh" )
            time.sleep(1)
            if (findFor(self.udid, 3, "bannhanh.png", 0)!= 0):
                for i in range(2):
                    click(self.udid,787,126,"o so 1")
                time.sleep(3)
                    # if (findFor(self.udid, 3, "selecto1.png", 0,threshold=1)!= 0):
                listcx=self.locdo()
                for i in reversed(listcx):
                    click(self.udid, i[0],i[1] )
                    click(self.udid, i[0],i[1] )
                    time.sleep(0.5)
                    click(self.udid, 899, 491,"vienht")
                    click(self.udid, 899, 491,"vienht")
                time.sleep(1)
                
                for i in range(2):
                    click(self.udid,786,268,"o so 2")
                time.sleep(3)
                listcx=self.locdo2()
                for i in reversed(listcx):
                    click(self.udid, i[0],i[1] )
                    click(self.udid, i[0],i[1] )
                    time.sleep(0.5)
                    click(self.udid, 899, 491,"vienht")
                    click(self.udid, 899, 491,"vienht")
                    
                click(self.udid, 917, 27,"nutx")
                
                return True
        return False
            
    def lenbai(self):
        for i in range(5):
            click(self.udid, 856,110 ,"map")
            if (findFor(self.udid, 5, "dichuyen.png", 0)!= 0):
                click(self.udid, 811, 137,"giang tam thon")
                self.dungdi()
                swipe(self.udid,83,446,142,330,5000)
                time.sleep(2)
                self.dungdi()
                swipe(self.udid,83,446,177,396,5000)
                return True
                
        return False
    def vaoTD(self):
        for i in range(5):
            click(self.udid, 856,110 ,"map")
            if (findFor(self.udid, 5, "dichuyen.png", 0)!= 0):
                click(self.udid, self.index[0],self.index[1],"toado")
                time.sleep(3)
                self.dungdi()
                return True
            
        return False

    def batauto(self):
        click(self.udid,916 ,209 )
        for i in range(5):
            if (findFor(self.udid, 1, "dangbatauto.png", 0)!= 0):
                return True
            else:
                click(self.udid, 864, 209)
                time.sleep(1)
    def tatauto(self):
        click(self.udid,916 ,209 )
        for i in range(5):
            if (findFor(self.udid, 1, "dangbatauto.png", 0)== 0):
                swipe(self.udid,83,446,142,330,1000)
                return True
            else:
                click(self.udid, 864, 209)
                time.sleep(1)
        
        
    def checkMap(self):
        for i in range(5):
            click(self.udid, 856,110 ,"map")
            if (findFor(self.udid, 5, "dichuyen.png", 0)!= 0):
                for i in range(5):
                    if (findFor(self.udid, 1, "pmd2.png", 0)!= 0):
                        return 1
                    if (findFor(self.udid, 1, "dailyphu.png", 0)!= 0):
                        return 0  
                click(self.udid,903,29,"nutx")
                          
        return False
    def train(self):
        start_time = time.time()

        while True:
            # Kiểm tra thời gian hiện tại
            current_time = time.time()
            
            # Tính thời gian đã trôi qua
            elapsed_time = current_time - start_time
            
            # Kiểm tra nếu đã đến 20 phút
            if elapsed_time >= 1200:  # 20 phút = 1200 giây
                break
            if (findFor(self.udid, 1, "vethanh.png", 1)!= 0):
                 if(self.lenbai()==True):
                    self.vaoTD()
                    self.batauto()  
            else:
                if(findFor(self.udid,3,"fulldo.png",threshold=0.85,yclick=0))==0:
                    if(self.vDL()==True):
                        for i in range(3):
                            click(self.udid,814,212,"Thoai")
                            time.sleep(1)
                            if (findFor(self.udid, 1, "hanhtrang.png", 0)!= 0):
                                if(self.bando()==True):
                                    if(self.lenbai()==True):
                                        self.vaoTD()
                                        self.batauto()   
                                        break
            
    def dieptuhinh(self):
        self.tatauto()
        for i in range(2):
            click(self.udid, 856,110 ,"map")
            if (findFor(self.udid, 5, "dichuyen.png", 0)!= 0):
                click(self.udid, 133, 454,"giangtamthon")
                time.sleep(2)
                click(self.udid, 228,530 )
                time.sleep(2)
                click(self.udid, 575, 310,"chuduocdiem")
                self.dungdi()
                break
        
        return True
        
    def main(self):
        while True:
            self.loadgame()
            if (findFor(self.udid, 3, "dangnhap.png",1 )!= 0):
                time.sleep(3)
                if (findFor(self.udid, 15, "batdau.png",1 )!= 0):
                    time.sleep(5)
                    findFor(self.udid,5,"roikhoi.png",threshold=0.8)
                    a=self.checkMap()
                    ck=False
                    if(a==1):
                        ck=True
                        pass
                    elif(a==0):
                        ck=self.lenbai()
                    else:           
                        if(self.phu()==True):
                            ck=self.lenbai()
                    if(ck==True):
                        self.vaoTD()
                        self.batauto()
                        self.train()
                                        
    
                            
a=toolLQ('emulator-5560',(695,444)).train()