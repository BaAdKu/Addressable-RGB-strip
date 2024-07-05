import time
import board # type: ignore
import neopixel # type: ignore

pixelnum=300
pixel1=neopixel.NeoPixel(board.D18, pixelnum, brightness=0.2)

def timer_start( sec):
    pixel1.fill((20, 20, 20))

    timersecs = int(sec)

    x=timersecs/pixelnum

    print("one led every " + str(x) + " seconds")

    i=0
    while i<pixelnum:
        pixel1[i]=(255, 255, 0)
        i+=1
        time.sleep(x)
    i=0
    while i<pixelnum:
        pixel1[i]=(255, 0, 0)
        i+=1
        time.sleep(x)

    i=0
    while i<3:
        pixel1.fill((255,0,0))
        time.sleep(0.2)
        pixel1.fill((0,0,0))
        time.sleep(0.2)
        i+=1

    pixel1.fill((0,0,0))

