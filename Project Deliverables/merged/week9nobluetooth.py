#!/usr/bin/env python3

import io
import json
import queue
import time
from multiprocessing import Process, Manager
from typing import Optional, List
import json
import requests
import time
# import pandas
from picamera import PiCamera

# import picamera
import requests
import socket

#  from communication.android import AndroidLink, AndroidMessage
from communication.stm32 import STMLink
from consts import SYMBOL_MAP
from logger import prepare_logger
from settings import API_IP, API_PORT, OUTDOOR_BIG_TURN

#import urllib
#import urllib2


class PiAction:
    """
    Represents an action that the Pi is responsible for:
    - Changing the robot's mode (manual/path)
    - Requesting a path from the API
    - Snapping an image and requesting the image-rec result from the API
    """

    def __init__(self, cat, value):
        self._cat = cat
        self._value = value

    @property
    def cat(self):
        return self._cat

    @property
    def value(self):
        return self._value


class RaspberryPi:
    def __init__(self):
        # prepare logger
        self.logger = prepare_logger()

        # communication links
#         self.android_link = AndroidLink()
        self.stm_link = STMLink()

        # for sharing information between child processes
        manager = Manager()

        self.instructions = manager.dict()

        # events
        self.android_dropped = manager.Event()  # set when the android link drops
        self.unpause = manager.Event()  # commands will be retrieved from commands queue when this event is set

        # movement lock, commands will only be sent to STM32 if this is released
        self.movement_lock = manager.Lock()

        # queues
        self.android_queue = manager.Queue()
        self.rpi_action_queue = manager.Queue()
        self.command_queue = manager.Queue()
        self.path_queue = manager.Queue()

        # define processes
        self.proc_recv_bluetooth = None
#         self.proc_recv_android = None
#         self.proc_recv_stm32 = None
        self.proc_android_sender = None
#         self.proc_command_follower = None
        self.proc_rpi_action = None

    def start(self):
        try:
            print("entered start")
            
            
            # establish bluetooth connection with Android
#             hostMACAddress = 'B8:27:EB:FE:BC:B6' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
#             port = 1 # 3 is an arbitrary choice. However, it must match the port used by the client.
#             backlog = 1
#             size = 1024
#             s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
#             s.bind((hostMACAddress,port))
#             s.listen(backlog)
#             global client
#             client, address = s.accept()
#             print("Accepted connection from", client)

            # establish connection with STM32
            self.stm_link.connect()

            # define processes
            self.proc_recv_bluetooth = Process(target=self.recv_bluetooth)
#             self.proc_recv_stm32 = Process(target=self.recv_stm)

            # start processes
            self.proc_recv_bluetooth.start()
#             self.proc_recv_stm32.start()

            self.logger.info("Child Processes started")

        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.android_link.disconnect()
#         self.stm_link.disconnect()
        self.logger.info("Program exited!")

            
    def recv_bluetooth(self) -> None:
    # b'ADDO,2,14,0,N' add obstacle, obstacle id, x,  y, direction
    # b'DELO,null' delet obstacle, obstacle id
    # b'ROBOT,5,8,N' robot location (x, y, direction)
       # Possible Errors:
       # 1. bluetooth disconnected
       # 2. flask disconnected
       # 3. stm disconnected
       # 4. no valid predicted image
        print("start to take image")
        camera = PiCamera()
        time.sleep(2)
       # image = camera.capture('./img{:d}.jpg'.format(i))
       # image = './img{:d}.jpg'.format(i)
        image = camera.capture('./img.jpg')
        camera.close()
        image = './img.jpg'
        response = requests.post('http://192.168.1.16:5000/predictImage', files={'file': open(image, 'rb')})
        if response.status_code == 200:
            predictedList = []
            for i in json.loads(response.content):
                if i["name"] != '10':
                    if len(predictedList) == 0:
                        predictedList = i
                    else:
                        if i["confidence"] > predictedList["confidence"]:
                            predictedList = i
            print("first image is:", predictedList["name"])
            
       
        print("start")
        self.stm_link.send('g025')
        if predictedList["name"] == '38': #right arrow
            print("enter send stm 1000")
            self.stm_link.send('1000')
        if predictedList["name"] == '39': #left arrow
            self.stm_link.send('1001')
        
        message :str = self.stm_link.recv()
        if message == 'K':
        camera = PiCamera()
        time.sleep(2)
       # image = camera.capture('./img{:d}.jpg'.format(i))
       # image = './img{:d}.jpg'.format(i)
        image = camera.capture('./img.jpg')
        camera.close()
        image = './img.jpg'
        response = requests.post('http://192.168.1.16:5000/predictImage', files={'file': open(image, 'rb')})
        if response.status_code == 200:
            predictedList = []
            for i in json.loads(response.content):
                if i["name"] != '10':
                    if len(predictedList) == 0:
                        predictedList = i
                    else:
                        if i["confidence"] > predictedList["confidence"]:
                            predictedList = i
            print("second image is:", predictedList["name"])
            
        if predictedList["name"] == '38': #right arrow
            self.stm_link.send('2000')
        if predictedList["name"] == '39': #left arrow
            self.stm_link.send('2001')
            
                
                


    def recv_stm(self) -> None:
        """
        Receive acknowledgement messages from STM32, and release the movement lock
        """
        print("enter stm")
