from glob import glob
from flask import Flask, request
import torch
from PIL import Image
from imutils import paths
from flask import send_file
from flask_api import status
# for getting latest exp folder
from pathlib import Path
import os
import glob
app = Flask(__name__)

# load img-rec model
model = torch.hub.load('./', 'custom', path='best.pt', source='local')

print("model loaded")


@app.route('/')
def index():
    return "Hello World"


# Takes in the image from the 'test' folder, and outputs the predicted label - sample at the end
# Images with predicted bounding boxes are saved in the runs folder
@app.route('/predictImage', methods=['POST'])
def predictImage():

    file = request.files['file']
    img = Image.open(file.stream)
    results = model(img)
    results.save('runs')
    print(results)
    latestFolder = max(Path('./runs/detect').glob('*/'), key=os.path.getmtime)
    # results.pandas().xyxy[0].to_json(orient="records") #this gives us the image object, class is useful to identify classes we detected
    if (results):
        return send_file(f"{latestFolder}/image0.jpg", mimetype='image/jpg'), status.HTTP_200_OK
    else:
        return "no predicted image generated, please try again", status.HTTP_404_NOT_FOUND


# For the returning of json, to get the class of the picture taken (idk any better way to do this... better to send both file and json in predictImage)
@app.route('/predictJSON', methods=['POST'])
def predictJSON():

    file = request.files['file']
    img = Image.open(file.stream)
    results = model(img)
    # this gives us the image in json, class attribute is useful to identify classes we detected
    if (results):
        print(results.pandas().xyxy[0].to_json(orient="records"))
        return results.pandas().xyxy[0].to_json(orient="records"), status.HTTP_200_OK
    else:
        return "no predicted class generated, please try again", status.HTTP_404_NOT_FOUND


@app.route('/stitchImage', methods=['GET'])
def stitchImage():
    imgFolder = 'runs'
    newPath = 'runs/stitched.jpg'
    imgPath = list(paths.list_images(imgFolder))
    images = [Image.open(x) for x in imgPath]
    width, height = zip(*(i.size for i in images))
    total_width = sum(width)
    max_height = max(height)
    stitchedImg = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for im in images:
        stitchedImg.paste(im, (x_offset, 0))
        x_offset += im.size[0]
    stitchedImg.save(newPath)
    return 'images stitched', status.HTTP_200_OK


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


print("app closeeeeee")
