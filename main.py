"""import rp2
import utime
from picuno import Neopixel, board
import machine
from machine import Pin

sens1 = machine.Pin(12, machine.Pin.IN)
sens2 = machine.Pin(15, machine.Pin.IN)
sens3 = machine.Pin(20, machine.Pin.IN)

numpix = 30
pixels = Neopixel(numpix, 0, 17, "GRB")
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
awll=(85,85,85)
onetwo=(127,127,0)
twothree=(0,127,127)
noned = (0,0,0)
color0 = red
pixels.brightness(50)

board.lvlpins()
state = 0
x = sens1.value()
y = sens2.value()
z = sens3.value()

def inst_1():
    global x
    a=[]
    
    if x==1:
        a.append(x)
    else:
        a.clear()
    if len(a)>42:
        pixels.fill(noned)
        pixels.show()
        a.clear()
def inst_2():
    global y
    b=[]
    
    if y==1:
        b.append(y)
    else:
        b.clear()
    if len(b)>42:
        pixels.fill(noned)
        pixels.show()
        b.clear()
def inst_3():
    global z
    c=[]
    
    if z==1:
        c.append(x)
    else:
        c.clear()
    if len(c)>42:
        pixels.fill(noned)
        pixels.show()
        c.clear()
while True:
    #print(x)
    utime.sleep(0.12)
    if x == 1 and y==1 and z==1:
        pixels.fill(awll)
        pixels.show()
        utime.sleep(0.12)
        inst_1()
        inst_2()
        inst_3()
         
    elif x == 1 and y==1:
        pixels.fill(onetwo)
        pixels.show()
        utime.sleep(0.12)
        inst_2()
        inst_1()
        
    elif y==1 and z==1:
        pixels.fill(twothree)
        pixels.show()
        utime.sleep(0.12)
        inst_2()
        inst_3()
    
    elif x==1:
        pixels.fill(red)
        pixels.show()
        utime.sleep(0.12)
        inst_1()
    
    elif y==1:
        pixels.fill(green)
        pixels.show()
        utime.sleep(0.12)
        inst_2()
    
    elif z==1:
        pixels.fill(blue)
        pixels.show()
        utime.sleep(0.12)
        inst(3)
    
    else:
        pixels.fill(noned)
        pixels.show()
        continue
        
"""
"""import rp2
import utime
from picuno import Neopixel, board
import machine
from machine import Pin

sens1 = machine.Pin(12, machine.Pin.IN)
sens2 = machine.Pin(15, machine.Pin.IN)
sens3 = machine.Pin(20, machine.Pin.IN)

numpix = 30
pixels = Neopixel(numpix, 0, 17, "GRB")
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
awll = (85, 85, 85)
onetwo = (127, 127, 0)
twothree = (127, 127, 127)
noned = (0, 0, 0)
pixels.brightness(50)

board.lvlpins()

def inst_1(x):
    a = []
    if x == 1:
        a.append(x)
    else:
        a.clear()
    if len(a) > 42:
        pixels.fill(noned)
        pixels.show()
        a.clear()

def inst_2(y):
    b = []
    if y == 1:
        b.append(y)
    else:
        b.clear()
    if len(b) > 42:
        pixels.fill(noned)
        pixels.show()
        b.clear()

def inst_3(z):
    c = []
    if z == 1:
        c.append(z)
    else:
        c.clear()
    if len(c) > 42:
        pixels.fill(noned)
        pixels.show()
        c.clear()

while True:
    x = sens1.value()
    y = sens2.value()
    z = sens3.value()
    
    utime.sleep(0.12)
    
    if x == 0 and y == 0 and z == 0:
        pixels.fill(awll)
        pixels.show()
        utime.sleep(0.12)
        inst_1(x)
        inst_2(y)
        inst_3(z)
    elif x == 0 and y == 0:
        pixels.fill(onetwo)
        pixels.show()
        utime.sleep(0.12)
        inst_2(y)
        inst_1(x)
    elif y == 0 and z == 1:
        pixels.fill(twothree)
        pixels.show()
        utime.sleep(0.12)
        inst_2(y)
        inst_3(z)
    elif x == 0:
        pixels.fill(red)
        pixels.show()
        utime.sleep(0.12)
        inst_1(x)
    elif y == 0:
        pixels.fill(green)
        pixels.show()
        utime.sleep(0.12)
        inst_2(y)
    elif z == 1:
        pixels.fill(blue)
        pixels.show()
        utime.sleep(0.12)
        inst_3(z)
    else:
        pixels.fill(noned)
        pixels.show()
        utime.sleep(0.12)


        """