#         self.instructions = {'1': ['3', '7', 'N'], '2': ['6', '4', 'N'], '3': ['2', '8', 'N']}
        while True:
            #data = client.recv(1024)
            if len(self.instructions) == 5:
                for i in self.instructions:
                    for j in self.instructions[i]:
                        print(j)
                        self.stm_link.send(j)
                    message :str = self.stm_link.recv()
                    #imgCounter = 1
                    if message == 'K':
                        camera = PiCamera()
                        time.sleep(2)
                        #image = camera.capture('./img{:d}.jpg'.format(i))
                        #image = './img{:d}.jpg'.format(i)
                        image = camera.capture('./img.jpg')
                        image = './img.jpg'
                        camera.close()
                        response = requests.post('http://192.168.1.16:5000/predictImage', files={'file': open(image, 'rb')})
                        if response.status == 200:
                            predictedList = []
                            for i in json.loads(response.content):
                                if response.content[i]["name"] != '10':
                                    if len(predictedList) == 0:
                                        predictedList = response.content[i]
                                    else:
                                        if response.content[i]["confidence"] > predictedList["confidence"]:
                                            predictedList = response.content[i]
                            # send predicted image id to android
                            client.send("TARGET,{},{}".format(i,predictedList["name"]).encode())
                    #imgCounter += 1
                            
                response2 = requests.get('http://192.168.1.16:5000/stitchImage')
                if response2.status_code == 200:
                    client.send("done with image rec".encode())
                    #close everything
                
            
#         while True:
#             print("datafromstm", message)
#             if message == 'K':
#                 counter += 1
#                 if counter == 3:
#                     self.stm_link.send('b010')
#                 camera = PiCamera()
#                 time.sleep(2)
#                 image = camera.capture('./img.jpg')
#                 print("Done.")
#                 image='./img.jpg'
#                 test = requests.post('http://192.168.1.16:5000/predictImage', files={'file': open(image, 'rb')})
#                 camera.close()
#                 
#         self.stm_link.send('g000')
#         print("send g000")
#         message :str = self.stm_link.recv()
#         counter = 0
#         while True:
#             print("datafromstm", message)
#             if message == 'K':
#                 counter += 1
#                 if counter == 3:
#                     self.stm_link.send('b010')
#                 camera = PiCamera()
#                 time.sleep(2)
#                 image = camera.capture('./img.jpg')
#                 print("Done.")
#                 image='./img.jpg'
#                 test = requests.post('http://192.168.1.16:5000/predictImage', files={'file': open(image, 'rb')})
#                 camera.close()
#                 
#                 response = requests.post('http://192.168.1.16:5000/predictJSON', files={'file': open(image, 'rb')})
#                 if (response.status_code == 200):
#                     print(json.loads(response.content))
#                     if json.loads(response.content)[0]["name"] == '10':
#                         self.stm_link.send('l090')
#                         print("move left 90 deg")
#                         message :str = self.stm_link.recv()
#                     else:
#                         print("found valid image")
                        

        
    def predictJSON(image):
        response = requests.post('http://192.168.1.16:5000/predictJSON',
                                 files={'file': open(image, 'rb')})
        if (response.status_code == 200):
            print(json.loads(response.content))
            array = []
            for i in json.loads(response.content):
                array.append(i['name'])
            print(array)


if __name__ == "__main__":
    rpi = RaspberryPi()
    print("start") 
    rpi.start()


