import time
import board # type: ignore
import neopixel # type: ignore


num_pixel = 300
pixel1=neopixel.NeoPixel(board.D18, num_pixel, brightness=0.2, auto_write= False)
i=0

thirtycolors=[(93, 138, 168), (255, 3, 62), (153, 102, 204), (164, 198, 57), (0, 255, 255), (189, 51, 164), (255, 8, 0), (0, 191, 255),
              (153, 50, 204), (255, 247, 0), (0, 84, 180), (207, 181, 59), (39, 59, 226), (207, 207, 196), (204, 51, 51), (1, 121, 111), 
              (252, 116, 253), (255, 143, 0), (227, 11, 93), (0, 64, 64), (183, 110, 121), (0, 86, 63), (35, 41, 122), (252, 15, 192), 
              (69, 206, 162), (163, 45, 23), (135, 206, 235), (0, 255, 127), (70, 130, 180), (160, 32, 240)]
while i<=num_pixel:
    j=0
    while j<10:
        pixel1[i+j]=thirtycolors[int(i/10)]
        j+=1
    i+=10
    pixel1.show()