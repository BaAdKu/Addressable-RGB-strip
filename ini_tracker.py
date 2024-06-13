import time
import board
import neopixel

pixel1=neopixel.NeoPixel(board.D18, 300, brightness=0.2, auto_write= False)
char_num=int(input("Please enter the number of players"))
i=0
char_order=[0]*char_num
while i<char_num:
    print("enter the next person by their number") 
    char_order[i]=int(input())
    i+=1

pixel1.fill(0x202020)
pixel1.show()

i=0

while True:
    if input()!='c':
        break
    pixel1.fill(0x202020)
    pixel1.show()
    j=(char_order[i]-1)*(300/char_num)
    while j<(char_order[i]*(300/char_num)):
        pixel1[j]=0x00dd00
        j+=1
    pixel1.show()


pixel1.fill(0x000000)
pixel1.show()