import cv2
import mediapipe as mp
import sys
import urllib.request
from os import remove

from mediapipe.python.solutions.face_detection import FaceDetection

link = sys.argv[1] #Se toma el link como argumento
filename = link.split('/')[-1] #Se lo almacena tomando el nombre del archivo
urllib.request.urlretrieve(link, filename) #Se descarga la imagen
img = cv2.imread(filename) #Se carga la imagen

mpFaceDetection = mp.solutions.face_detection
faceDetection = mpFaceDetection.FaceDetection()

#Se define un objeto para devolverlo
class DetectionBox:
    def __init__(self, xmin, ymin, width, height,score):
        self.xmin = xmin
        self.ymin = ymin
        self.width = width
        self.height = height
        self.score = score

results = faceDetection.process(img)
detectionesfinales = [] #Aqui se guardaran las detecciones de una imagen

if results.detections:
    for id,detection in enumerate(results.detections):
            boundingBox = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            box = DetectionBox(int(boundingBox.xmin * iw),int(boundingBox.ymin * ih),int(boundingBox.width * iw),int(boundingBox.height * ih),detection.score[0])
            detectionesfinales.append(box)

cv2.waitKey(1)
print ([det.__dict__ for det in detectionesfinales]) #Se muestran las detecciones como json
remove(filename) #Se remueve la imagen
sys.stdout.flush() #Se envia la informacion al archivo js
