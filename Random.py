import random
import time
while True:
 sc = 0
 x = random.randint(1,1)
 y = random.randint(1,1)
 num = print ("Your number: %d" % x )
 z = print ("Random number is: %d" % y )
 print (sc)
 if x == y:
    print ("Correct")
    sc = sc + 1
 else:
    print ("Wrong")
    sc = sc - 1
 print ("score : %d" % sc)
 time.sleep(3)
 print ("")