#importing required libraries
import rp2
import utime
from picuno import Neopixel, board
import machine
from machine import Pin

#gathering input from each sensor
sens1 = machine.Pin(12, machine.Pin.IN)
sens2 = machine.Pin(15, machine.Pin.IN)
sens3 = machine.Pin(8, machine.Pin.IN)

#code for using neopixel
numpix = 30
pixels = Neopixel(numpix, 0, 17, "GRB")
#defining various colours
green = (0, 255, 0)#for centre sensor
blue = (0, 0, 255)#for right sensor
red = (255, 0, 0)#for for left sensor
awll = (255, 192, 203)#for very large potholes 
onetwo = (255, 255, 0)#for intermediate potholes oriented to centre-left
twothree = (13, 152, 186)#for intermediate potholes oriented to the centre-right
noned = (0, 0, 0)#when no pothole is detected
pixels.brightness(50)#brightnness

board.lvlpins()

#precaution code for sensors sendinng  a sinngle output for too long
def inst_1(x):
    a = []
    if x ==1:
        a.append(x)
    else:
        a.clear()
    if len(a) > 42:#about 5 seconds
        pixels.fill(noned)#if each sensors sends an output for more than 5 seconds, it blinks once
        pixels.show()
        a.clear()

#repeat for other two sensors
def inst_2(y):
    b = []
    if y == 1:
        b.append(y)
    else:
        b.clear()
    if len(b) > 42:
        pixels.fill(noned)
        pixels.show()
        b.clear()

def inst_3(z):
    c = []
    if z == 1:
        c.append(z)
    else:
        c.clear()
    if len(c) > 42:
        pixels.fill(noned)
        pixels.show()
        c.clear()

#fun begins here
while True:#To run loop till the connection is plugged off
    x = sens1.value()#Analog input from each sensor to Picuno board
    y = sens2.value()
    z = sens3.value()
    
    utime.sleep(0.12)#refreshes every 0.12s
    
    if x == 1 and y == 1 and z == 1:#for large potholes
        pixels.fill(awll)#displays colour in neopixel
        pixels.show()
        utime.sleep(0.12)#refreshes ever 0.12s
        
        #runs precautions(recursion)
        inst_1(x)
        inst_2(y)
        inst_3(z)
    elif x == 1 and y == 1:#intermediate potholes oriented to centre-left
        pixels.fill(onetwo)#display colours...
        pixels.show()
        utime.sleep(0.12)
        inst_2(y)
        inst_1(x)
    elif y == 1 and z == 1:#potholes oriented to centre-right
        pixels.fill(twothree)
        pixels.show()
        utime.sleep(0.12)
        inst_2(y)
        inst_3(z)
    elif z == 1:#small potholes to right
        pixels.fill(blue)
        pixels.show()
        utime.sleep(0.12)
        inst_3(z)
    elif x == 1:#small potholes to left
        pixels.fill(red)
        pixels.show()
        utime.sleep(0.12)
        inst_1(x)
    elif y == 1:#small potholes to centre
        pixels.fill(green)
        pixels.show()
        utime.sleep(0.12)
        inst_2(y)
    else:#potholes  to centre
        pixels.fill(noned)
        pixels.show()
        utime.sleep(0.12)

        
    
    
        