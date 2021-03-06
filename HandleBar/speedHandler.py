import RPi.GPIO as GPIO
import socket, sys, time
#GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.IN) #speed

#UDP setup
host = sys.argv[1]
textport = sys.argv[2]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

#data for calculations
radius = 0.29 #radius of bike wheel
pi = 3.14159 
count = 0
rotations = 15 #number of rotations
wait = 0.1 #wait used for debouncing
start = time.time() #timer

while 1:  
  if not GPIO.input(21):
    time.sleep(wait) # wait so only one reading occurs
    if count == rotations: #enter if max rotation
      t = time.time() - start - wait #time for 5 rotations
      speed = (2*pi*radius*rotations*3.6)/t #speed calc
      #send packet
      data = "Speed:%f" %speed
      s.sendto(data.encode('utf-8'), server_address)
      #reset count and time
      start = time.time()
      count = 0
    else:
      count = count + 1
s.shutdown(1)
      
