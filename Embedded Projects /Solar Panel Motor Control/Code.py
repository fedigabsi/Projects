from machine import Pin , PWM
import time

counter = 0
angle =0
buttonA = Pin(15, Pin.IN, Pin.PULL_DOWN)
buttonB = Pin(0, Pin.IN, Pin.PULL_DOWN)
servo = PWM(Pin(5,Pin.OUT),freq=50)

segment = [
    Pin( 27 ,Pin.OUT), #a
    Pin( 14 ,Pin.OUT), #b
    Pin( 12 ,Pin.OUT), #c
    Pin( 13 ,Pin.OUT), #d
    Pin( 19 ,Pin.OUT), #e
    Pin( 32 ,Pin.OUT), #f
    Pin( 4 ,Pin.OUT)   #g
]

numbers = [
    [1,1,1,1,1,1,0],  # 0
    [0,1,1,0,0,0,0],  # 1
    [1,1,0,1,1,0,1],  # 2
    [1,1,1,1,0,0,1],  # 3
    [0,1,1,0,0,1,1],  # 4
    [1,0,1,1,0,1,1],  # 5
    [1,0,1,1,1,1,1],  # 6
    [1,1,1,0,0,0,0],  # 7
    [1,1,1,1,1,1,1],  # 8
    [1,1,1,1,0,1,1]   # 9
]

def clear():
    for i in range(7):
         segment[i].value(0)

def display(n) :
    digit = numbers[n]
    for i in range (7) :
        segment[i].value(digit[i])

def map_value(x, in_min, in_max, out_min, out_max):
    x = max(in_min, min(x, in_max))  # clamp
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min 

def rotate(A):
    A = int ( map_value (A,0,180,1500,8000))
    servo.duty_u16(A)

while True :
    stateA = buttonA.value()
    stateB = buttonB.value()
    if not stateA == 1 and counter < 9 :
        counter = counter + 1 
        time.sleep_ms(200)
    display(counter)
    if not stateB == 1 and counter > 0 :
        counter = counter - 1 
        time.sleep_ms(200)
    display(counter)
    rotate(counter*20)
    time.sleep_ms(50)
