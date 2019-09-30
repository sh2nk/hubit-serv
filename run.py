import cv2
import sys
from em_model import EMR
import numpy as np
import imutils

from flask import Flask, request, Response, jsonify
app = Flask(__name__)


EMOTIONS = ['angry', 'disgusted', 'fearful', 'happy', 'sad', 'surprised', 'neutral']
cascade_classifier = cv2.CascadeClassifier('haarcascade_files/haarcascade_frontalface_default.xml')

network = EMR()

def brighten(data,b):
     datab = data * b
     return datab    

def format_image(image):
  if image is None:
    cv2.destroyAllWindows()
    exit()
  if len(image.shape) > 2 and image.shape[2] == 3:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  else:
    image = cv2.imdecode(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
  faces = cascade_classifier.detectMultiScale(
      image,
      scaleFactor = 1.3 ,
      minNeighbors = 5
  )
  if not len(faces) > 0:
    return None
  max_area_face = faces[0]
  for face in faces:
    if face[2] * face[3] > max_area_face[2] * max_area_face[3]:
      max_area_face = face
  face = max_area_face
  image = image[face[1]:(face[1] + face[2]), face[0]:(face[0] + face[3])]
  try:
    image = cv2.resize(image, (48,48), interpolation = cv2.INTER_CUBIC) / 255
  except Exception:
    print("[+] Problem during resize")
    return None
  return image

@app.route('/api/jpeg', methods=['POST'])
def login():
    if request.method == 'POST':
      r = request
      f = open('frame.jpeg', 'wb')
      f.write(r.data)
      f.close()
      nparr = np.fromstring(r.data, np.uint8)
      frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
      result = network.predict(format_image(frame))
      print(result)
      return Response(status=200)
        

if __name__ == '__main__':
  network.build_network()
  app.run()
