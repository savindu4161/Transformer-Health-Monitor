import codecs
import serial				#import serial library
import numpy                            #import numpy
import datetime as dt
import matplotlib.pyplot as plt	#import matplotlib library
import matplotlib.animation as animation
from drawnow import*		#import everything from drawnow library
from tkinter import*			#Import everything from Tkinter library
from tkinter import messagebox			#Import tkMessageBox module
from PIL import ImageTk, Image	 #Import the PIL.ImageTk module
import numpy as np               #for scatter plot
import matplotlib.pyplot as plt  #for background image
from scipy.misc import imread    #for background image
import matplotlib.cbook as cbook  #for background image

#from drawnow import drawnow
import threading
import time
import math
from PIL import ImageTk, Image	#Import the PIL.ImageTk module
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

import RPi.GPIO as GPIO
from time import sleep
#Disable warnings (optional)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer=2
GPIO.setup(buzzer,GPIO.OUT)
GPIO.output(buzzer,GPIO.HIGH)


#from tkinter import *
#from tkinter.ttk import *


count =0
T1 =0
N1 =0
T2 =0
N2 =0
power1=[]
Temperature1=[]
logic1 = True;
logic2 = True;
Z=0
g=0

#fig4 = plt.figure()
#ax4 = fig4.add_subplot(1, 1, 1)   
xs = []
ys = []


#stra =''
#start_code =''

# this port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = '/dev/ttyUSB0'
# be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 9600
#plt.ion()#interactive mode on

displayWindow = Tk()
displayWindow.title('Designed & Developed By O-171')
displayWindow.geometry('800x600')
displayWindow.configure(background='black')

path1 = '/home/pi/Project1/128x160increst.png'
LogoImage = ImageTk.PhotoImage(Image.open(path1))
displayImage1 = Label(displayWindow, image = LogoImage)
displayImage1.place(x=670 ,y= 0,height = 160 , width = 128)

path2 = '/home/pi/Project1/130x160xcrest.png'
LogoflagImage = ImageTk.PhotoImage(Image.open(path2))
displayImage2 = Label(displayWindow, image = LogoflagImage)
displayImage2.place(x=0 ,y= 0,height = 160 , width = 130)

path3 = '/home/pi/Project1/TF.jpg'
TFImage = ImageTk.PhotoImage(Image.open(path3))
displayImage3 = Label(displayWindow, image = TFImage)
displayImage3.place(x=155 ,y= 60,height = 500 , width = 500)

def tone() :
    
    GPIO.output(buzzer,GPIO.LOW)
    sleep(.5) # Delay in seconds
    GPIO.output(buzzer,GPIO.HIGH)
    sleep(.5)


def graphhr1():
    plt.ylim(0,100)
    plt.plot(power1,'r-',label='Power')
   
    plt.title('POWER OVER TIME')
    plt.xlabel('Time')
    plt.ylabel('Power(W)')   
    white_line = mlines.Line2D([], [], color='red', label='Power')
    plt.legend(loc = 'upper right',handles=[white_line])    
    #/home/pi/Desktop/system_monitor.png
    datafile = cbook.get_sample_data('/home/pi/Project1/system_monitor.png')
    img1 = imread(datafile)
    plt.imshow(img1, zorder=0, extent=[0,120, 0,90])
    plt.show()

def graphhr2():
    plt.ylim(0,100)
    plt.plot(Temperature1,'c-',label='Temperature')
   
    plt.title('TEMPERATURE OVER TIME')
    plt.xlabel('Time')
    plt.ylabel('Temprature(°C)')    
    white_line = mlines.Line2D([], [], color='cyan', label='TEMP.')
    plt.legend(loc = 'upper right',handles=[white_line])    
    #/home/pi/Desktop/temp.jpg
    datafile = cbook.get_sample_data('/home/pi/Project1/temp.jpg')
    img2 = imread(datafile) 
    plt.imshow(img2, zorder=0, extent=[0,130, 0,100])
    plt.show()


        

