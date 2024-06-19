import time
import board # type: ignore
import neopixel # type: ignore

pixel1=neopixel.NeoPixel(board.D18, 300, brightness=0.2, auto_write= False)
i=0
while i<=300:
    j=0
    while j<10:
        pixel1[i+j]=(255-i, 255-i+j, 255-i-j)
        j+=1
    i+=10
    pixel1.show()

    