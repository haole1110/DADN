from Adafruit_IO import MQTTClient
import requests
from pymongo import MongoClient
import time

# Kết nối tới Adafruit IO API và truy xuất dữ liệu từ feed
AIO_USERNAME = 'haole111002'
AIO_KEY = 'aio_Cith08i6vd0UsqoE47GFw8S9jVRV'
FEED_NAME = ['history-humi', 'history-light', 'history-soil', 'history-temp']

#Khoi tao gia tri rong
last_data_id = [None] * 4
pre = [None] * 4

#Khoi tao gia tri ban dau
response = requests.get(f'https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME[0]}/data', headers={'X-AIO-Key': AIO_KEY})
data = response.json()
pre[0] = data[0]['value']

response = requests.get(f'https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME[1]}/data', headers={'X-AIO-Key': AIO_KEY})
data = response.json()
pre[1] = data[0]['value']

response = requests.get(f'https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME[2]}/data', headers={'X-AIO-Key': AIO_KEY})
data = response.json()
pre[2] = data[0]['value']

response = requests.get(f'https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME[3]}/data', headers={'X-AIO-Key': AIO_KEY})
data = response.json()
pre[3] = data[0]['value']


#Ket noi voi MongoDB
client = MongoClient('localhost', 27017)
db = client['Project_DADN']
collection = [db['history_humi'], db['history_light'], db['history_soil'], db['history_temp']]

# for item in data:
#     record = {'value': item['value'], 'time': item['created_at']}
#     result = collection.insert_one(record)
#     print("Pushing...")

print("Connected...")
while True:
    print("Checking...")

    #Kiem tra voi humi
    response = requests.get(f'https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME[0]}/data', headers={'X-AIO-Key': AIO_KEY})
    data = response.json()
    # print(data)
    last_data_id[0] = data[0]['value']
    # print(pre, " ", last_data_id)
    if pre[0] != last_data_id[0]:
        record = {'value': data[0]['value'], 'time': data[0]['created_at']}
        result = collection[0].insert_one(record)
        pre[0] = last_data_id[0]
        print("Humi...Pushed...")

    # Kiem tra voi light
    response = requests.get(f'https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME[1]}/data', headers={'X-AIO-Key': AIO_KEY})
    data = response.json()
    # print(data)
    last_data_id[1] = data[0]['value']
    # print(pre, " ", last_data_id)
    if pre[1] != last_data_id[1]:
        record = {'value': data[0]['value'], 'time': data[0]['created_at']}
        result = collection[1].insert_one(record)
        pre[1] = last_data_id[1]
        print("Light...Pushed...")
    # Kiem tra voi soil
    response = requests.get(f'https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME[2]}/data', headers={'X-AIO-Key': AIO_KEY})
    data = response.json()
    # print(data)
    last_data_id[2] = data[0]['value']
    # print(pre, " ", last_data_id)
    if pre[2] != last_data_id[2]:
        record = {'value': data[0]['value'], 'time': data[0]['created_at']}
        result = collection[2].insert_one(record)
        pre[2] = last_data_id[2]
        print("Soil...Pushed...")
    # Kiem tra voi temp
    response = requests.get(f'https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME[3]}/data', headers={'X-AIO-Key': AIO_KEY})
    data = response.json()
    # print(data)
    last_data_id[3] = data[0]['value']
    # print(pre, " ", last_data_id)
    if pre[3] != last_data_id[3]:
        record = {'value': data[0]['value'], 'time': data[0]['created_at']}
        result = collection[3].insert_one(record)
        pre[3] = last_data_id[3]
        print("Temp...Pushed...")

    time.sleep(1)