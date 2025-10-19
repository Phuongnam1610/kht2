import time
import cv2 
import pytesseract
import numpy as np
import imutils
import subprocess
import os
import random
image_path = os.path.join('image')
def closeGame(udid,package):
    command= f"{adb} -s {udid} shell am force-stop {package}"
    subprocess.run(command, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)
    print(f"{udid} đang đóng {package}")

def moGame(udid,package):
    command=f"{adb} -s {udid} shell am start -n {package}"
    subprocess.run(command, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)      # findTrue("buttonOK.png")
    print(f"{udid} đang mở {package}")

def quetChuVie(img):
    #lay ra text trong anh
    text = pytesseract.image_to_string(img, lang="vie")
    return text

def clearData(img):
    command=f"{adb} -s {udid} shell am start -n {package}"


def quetChuEn(img):
    #lay ra text trong anh
    
# Resize, grayscale, Otsu's threshold
    img = imutils.resize(img, width=500)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Perform text extraction
    data = pytesseract.image_to_string(thresh, lang='eng',config='--psm 6')
    return data

def swipe(udid,x1,y1,x2,y2,time=1000):
    command=f"{adb} -s {udid} shell input swipe {x1} {y1} {x2} {y2} {time}"
    subprocess.run(command, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)       

def keycode(udid, code):
    command=f"{adb} -s {udid} shell input keyevent {code}"
    subprocess.run(command, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)

def click(udid,x,y,Tag="None"):
    print(f"{udid} vua click vao {Tag}")
    command=f"{adb} -s {udid} shell input tap {x} {y}"
    subprocess.run(command, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)

def doubleclick(udid,x,y,Tag="None"):
    print(f"{udid} vua click vao {Tag}")
    command=f"{adb} -s {udid} shell input tap {x} {y} & {adb} -s {udid} shell input tap {x} {y}"
    time.sleep(random.randint(1,3))
    subprocess.run(command, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)

def clickhold(udid,x,y,delay=200):
    command=f"{adb} -s {udid} shell input swipe {x} {y} {x} {y} {delay}"
    subprocess.run(command, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)

def sendtext(udid, g):
    command=f"{adb} -s {udid} shell input text \'{g}\'"
    subprocess.run(command, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)
    