#def history():

  # ani = animation.FuncAnimation(fig4, animate, fargs=(xs, ys), interval=1000)
   # plt.show()
#def animate(i, xs, ys):
    #global T1
    
    # Read temperature (Celsius) from TMP102
    #temp_c = round(T1, 2)
    # Add x and y to lists
    #xs.append(dt.datetime.now().strftime('%D:%H:%M:%S'))
    #ys.append(temp_c)

    # Limit x and y lists to 20 items
    #xs = xs[-20:]
    #ys = ys[-20:]

    # Draw x and y lists
    #ax4.clear()
    #ax4.plot(xs, ys)

    # Format plot
    #plt.xticks(rotation=45, ha='right')
    #plt.subplots_adjust(bottom=0.30)
    #plt.title('History')
    #plt.ylabel('Temperature & Power')

# Set up plot to call animate() function periodically


def SerialPortConnection():
    global ser
    try:
        print ("try to connect port 0 ")
        SERIAL_PORT = '/dev/ttyUSB0'
        ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
        print ("connected port 0 ")
    except:        
        print ("try to connect port 1 ")
        SERIAL_PORT = '/dev/ttyUSB1'
        ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
        print ("connected port 1 ")

def ThreadOne():
    global device
    dataArray1=[]
    dataArray2=[]
    global T1
    global T2
    global N1
    global T2
    global N2
    global Z
    global g
        
    while ser.inWaiting():
        reading_beforehex = ser.readline()
        sixtyfouraddress=reading_beforehex[0:3]
        asciidata=reading_beforehex[4:20]
        
        #print("fsfsf")
        
        #Serial.print("30.5")
        #Serial.print(",")
        #Serial.print("230")
        #Serial.print(",")
        #Serial.print("20")
        #Serial.print(",")
        #Serial.print("22.4")
        #Serial.print(",")
        #Serial.print("22")
        #Delay(5000)

        
        reading=reading_beforehex.hex()
        #reading=reading_beforehex.hex().upper()         
        start_code = reading[4:6]
        length = reading[2:6]
        Frame_type=reading[6:8]
        sixtyfouraddress=reading[10:26]
        sixteenaddress=reading[24:28]
        Receive_option=reading[28:30]
        data_set=reading[30:41]
        asciidata=reading_beforehex[16:70]
        
        #sixtyfouraddress1=sixtyfouraddress.decode('utf-8')        
        #print("reading_beforehex",reading_beforehex)
        #print("reading",reading)
        #print("start_code",start_code)
        #print("ADRES",sixtyfouraddress)
        
        print("datata recive",asciidata)
            
         
        try:
            
            #if sixtyfouraddress1 == "AAA":
            decodedasciidata1=asciidata.decode('utf-8')
            dataArray1 =decodedasciidata1.split(',')
            T1 =    float(dataArray1[0])                
            N1 =    float(dataArray1[1])                                
            N2 =    float(dataArray1[2])
            T2 =    float(dataArray1[3])
            Z =    float(dataArray1[4])
            g =    float(dataArray1[5])
             
            print("power = ",T1)
            print("current = ",N1)
            print("voltage = ",N2)
            print("temp = ",T2)
            print("oillevel1 = ",z)
            print("oillevel2 = ",g)
            
            
        except:
            print('cannot convert ')



        '''

        # for error detection
        
        print(reading)
        print(start_code)
        print(length)
        print(Frame_type)
        print(sixtyfouraddress)
        print(sixteenaddress)
        print(Receive_option)        
        print(data_set)         
        print('read without format =' , reading_beforehex)
        #print('read without format =' , reading_beforehex)
        #print('read without format =' , reading_beforehex)
        #print(sixtyfouraddress)

        '''

