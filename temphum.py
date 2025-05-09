import grovepi
import paho.mqtt.publish as publish
import math
import json
import time
from grove_rgb_lcd import*
import datetime

# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND
tempsensor = 4  # The Sensor goes on digital port 4.
pressuresensor=0 # The Sensor goes on analogic port 0.
rotary=1 # The Sensor goes on analogic port 1.

# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.
setRGB(0,128,64)
while True:
    
    
    try:
        # This example uses the blue colored sensor.
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = grovepi.dht(tempsensor,blue)
        pressure=grovepi.analogRead(pressuresensor)
        angle=grovepi.analogRead(rotary)
        clientid=0
        if (angle < 256):
            clientid=1
        if (angle >=256 and angle <512):
            clientid=2
        if (angle >=512 and angle <768):
            clientid=3
        if (angle >=768 and angle <1024):
            clientid=4
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            setText("ID: "+str(clientid)+" T: "+str(temp)+" H: "+str(humidity)+" P: "+str(pressure))
            mesure={}
            mesure['temperature']=str(temp)
            mesure['humidite']=str(humidity)
            mesure['pression']=str(pressure)
            mesure['clientid']=str(clientid)
            mesure['date']=datetime.datetime.now().strftime('%R')
            print(mesure)
            json_data=json.dumps(mesure)
            publish.single("escapp/mesures", json_data, hostname="broker.mqttdashboard.com")
        time.sleep(5)
            

    except IOError:
        print ("Error")
