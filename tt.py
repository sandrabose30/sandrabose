import cv2
import numpy as np
from imutils import face_utils
import imutils
import dlib
from keras.models import load_model
import json
from flask import Flask, render_template, request
import time

MAX_LEN = 21
with open('vocab_index.json') as json_file:
      new_dict = json.load(json_file)
model = load_model('LSTMV3.h5')
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def getCamera():
  cap = cv2.VideoCapture(0)
  success = 1
  frames = []
  while success:
    time.sleep(0.05)
    success, image = cap.read()
    cv2.imshow('frame', image)
    frames.append(image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  cap.release()
  cv2.destroyAllWindows()
  return frames

app = Flask('__name__')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/after', methods=['GET', 'POST'])
def after():
  frames = getCamera()
  faces = []

  for frame in frames:
    img = frame
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detected_faces = face_classifier.detectMultiScale(img,1.3,3)
    [[x,y,h,w]] = detected_faces
    img_crop = img[y:y+h,x:x+w]
    faces.append(img_crop)

  detector = dlib.get_frontal_face_detector()
  predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
  lips = []
  for face in faces:
    img = face
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(img, 1)
    for (i,rect) in enumerate(rects):
       shape = predictor(img, rect)
       shape = face_utils.shape_to_np(shape)
       for (name,(i,j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
         if name=='mouth':
            for (x, y) in shape[i:j]:
                (x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
                roi = img[y:y + h, x:x + w]
                roi = imutils.resize(roi, width=250, inter=cv2.INTER_CUBIC)
                roi = cv2.resize(roi, (32,32))
                roi = np.reshape(roi, (32,32,1))
                roi = roi/255.0
                lips.append(roi)
  seq = lips[-MAX_LEN:]
  seq = np.array(seq)
  seq = np.reshape(seq,(1, 21, 32, 32, 1))

  prediction = new_dict[str(np.argmax(model.predict(seq)))]
  return render_template('predict.html', caption='Choose')

if __name__ == '__main__':
  app.run(debug=True)