def Threadtwo():
    
    while True:

        currentValue1 = str(N1)
        powerValue2   = str(T1)
        voltageValue3 = str(N2)
        tempValue4    = str(T2)
        oilValue5     = "NORMAL"
        val6          = " "
        
        if Z==0:
            if g==1:
                oilValue5 = "LOW"
                tone()
            else:
              oilValue5 = "NORMAL"

        else:
            if g==0:
              oilValue5 = "HIGH"
              tone()
            
            

        if N1>6.0:
            val6 ="OVER CURRENT, " 
            tone()                

        if N2<12.8:
            val6+="UNDER VOLTAGE, "
            tone()
        
        if T2>60.0:
            val6+="TEMPRATURE IS HIGH"            
            tone()


            

        if T2<60.0:
            if N1<6.0:
                if N2>12.8:
                    val6 ="NORMAL"

        
        
        
        showcurrentValue1.set((str(currentValue1)))
        showpowerValue2.set((str(powerValue2)))
        showvoltageValue3.set((str(voltageValue3)))
        showtempValue4.set((str(tempValue4)))
        showoilValue5.set((str(oilValue5)))
        showValue6.set((val6))

   


           
def Threadthree():
    
    global power1
    global T1
    cnt=0
    plt.ion()
    fig, ax = plt.subplots()    
    fig.canvas.mpl_connect('close_event', handle_close_power)
    while logic1==True:         
        power1.append(T1)  
        drawnow(graphhr1)
        #plt.pause(.000001)
        cnt = cnt+ 1
        print ('count',cnt)                    
        if(cnt>100):
            power1.pop(0)
    plt.close()

    
def Threadfour():
    global Temperature1
    global T2
    cnt=0
    plt.ion()
    fig1, ax1 = plt.subplots()    
    fig1.canvas.mpl_connect('close_event', handle_close_temp) 
    while logic2==True:         
        Temperature1.append(T2)  
        drawnow(graphhr2)
        #plt.pause(.000001)
        cnt = cnt+ 1
        print ('count',cnt)                    
        if(cnt>100):
            Temperature1.pop(0)
    plt.close()   
   
def handle_close_power(evt):
    global logic1   
    logic1 = False
    print('Closed Power Figure!')
    print(logic1 )

def handle_close_temp(evt):
    global logic2
    logic2 = False
    print('Closed Temperature Figure')
    print(logic2)

def serialreadStart():
    threading.Thread(target=ThreadOne).start()

def dataupdate():
    threading.Thread(target=Threadtwo).start()

#def historyread():
    #global logic2
    #print(logic2)

def tempread():
    global logic2
    logic2 = True
    print(logic2)
    print('open temp Figure!')
    threading.Thread(target=Threadfour).start()
   
def powerread():
    global logic1
    logic1 = True
    print(logic1)
    print('open power Figure!')
    threading.Thread(target=Threadthree).start()
    

showcurrentValue1=StringVar()
showpowerValue2=StringVar()
showvoltageValue3=StringVar()
showtempValue4=StringVar()
showoilValue5=StringVar()
showValue6=StringVar()



# initial setting

SerialPortConnection()

# Place Power Curve  Plot Button
   
plotButton = Button(displayWindow, text ="POWER CURVE", bg = "yellow", command=powerread, font = ('Cambria', '8', 'bold'))
plotButton.place(x = 20, y = 500, height = 40, width = 120)


# Place Temp Curve  Plot Button
plotButton = Button(displayWindow, text ="TEMPERATURE CURVE", bg = "yellow", command=tempread, font = ('Cambria', '8', 'bold'))
plotButton.place(x = 155, y = 500, height = 40, width = 150)

# Place Previous Day Record  Plot Button

#plotButton = Button(displayWindow, text ="HISTORY", bg = "blue", command=history, font = ('Cambria', '8', 'bold'))
#plotButton.place(x = 320, y = 510, height = 30, width = 70)

#Serial Data Read
plotButton = Button(displayWindow, text ="Serial Data", bg = "pink", command=serialreadStart, font = ('Cambria', '6', 'bold'))
plotButton.place(x = 520, y = 500, height = 20, width = 100)

# Place EXIT Buttons

