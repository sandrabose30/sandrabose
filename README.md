# sandrabose
https://drive.google.com/uc?id=1TcPVwcGcFFi98_oNZJBJNUnRii4qCRwx&export=download

# Steps to Follow

## Step 1

Copy the downloaded MIRACL-VC1_all_in_one.zip to project folder

Extract MIRACL-VC1_all_in_one.zip

Rename extracted folder to Dataset

delete catlib.txt file

## Step 2

Install required dependencies

'''
pip install opencv-python numpy imutils
'''

If on Windows install Visual Studio Community with Desktop Development with C++ enabled

'''
pip install cmake wheel dlib
'''

## step 3

Download Extra Dependencies to Project Folder

### haarcascade_frontalface_default.xml
https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

### shape_predictor_68_face_landmarks.dat.bz2

https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2

Extract this downloaded file .bz2 to .dat

## Step 3 

Replace path in code with your downloaded path in every py before running

### Order to Execute:

DatasetFolderArrange.py

FaceExtract.py

LipExtract.py

arenge.py

CreateCluster.py

TrainValTestSplit.py

TrainValTestSplitCluster.py