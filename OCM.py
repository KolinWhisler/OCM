"""OCM Animatronics Project. The goal of this project is to allow
for the creation of a functional motor control over the motors
that will be operating the animatronic. This will connect to the
UI Pi to allow for communication between the UI and the moto control
"""    



#These imports will allow for the usage of GPIO commands,
#the timer ability and system calls that can exit the program
import numpy
import RPi.GPIO as GPIO
import time
import sys
import os
import socket
import numpy as mp


"""HOST, PORT = "localhost", 5900
data = " ".join(sys.argv[1:])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
sock.sendall(bytes(data + "\n", "utf-8"))

received =str(sock.recv(1024), "utf-8")

print("Sent: {}".format(data))
print("Received: {}".format(received))"""

#These stop any GPIO warnings from appearing aso the code can show only important notifications
GPIO.setwarnings(False)



#Set the output mode to BCM
GPIO.setmode(GPIO.BCM)



#Sets all of the Pin headers to the motor they will power
Motor1=10
Motor2=12
Motor3=13
Motor4=9
Motor5=10
Motor6=11



#sets each motor to operate when given the command to do so
GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor3,GPIO.OUT)
GPIO.setup(Motor4,GPIO.OUT)
GPIO.setup(Motor5,GPIO.OUT)
GPIO.setup(Motor6,GPIO.OUT)



#Temporary case, opens a txt file that the program will read to the user
file="/home/pi/Desktop/Binary.txt"



#sets the base command to off
f = "000000"




#Creates error exception handling by setting the value of operations to working or not working
while 1==1:
    class NoError:
        1==1





#Try loop opens file to be read and then closes when given command to
    try:
        while 1==1:
            
            g=open(file, "r")
            h = g.read()
            if f != h and h != "":
                f=h



#GPIO outputs ensure that the motor                
                GPIO.output(Motor1, int(f[0]))
                GPIO.output(Motor2, int(f[1]))
                GPIO.output(Motor3, int(f[2]))
                GPIO.output(Motor4, int(f[3]))
                GPIO.output(Motor5, int(f[4]))
                GPIO.output(Motor6, int(f[5]))



#Prints txt file output                
            if NoError:
                print(f)
                g.close()
                time.sleep(2)
                
               
               
#Ports the UI code into motor control to allow for UI to control the motor control group
               
           


 
#Exception erros to help find wy the code isn't working
#Each one is set to stop the program immediately after an error occurs.
    #except FileNotFoundError:
     #   print("Invalid file")
      #  time.sleep(1)
       # sys.exit()
    #except ValueError:
     #   print("Invalid txt input")
      #  time.sleep(1)
       # sys.exit()
    except KeyboardInterrupt:
        print("Program End")
        GPIO.output(Motor1, 0)
        GPIO.output(Motor2, 0)
        GPIO.output(Motor3, 0)
        GPIO.output(Motor4, 0)
        GPIO.output(Motor5, 0)
        GPIO.output(Motor6, 0)

        sys.exit()
    #except NameError:
     #   print("Please specify command")
      #  time.sleep(1)
       # sys.exit()
    #except IndexError:
     #   print("Please insert 6-digit command")
      #  time.sleep(1)
       # sys.exit()
   # except SyntaxError:
       # print("Correct Syntax")
        #time.sleep(1)
        #sys.exit()
       
       
       
#Keypress halts the process when given command to
   # except KeyboardInterrupt:
    #    print("Press Ctrl-C to terminate program")
     #   sys.exit()
        
        
#killswitch
    #if keyboard.is_pressed('k'):
        #sys.exit
        
        #if on_press('c') == True:
            #sys.exit()
        
        #sys.exit(OCM.py)
        #print('prgram stop')