exitButton = Button(displayWindow, text ="Exit", bg = "blue",fg ="white", command = displayWindow.destroy, font = ('Cambria', '6', 'bold'))
exitButton.place(x = 700, y = 560, height = 20, width = 50)


# Placing read (DATA READ) button of TF
plotButton = Button(displayWindow, text ="Data Read", bg = "pink", command=dataupdate, font = ('Cambria', '6', 'bold'))
plotButton.place(x = 630, y = 500, height = 20, width = 70)

#.......................................TF details....................

# Placing Text label of current
t1 = Label(displayWindow, fg ="white",bg="green", text = 'CURRENT(A):', font = ('Cambria','9', 'bold'))
t1.place(x = 470, y = 160, height = 35, width = 200)

# Placing Text of current value  
txt1 = Label(displayWindow, bg= 'white', fg ="black",textvariable=showcurrentValue1, font= ('Cambria', '9', 'bold'))
txt1.place(x = 500, y = 200, height = 30, width = 150)

# Placing Text label of power
t2 = Label(displayWindow, fg ="white", bg="brown",text = 'TOTAL POWER OUTPUT(W):', font = ('Cambria','9', 'bold'))
t2.place(x = 300, y = 80, height = 35, width = 200)

# Placing Text Field of power value   
txt2 = Label(displayWindow, bg= 'white', fg ="black",textvariable=showpowerValue2, font= ('Cambria', '9', 'bold'))
txt2.place(x = 325, y = 120, height = 30, width = 150)

# Placing Text label of voltage
t3 = Label(displayWindow, fg ="white",bg="green", text = 'VOLTAGE(V):', font = ('Cambria','9', 'bold'))
t3.place(x = 130, y = 160, height = 35, width = 200)

# Placing Text of voltage value  
txt3 = Label(displayWindow, bg= 'white', fg ="black",textvariable=showvoltageValue3, font= ('Cambria', '9', 'bold'))
txt3.place(x = 160, y = 200, height = 30, width = 150)

# Placing Text label of temprature
t4 = Label(displayWindow, fg ="white",bg="red", text = 'TEMPERATURE(°C):', font = ('Cambria','9', 'bold'))
t4.place(x = 130, y = 240, height = 35, width = 200)

# Placing Text of Temprature value   
txt4 = Label(displayWindow, bg= 'white', fg ="black",textvariable=showtempValue4, font= ('Cambria', '9', 'bold'))
txt4.place(x = 340, y = 243, height = 30, width = 150)

# Placing Text label of Oil Level
t5 = Label(displayWindow, fg ="white",bg="orange", text = 'OIL LEVEL:', font = ('Cambria','9', 'bold'))
t5.place(x = 130, y = 300, height = 35, width = 200)

# Placing Text of oil level value

txt6 = Label(displayWindow, bg= 'white', fg ="black",textvariable= showoilValue5, font= ('Cambria', '9', 'bold'))
txt6.place(x = 340, y = 303, height = 30, width = 150)


# Placing Text label of warning status
t5 = Label(displayWindow, fg ="white",bg="dimgray", text = 'WARNING STATUS:', font = ('Cambria','9', 'bold'))
t5.place(x = 130, y = 400, height = 35, width = 200)

# Placing Text of warning status   
txt7 = Label(displayWindow, bg= 'white', fg ="red",textvariable= showValue6, font= ('Cambria', '9', 'bold'))
txt7.place(x = 340, y = 365, height = 100, width = 450)
 
# Placing topic
t7 = Label(displayWindow, fg ="yellow",bg="black", text = 'TRANSFORMER HEALTH MONITOR V.1.0', font = ('Cambria','12', 'bold'))
t7.place(x = 190, y = 20, height = 35, width = 400)

# Placing © 
t7 = Label(displayWindow, fg ="blue",bg="black", text = '© Faculty of Project.INS Valsura', font = ('Cambria','8', 'bold'))
t7.place(x = 190, y = 570, height = 35, width = 400)


   
displayWindow.mainloop()
