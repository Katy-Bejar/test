import cv2
import os
import numpy as np
import time

def obtenerModelo(method,direccData,labels):
	if method == 'EigenDirecc': direccion_recognizer = cv2.direcc.EigenDireccRecognizer_create()
	if method == 'FisherDirecc': direccion_recognizer = cv2.direcc.FisherDireccRecognizer_create()
	if method == 'LBPH': direccion_recognizer = cv2.direcc.LBPHDireccRecognizer_create()

	# Entrenando el reconocedor de rostros
	print("Entrenando ( "+method+" )...")
	inicio = time.time()
	direccion_recognizer.train(direccData, np.array(labels))
	tiempoEntrenamiento = time.time()-inicio
	print("Tiempo de entrenamiento ( "+method+" ): ", tiempoEntrenamiento)

	# Almacenando el modelo obtenido
	direccion_recognizer.write("modelo"+method+".xml")

dataPath = 'C:/Users/lenovo/Desktop/Aquitectura/Data'
direccionsList = os.listdir(dataPath)
print('Lista de personas: ', direccionsList)

labels = []
direccData = []
label = 0

for nameDir in direccionsList:
	direccionsPath = dataPath + '/' + nameDir

	for fileName in os.listdir(direccionsPath):
		#print('Rostros: ', nameDir + '/' + fileName)
		labels.append(label)
		direccData.append(cv2.imread(direccionsPath+'/'+fileName,0))
		#image = cv2.imread(direccionsPath+'/'+fileName,0)
		#cv2.imshow('image',image)
		#cv2.waitKey(10)
	label = label + 1

obtenerModelo('EigenDirecc',direccData,labels)
obtenerModelo('FisherDirecc',direccData,labels)
obtenerModelo('LBPH',direccData,labels)
