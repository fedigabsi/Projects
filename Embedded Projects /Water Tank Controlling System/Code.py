from machine import Pin 
import time

trig = Pin (32, Pin.OUT)
echo = Pin (33, Pin.IN)
relayIn = Pin (26, Pin.OUT)
relayOut = Pin (27, Pin.OUT)
TON = TOFF = t = 0

while 1 :
    trig.on()
    time.sleep_us(10)
    trig.off()
    time.sleep_us(2)
    while echo.value() == 0 :
        TOFF = time.ticks_us()
    while echo.value() == 1 :
        TON = time.ticks_us()
    
    t = ( TON - TOFF ) / 2
    water = t * 0.0343
    time.sleep_ms(200)
    
    if water < 50 :
        relayIn.on()
        relayOut.off()
    elif water >350 :
        relayIn.off()
        relayOut.on()
    else :
        relayIn.on()
        relayOut.on()
