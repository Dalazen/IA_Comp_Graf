import numpy as np
import cv2
<<<<<<< HEAD

=======
>>>>>>> e9f6803fd9c79224d5edf2b9c39b09fc642b8c50
car_cascade = cv2.CascadeClassifier("treinamento/cascade.xml")
img = cv2.imread("analise02.jpg")
height, width, c = img.shape
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
objetos = car_cascade.detectMultiScale(gray, 1.2, 5)
print(objetos)
for (x,y,w,h) in objetos:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow('Analise', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
<<<<<<< HEAD
 
# opencv_annotation --annotations=positivas.txt --images=positivas/
# opencv_createsamples -info positivas.txt -bg negativas.txt -vec vetor.vec -w 24 -h 24 -num 1000 -vec vetor.vec
# opencv_traincascade -data treinamento -vec vetor.vec -bg negativas.txt -numPos 77 -numNeg 435 -w 24 -h 24 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -numStages 30 -acceptanceRatioBreakValue 1.0e-5
=======

# opencv_annotation --annotations=saida.txt --images=positives/
# opencv_createsamples -info saida.txt -bg bg.txt -vec positives.txt -w 24 -h 24
# opencv_traincascade -data treinamento -vec positives.txt -bg bg.txt -numPos 23 -numNeg 435 -w 24 -h 24 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -numStages 30 -acceptanceRatioBreakValue 1.0e-5
>>>>>>> e9f6803fd9c79224d5edf2b9c39b09fc642b8c50

# opencv_createsamples -img train.jpeg -bg bg.txt -info info/info.txt -pngoutput info -maxxangle 0.5 -maxyangle -0.5 -maxzangle 0.5 -num 1950
# opencv_traincascade -data treinamento -vec info/info.txt -bg bg.txt -numPos 420 -numNeg 435 -w 24 -h 24 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -numStages 30 -acceptanceRatioBreakValue 1.0e-5
# Ver a saida
# opencv_createsamples -w 24 -h 24 -vec relogios.vev