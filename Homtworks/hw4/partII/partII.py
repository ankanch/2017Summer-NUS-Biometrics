import cv2
import os

def detect_face(img_name):
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	# 'haarcascade_frontalface_default.xml' is provided by opencv, you can find it ine the opencv folder 
	img = cv2.imread(img_name)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray)
	if not len(faces):
		print('no face detected for', img_name)
	else:
		print(len(faces), 'faces detected for', img_name)
	
		for (x, y, w, h) in faces:
			cv2.rectangle(img, (x,y),(x+w, y+h), (255,0,0),2)

		cv2.imwrite(img_name[:-4]+'_result'+img_name[-4:], img)

if __name__=='__main__':
	#write your code here
	faces = ["./"+x for x in os.listdir("./") if x[-3:] in ("png","jpg")]
	#faces = ["./test1.png","./test2.png","./test3.png","./test4.jpg"]
	for face in faces:
		detect_face(face)
	