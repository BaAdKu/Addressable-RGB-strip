import time
import board
import neopixel

pixel1=neopixel.NeoPixel(board.D18, 300, brightness=0.2)

x=0

pixel1.fill((30, 0, 80))

while x<300: 
    pixel1[x]=        (105, 85, 127)
    pixel1[x-1]=      (197, 170, 193)
    pixel1[x-2]=      (255, 255, 255)
    pixel1[x-3]=      (255, 255, 255)
    pixel1[x-4]=      (255, 255, 255)
    pixel1[x-5]=      (255, 255, 255)
    pixel1[x-6]=      (200, 159, 189)
    pixel1[x-7]=      (136, 100, 148)
    pixel1[x-8]=      (96, 62, 122)
    pixel1[x-9]=      (71, 39, 107)
    pixel1[x-10]=     (55, 24, 96)
    pixel1[x-11]=     (46, 15, 90)
    pixel1[x-12]=     (40, 10, 87)
    pixel1[x-13]=     (36, 6, 84)
    pixel1[x-14]=     (34, 4, 82)
    pixel1[x-15]=     (32, 3, 81)
    pixel1[x-16]=     (30, 0, 80)
    
    x+=1
    time.sleep(0.07)

time.sleep(4)
pixel1.fill((30, 0, 80))
input("press anything to continue")
pixel1.fill((0,0,0))

pixel1.disp