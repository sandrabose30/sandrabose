import cv2
import numpy as np
from imutils import face_utils
import imutils
import dlib
from keras.models import load_model
import json
import flask
# p=r'D:\project\codes\reduced_vocab_index.json'
# # with open(p) as json_file:
# #     new_dict = json.load(json_file)
# json_file=open(p)
# new_dict = json.load(json_file)

model = load_model('CNNv5.h5')

cap = cv2.VideoCapture(0)
success = 1
frames = []

while success:
  success, image = cap.read()
  cv2.imshow('frame', image)
  frames.append(image)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()

faces = []
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

for frame in frames:
   img = frame
   img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   detected_faces = face_classifier.detectMultiScale(img, 1.3, 3)
   print(detected_faces)
   try:
       [[x, y, h, w]] = detected_faces
   except:
       print("eroor onduuu")
   img_crop = img[y:y + h, x:x + w]
   faces.append(img_crop)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
lips = []

for face in faces:
   img = face
   # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   rects = detector(img, 1)
   for (i, rect) in enumerate(rects):
       shape = predictor(img, rect)
       shape = face_utils.shape_to_np(shape)
       for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
          if name == 'mouth':
              for (x, y) in shape[i:j]:
                 (x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
                 roi = img[y:y + h, x:x + w]
                 roi = imutils.resize(roi, width=250, inter=cv2.INTER_CUBIC)
                 lips.append(roi)
       seq = np.zeros((224, 224))
       orig = len(lips)
       orig_image = []
       for lip in lips:
          img = lip
          img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_LINEAR)
          orig_image.append(img)
       x_limit = 32
       y_limit = 32
       iterator_x = 0
       iterator_y = 0
       for i in range(0, 49):
          seq[iterator_y:iterator_y + y_limit, iterator_x:iterator_x + x_limit] = orig_image[int((i * orig) / 49)]
       #movement along y - axis
          iterator_x = iterator_x + x_limit
          if iterator_x == 224:
              iterator_x = 0
              iterator_y = iterator_y + y_limit
          cv2.imwrite('cluster.jpg', seq)


          cluster = cv2.imread('cluster.jpg')
          cluster = cv2.cvtColor(cluster, cv2.COLOR_BGR2GRAY)
          cluster = cv2.resize(cluster, (224, 224))
          cluster = np.reshape(cluster, (1, 224, 224, 1))
          cluster = cluster / 255.0
          # prediction = new_dict[str(np.argmax(model.predict(cluster)))]
          print(str(np.argmax(model.predict(cluster))))
          # print(prediction)