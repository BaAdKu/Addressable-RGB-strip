import time
import board
import neopixel

pixel1=neopixel.NeoPixel(board.D18, 300, brightness=0.2)

x=0

pixel1.fill((204, 0, 204))

while x<300: 
    pixel1[x]=(102, 102, 255)
    pixel1[x-7]=(153, 153, 0)
    pixel1[x-21]= (255, 204, 204)
    x+=1
    time.sleep(0.05)

time.sleep(4)

pixel1.fill((0,0,0))