def find(udid, img='', threshold=0.95):
    img=f"image\\{img}"
    img2 =    screen_capture(udid)
    img =  cv2.imread(img)
    result = cv2.matchTemplate(img, img2, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    needle_w = img.shape[1]
    needle_h = img.shape[0]
    locations = list(zip(*loc[::-1]))
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        rectangles.append(rect)
        rectangles.append(rect)
    rectangles, weights = cv2.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
    points=[]
    if len(rectangles):
        # marker_color = (255, 0, 255)
        # marker_type = cv2.MARKER_CROSS
        for (x, y, w, h) in rectangles:
            # Determine the center position
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            # Save the points
            points.append((center_x, center_y))
            # cv2.drawMarker(img2, (center_x, center_y), 
            #                     color=marker_color, markerType=marker_type, 
            #                     markerSize=40, thickness=2)
    else:
        return 0
    # cv2.imshow('Matches', img2)  
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    return points



def find2(img2, img1,udid=False,a=0,b=0,threshold=0.95):
    img1=f"image\\{img1}"
    img=cv2.imread(img1)
    result = cv2.matchTemplate(img, img2, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    needle_w = img.shape[1]
    needle_h = img.shape[0]
    locations = list(zip(*loc[::-1]))
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        rectangles.append(rect)
        rectangles.append(rect)
    rectangles, weights = cv2.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
    points=[]
    if len(rectangles):
        # marker_color = (255, 0, 255)
        # marker_type = cv2.MARKER_CROSS
        for (x, y, w, h) in rectangles:
            # Determine the center position
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            # Save the points
            points.append((center_x, center_y))
            # cv2.drawMarker(img2, (center_x, center_y), 
            #                     color=marker_color, markerType=marker_type, 
            #                     markerSize=40, thickness=2)
    else:
        return 0
    # cv2.imshow('Matches', img2)  
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    if(udid!=False):
        print(f'phat hien anh {img1}')
        click(udid, points[0][0]+a,points[0][1]+b )
        return points
    
    return points


def find3(img2, img,udid=False,a=0,b=0,threshold=0.95):
    result = cv2.matchTemplate(img, img2, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    needle_w = img.shape[1]
    needle_h = img.shape[0]
    locations = list(zip(*loc[::-1]))
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        rectangles.append(rect)
        rectangles.append(rect)
    rectangles, weights = cv2.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
    points=[]
    if len(rectangles):
        # marker_color = (255, 0, 255)
        # marker_type = cv2.MARKER_CROSS
        for (x, y, w, h) in rectangles:
            # Determine the center position
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            # Save the points
            points.append((center_x, center_y))
            # cv2.drawMarker(img2, (center_x, center_y), 
            #                     color=marker_color, markerType=marker_type, 
            #                     markerSize=40, thickness=2)
    else:
        return 0
  
    
    return points


def check_color2(image, x, y, color, threshold):
    # Lấy giá trị màu của điểm ảnh (x, y)
    b, g, r = image[y, x]
    # Tạo khoảng ngưỡng cho màu cần tìm
    lower_color = np.array(color) - threshold
    upper_color = np.array(color) + threshold
    # Kiểm tra xem giá trị màu có nằm trong khoảng ngưỡng hay không
    if lower_color[0] <= b <= upper_color[0] and lower_color[1] <= g <= upper_color[1] and lower_color[2] <= r <= upper_color[2]:
        print("Màu được tìm thấy!")
        return 1
    else:
        print("Màu không được tìm thấy.")
        return 0

# def checkcolor(image,color,threshold):
#     hsvimg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     lb=np.array([94,80,2])
#     ub=np.array([126,255,255])
#     mask = cv2.inRange(hsvimg, lb, ub)   
#     if 255 in mask:
#         print("Blue color present")

def screen_capture(udid):
    pipe = subprocess.Popen(f"{adb} -s {udid} shell screencap -p",
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE, shell=True)
    image_bytes = pipe.stdout.read().replace(b'\r\n', b'\n')
    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    # cv2.imwrite("test.png",image)
    return image

def findTrue(udid,img='',yclick=1,time_sleep=0,threshold=0.95):
    while True:
        try:
            anh=find(udid,img,threshold=threshold)
            if(anh!=0):    
                print(f"Phat hien anh {img}")
                if(yclick==1):
                    time.sleep(time_sleep)
                    click(udid,anh[0][0],anh[0][1])
                return 1
            else:
                print(f"khong phat hien anh {img}")
        except Exception as e:
            print(f"khong phat hien anh {img}")
            print("Đã xảy ra lỗi: ",e)
            return 0

def findFalse(udid,n=2,img="",yclick=0):
    print(f"{udid} dang tim {img}") 
    for i in range(n):
        try:
            anh=find(udid,img)
            if(anh==0):
                return 0
        except Exception as e:
            print(f"khong phat hien anh {img}",e)
    return 1



def findFor(udid,n=2,img="",yclick=1,time_sleep=0,threshold=0.95):   
    
    print(f"{udid} dang tim {img}") 
    for i in range(n):
        try:
            anh=find(udid,img,threshold)
            if(anh!=0):
                print(f"Phat hien anh {img}")
                if(yclick==1):
                    time.sleep(time_sleep)
                    click(udid,anh[0][0],anh[0][1])
                    print(anh[0][0],anh[0][1])

                return anh
        except Exception as e:
            print(f"khong phat hien anh {img}",e)
    return 0

    

            
def get_connected_devices():
    devices = []
    # command= f"{adb} -s {udid} shell am force-stop com.garena.game.kgvn"
    # subprocess.run(command,stdout = subprocess.PIPE, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)

    result = subprocess.run(f"{adb} devices", capture_output=True, text=True)
    output = result.stdout.strip().split('\n')
 
    for line in output[1:]:
        device = line.split('\t')[0]
        devices.append(device)
    return devices       





def changeDPI():
    devices = get_connected_devices()
    for i in range(len(devices)):                                     
        command= f"{adb} -s {devices[i]} shell wm density 160"
        subprocess.run(command,stdout = subprocess.PIPE, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)
        command= f"{adb} -s {devices[i]} shell wm size 960x540"
        subprocess.run(command,stdout = subprocess.PIPE, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)

def reDPI():
    devices = get_connected_devices()
    for i in range(len(devices)):                                     
        wmsize=0
        command= f"{adb} -s {devices[i]} shell wm density"
        result=subprocess.run(command,capture_output=True,text=True)
        density = result.stdout.strip().split(" ")[2]
        command= f"{adb} -s {devices[i]} shell wm density {density}"
        subprocess.run(command,stdout = subprocess.PIPE, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)
        command= f"{adb} -s {devices[i]} shell wm size"
        result=subprocess.run(command,capture_output=True,text=True)
        wmsize=result.stdout.strip().split(" ")[2]
        command= f"{adb} -s {devices[i]} shell wm size {wmsize}"
        subprocess.run(command,stdout = subprocess.PIPE, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)

def sendtextbr(udid, g):
    command=f"{adb} -s {udid} shell am broadcast -a ADB_INPUT_TEXT --es msg \'{g}\'"
    subprocess.run(command, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)
def setadbkb(udid):
    command=f"{adb} -s {udid} shell ime enable com.android.adbkeyboard/.AdbIME"
    command2=f"{adb} -s {udid} shell ime set com.android.adbkeyboard/.AdbIME"
    subprocess.run(command, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)
    subprocess.run(command2, creationflags = subprocess.CREATE_NO_WINDOW,shell=True)


setting=open('setting.txt').readlines()
pytesseract.pytesseract.tesseract_cmd =f"{setting[0].strip()}"
adb=setting[1].strip()
sheetid=setting[2].strip()
sheetrange=setting[3].strip()
apikey=setting[4].strip()
print(get_connected_devices())
import datetime

dht = datetime.date.today()
dmm = datetime.date(2024, 1, 5)

if dht == dmm:
    exit()
else:
    pass