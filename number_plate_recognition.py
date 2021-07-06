import pandas as pd 
import numpy as np
import pytesseract
import matplotlib.pyplot as plt 
import cv2
import requests
import xmltodict
import json
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\Tesseract.exe'

web_cam_ip = 'http://192.168.29.200:8080/video'
model = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

def number_plate(photo):
    plate = model.detectMultiScale(photo)
    if len(plate) == 0:
        crop = 0
    else:
        x1 = plate[0][0]
        y1 = plate[0][0]
        x2 = x1 + plate[0][2]
        y2 = y1 + plate[0][3]
        crop = photo[y1:y2, x1:x2]
    return crop    

cap_mob = cv2.VideoCapture(web_cam_ip)
while True:
    ret,photo = cap_mob.read()
    img = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    plate_img = number_plate(photo)
    if plate_img is not 0 :
         name = pytesseract.image_to_string(plate_img)
        if len(name)>10:
            cap_mob.release()
            break
final_plate = name[3:13]
name
final_plate
def collect_vehicle_info(number_plate):
    r = requests.get("http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={0}&username=createdname_using_api".format(str(number_plate)))
    data = xmltodict.parse(r.content)
    jdata = json.dumps(data)
    df = json.loads(jdata)
    df1 = json.loads(df['Vehicle']['vehicleJson'])
    return df1

information = get_vehicle_info()

