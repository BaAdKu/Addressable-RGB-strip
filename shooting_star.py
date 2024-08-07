import time
import board # type: ignore
import neopixel # type: ignore

num_pixel=300

pixel1=neopixel.NeoPixel(board.D18, num_pixel, brightness=0.2, auto_write= False)

def shootingstar ():
    x=0
    pixel1.fill((30, 0, 80))
    pixel1.show()

    while x<num_pixel: 
        pixel1[x]=(105, 85, 127)
        pixel1[x-1]=(197, 170, 193)
        pixel1[x-2]=(255, 255, 255)
        pixel1[x-3]=(255, 255, 255)
        pixel1[x-4]=(255, 255, 255)
        pixel1[x-5]=(255, 255, 255)
        pixel1[x-6]=(200, 159, 189)
        pixel1[x-7]=(136, 100, 148)
        pixel1[x-8]=(96, 62, 122)
        pixel1[x-9]=(71, 39, 107)
        pixel1[x-10]=(55, 24, 96)
        pixel1[x-11]=(46, 15, 90)
        pixel1[x-12]=(40, 10, 87)
        pixel1[x-13]=(36, 6, 84)
        pixel1[x-14]=(34, 4, 82)
        pixel1[x-15]=(32, 3, 81)
        pixel1[x-16]=(30, 0, 80)
        x+=1
        pixel1.show()

        # print("one step")
        time.sleep(0.001)

    time.sleep(1)
    pixel1.fill((30, 0, 80))
    # input("press anything to continue")
    time.sleep(1)
    pixel1.fill((0,0,0))
    pixel1.show()