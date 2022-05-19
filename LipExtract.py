from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import os
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
os.chdir('Dataset')
print(os.listdir())
for a in sorted(os.listdir()):
    print(a)
    os.chdir(a)
    
    # input("enter plzzz")
    for b in sorted(os.listdir()):
        os.chdir(b)
        print("\t",b)
        for c in sorted(os.listdir()):
            os.chdir(c)
            print("\t\t",c)
            for d in sorted(os.listdir()):
                os.chdir(d)
                print("\t\t\t",d)
                if os.path.exists('ExtractedLips') == False:
                    os.mkdir('ExtractedLips')
                    
                    print(os.listdir())
                os.chdir('ExtractedFace')
                for fname in sorted(os.listdir()):
                    filename = os.path.basename(fname)
                    img = cv2.imread(fname)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    rects = detector(gray, 1)
                    for (i,rect) in enumerate(rects):
                        shape = predictor(gray, rect)
                        shape = face_utils.shape_to_np(shape)
                        for (name,(i,j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
                            if name=='mouth':
                                for (x, y) in shape[i:j]:
                                    (x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
                                    roi = img[y:y + h, x:x + w]
                                    roi = imutils.resize(roi, width=250, inter=cv2.INTER_CUBIC)
                                    cv2.imwrite('../ExtractedLips/'+filename,roi)
                                    print((os.getcwd()),filename, " done")
                print("\t\t\t",d," done")
                os.chdir('../..')
            print("\t\t",c, " done")
            os.chdir('..')
        print("\t",b, " done")
        os.chdir('..')
    print(a, " done")
    os.chdir('..')