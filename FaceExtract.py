import os
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

failed_files_string = ""
os.chdir(r'Dataset')
for a in sorted(os.listdir()):
   os.chdir(a)
   print(a)
   
   for b in sorted(os.listdir()):
      os.chdir(b)
      print("\t",b)
      for c in sorted(os.listdir()):
         os.chdir(c)
         print("\t\t",c)
         for d in sorted(os.listdir()):
            print("d========",d)
            os.chdir(d)
            print("\t\t\t",d)
            if os.path.exists('ExtractedFace') == False:
               os.mkdir('ExtractedFace')
            os.chdir('face')
            for p in sorted(os.listdir()):
               if 'color' in p:
                  try:
                     filename = os.path.basename(p)
                     print((os.getcwd()),filename, " prep")
                     img = cv2.imread(p)
                     cv2.imshow('image',img)
                     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                     faces = face_classifier.detectMultiScale(img,1.3,3)
                     [[x,y,h,w]] = faces
                     img_crop = img[y:y+h,x:x+w]
                     cv2.imwrite('../ExtractedFace/'+filename,img_crop)
                     print((os.getcwd()),filename, " done")
                  except:
                     print("eroorrrrrrrrrrrrrrrrrrrrr")
                     
            os.chdir('..')
            os.chdir('..')
            print((os.getcwd()))
         print("\t\t\t",d," done")
         # os.chdir('../../..')
         os.chdir('..')
      print("\t\t",c," done")
      os.chdir('..')
   print("\t",b, " done")
   os.chdir('..')
print(a, " done")
os.chdir('..')