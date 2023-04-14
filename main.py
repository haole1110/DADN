import sys
from Adafruit_IO import MQTTClient
import time
import random
from simple_ai import *
from uart import *
# from linkMongoDB import *

AIO_FEED_IDs = ["device-buzzer", "device-light", "device-pump"]
AIO_USERNAME = "haole111002"
AIO_KEY = "aio_Cith08i6vd0UsqoE47GFw8S9jVRV"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " feed id: " + feed_id)
    if feed_id == "device-buzzer":
        if payload == "0":
            writeData(1)
        else:
            writeData(2)
    if feed_id == "device-light":
        if payload == "0":
            writeData(3)
        else:
            writeData(4)
    if feed_id == "device-pump":
        if payload == "0":
            writeData(5)
        else:
            writeData(6)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
type_sensor = 0
counter_ai = 5
ai_result = ""
pre_ai_result = ""
while True:
    counter = counter - 1
    counter_ai = counter_ai - 1
    # if counter <= 0:
    #     counter = 10
    #     if type_sensor == 0:
    #         print("Temp...")
    #         temp = random.randint(10, 20)
    #         # Day du lieu len adafruit
    #         client.publish("cambien1", temp)
    #         type_sensor = 1
    #     elif type_sensor == 1:
    #         print("Humi...")
    #         humi = random.randint(50,70)
    #         client.publish("cambien3", humi)
    #         type_sensor = 2
    #     else:
    #         print("Light...")
    #         light = random.randint(0,100)
    #         client.publish("cambien2", light)
    #         type_sensor = 0
    # if counter_ai <= 0:
    #     counter_ai = 5
    #     ai_result = image_detector()
    #     print("AI output: ", ai_result)
    #     if pre_ai_result != ai_result:
    #         client.publish("ai", ai_result)
    #         pre_ai_result = ai_result
    readSerial(client)


    time.sleep(1)
    pass