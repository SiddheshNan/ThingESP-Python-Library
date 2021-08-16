import ThingESP
import cv2
from datetime import datetime

thing = ThingESP.Client('username', 'project_name', 'credentials')
cam = ThingESP.WebcamVideoStream(src=0).start()

img_name = "img.jpg"


def handleResponse(query):
    if query == 'hi':
        return "hello, how are you?"
    elif query == "send image":
        cam.saveImage(img_name)
        thing.sendImage(img_name, "your_phone_number", "here's your image!")
        return f"image sent on {datetime.now()}"


thing.setCallback(handleResponse).start()

while True:
    frame = cam.read()
    cv2.imshow('webcam', frame)
