import time
import board
import neopixel

num_pixel = 300
pixel1=neopixel.NeoPixel(board.D18, num_pixel, brightness=0.2, auto_write= False)
char_num=int(input("Please enter the number of players "))
i=0
char_order=[0]*char_num
while i<char_num:
    print("enter the next person by their number",end="\r", flush=True) 
    char_order[i]=int(input())
    i+=1

pixel1.fill(0x202020)
pixel1.show()

i=0

while True:
    if input()=='c':
        break
    
    pixel1.fill(0x202020)
    pixel1.show()

    j=int((char_order[i%char_num]-1)*(num_pixel/char_num))
    while j<(char_order[i%char_num]*(num_pixel/char_num)):
        pixel1[j]=(00, 221, 00)
        j+=1

    k=int((char_order[(i+1)%char_num]-1)*(num_pixel/char_num))
    while k<((char_order[(i+1)%char_num])*(num_pixel/char_num)):
        pixel1[k]=(221, 221, 00)
        k+=1

    pixel1.show()
    i+=1
    print ("this is round number " + str(int(i/char_num +1)) + " of the initiative",end="\r", flush=True)
    # if i==char_num:
    #     i=0

pixel1.fill(0x000000)
pixel1.show()