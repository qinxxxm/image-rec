import json
import requests
import pandas
# from picamera import PiCamera
# send image to python flask for image recognition


def predictImage(image):
    # camera = PiCamera()
    # time.sleep(2)
    # camera.capture("picameraImages/img.jpg")
    # print("Done.")
    # image='picameraImages/img.png'
    response = requests.post('http://192.168.1.16:5000/predictImage',
                             files={'file': open(image, 'rb')})

    if (response.status_code == 200):
        print(response.content)
        # stitchImage()
        # json = response.json()
        # we can get the 'class' from here, and with that info know what to do
        # print(response.content)
        # print(json.loads(response.content))
    # else:
        # self.logger.error("Something went wrong when requesting path from image-rec API. Please try again.")
        # self.android_queue.put(AndroidMessage("error", "Something went wrong when requesting path from image-rec API. Please try again."))

    return


def predictJSON(image):
    response = requests.post('http://192.168.50.246:5000/predictJSON',
                             files={'file': open(image, 'rb')})
    if (response.status_code == 200):
        print(json.loads(response.content))

# call this to put all images in one folder (meet the tiled image requirement???)


def stitchImage():
    response = requests.get('http://192.168.50.246:5000/stitchImage')
    print(response.content)


predictImage('test-img/IMG_1100.jpg')  # for getting back predicted image file

# predictJSON('test-img/IMG_2203.jpg')  # for getting back predicted image class
