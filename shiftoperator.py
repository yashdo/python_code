print(-19<<3)
print(bin(19))   #00010011
                 #11101100(1st comp)
                 #       1 (add one)
                 #--------
                 #11101101 -->(-19) 
                 #01101000 -->left 3 value shift to right(remember in the case of left shift shift only 0s)
                 #10010111 -->(2nd compliments)
                 #       1
                 #----------
                 #10011000 ---(152)
print(int(0b011000))

##right shift
print(-24>>2)
print(bin(24))  #00011000 -->binary of 24 convert into bytes
                #11100111 ---> 1st compliment (-24) how will you prove this
                #       1
                #-----------
                #11101000  
                #00101000 -->shift right 2 with the left 2
                #11010111---> 2nds compliment
                #       1
                #--------------
                #11011000
print(bin(0b1010))
print(int(0b1010)) #2**0,2**1,2**2,2**3
                   #0,1,0,1
                   #1,2,4,8
print(bin(10)) #2,4,8,16,32,64
               #1,0,1,0


