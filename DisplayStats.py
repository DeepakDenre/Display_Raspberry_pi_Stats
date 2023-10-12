#! /usr/bin/python3.9
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import ST7735 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import socket
import psutil
import os
from time import sleep
from datetime import datetime

pwd = str(os.path.dirname(__file__))
print("File directory:"+pwd)
WIDTH = 130
HEIGHT = 132
SPEED_HZ = 15
bug=False

# Raspberry Pi configuration.
DC = 24
RST = 25
SPI_PORT = 0
SPI_DEVICE = 0

print("Starting DisplayStats.py")
try:
    # Create TFT LCD display class.
    disp = TFT.ST7735(
        DC,
        height=HEIGHT,
        width=WIDTH,
        rst=RST,
        spi=SPI.SpiDev(
            SPI_PORT,
            SPI_DEVICE,
            max_speed_hz=SPEED_HZ))
    try:
        xfont = ImageFont.FreeTypeFont(
            pwd+"/Comfortaa.ttf",
            size=12)
    except Exception:
        xfont = ImageFont.load_default()
    color = {
        "red": (255,0,0),
        "green": (0,255,0),
        "blue": (0,0,255),
        "orange": (255,165,0),
        "white": (255,255,255),
        "black": (0,0,0)
    }
    now = datetime.now()

    # Initialize display.
    disp.begin()

    # Can pass any tuple of red, green, blue values (from 0 to 255 each).
    disp.clear((255, 0, 0))

    # disp.clear()

    # Get a PIL Draw object to start drawing on the display buffer.
    draw = disp.draw()
except Exception as e:
    print(e)
while bug==False:
    try:
        try:
            while True:
                print("starting!")
                # gather data
                current_time = str(now.strftime("%H:%M:%S"))+": "
                print(current_time+"Gathering Data")

                print(current_time+"Getting Hostname")
                hostname = str(socket.gethostname())

                ip = psutil.net_if_addrs()
                print(current_time+"Getting IP wlan0")
                if(ip["wlan0"][0].netmask == None):
                    ip1 = "Not Connected"
                else:
                    ip1 = ip["wlan0"][0].address
                
                print(current_time+"Getting IP eth0")
                if(ip["eth0"][0].netmask == None):
                    ip2 = "Not Connected"
                else:
                    ip2 = ip["eth0"][0].address
                
                print(current_time+"Getting CPU")
                cpu = str(psutil.cpu_percent())+"%"+" = "+str(psutil.cpu_freq().current/1000)+"GHz"

                print(current_time+"Getting Temp")
                cpt_temp = str(psutil.sensors_temperatures()["cpu_thermal"][0].current)[0:5]

                print(current_time+"Getting RAM")
                ram = str(psutil.virtual_memory().percent)+"%"+" = "+str(psutil.virtual_memory()[3]/1000000000)[:4]+"GB"

                # display data  
                print(current_time+"Displaying Data")
                disp.clear()

                # display hostname
                print(current_time+"Displaying Hostname : "+hostname)
                draw.text((5,5),"Hostname:",font=xfont,fill=color["white"])
                draw.text((35,20),hostname,font=xfont,fill=color["red"])

                # display ip
                print(current_time+"Displaying IP : "+"wlan0:"+ip1+" & "+"eth0:"+ip2)
                draw.text((5,35),"IP(Wlan0:1 & Eth0:2):",font=xfont,fill=color["white"])
                draw.text((5,50),"[1] "+ip1,font=xfont,fill=color["green"])
                draw.text((5,65),"[2] "+ip2,font=xfont,fill=color["green"])

                # display cpu details
                print(current_time+"Displaying CPU : "+cpu)
                draw.text((5,80),"CPU:",font=xfont,fill=color["white"])
                draw.text((33,80),cpu,font=xfont,fill=color["green"])

                # display cpu temp
                print(current_time+"Displaying Temp : "+cpt_temp+" °C")
                draw.text((5,95),"Temp:",font=xfont,fill=color["white"])

                # display ctu temp color according to temp

                # display temp in red if temp > 50
                if(float(cpt_temp) > 50):
                    draw.text((46,95),cpt_temp+" °C",font=xfont,fill=color["red"])

                # display temp in orange if temp > 40
                elif(float(cpt_temp) > 40):
                    draw.text((46,95),cpt_temp+" °C",font=xfont,fill=color["orange"])

                # display temp in green if temp < 40
                else:
                    draw.text((46,95),cpt_temp+" °C",font=xfont,fill=color["green"])

                # display ram  
                print(current_time+"Displaying RAM : "+ram+"%") 
                draw.text((5,110),"RAM:",font=xfont,fill=color["white"])
                draw.text((35,110),ram,font=xfont,fill=color["green"])
                
                # Display image.
                print(current_time+"Rendering Image")
                sleep(1)
                disp.display()
                bug=False
                print(
                    current_time+"Done"+
                    "\n\n---------------------------------------\n")
        except KeyboardInterrupt:
            print("Bye")
            disp.clear()
            disp.display()
            break
    except Exception as e:
        print(e)
        bug=True
