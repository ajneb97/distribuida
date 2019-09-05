import sys, Ice
import Demo
import numpy as np
 
import io
import cv2

class CaraI(Demo.Cara):
        def getCaras(self,image_data,current=None):
		# Load the cascade
		# CARAS
		face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
		# face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

		# Read the input image
		nparr = np.fromstring(image_data, np.uint8)
		img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # cv2.IMREAD_COLOR in OpenCV 3.1

		# Convert into grayscale
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		# Detect faces
		faces = face_cascade.detectMultiScale(gray, 1.10, 4)

		# Draw rectangle around the faces
		n = 0
		for (x, y, w, h) in faces:
		    n = n+1
		
		return 'Numero de caras en foto: '+str(n)
 
with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("Caras", "default -p 10000")
    object = CaraI()
    adapter.add(object, communicator.stringToIdentity("Cara"))
    adapter.activate()
    communicator.waitForShutdown()
