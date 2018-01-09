import random
import time
sc = 0
while True:
 x = random.randint(1,10)
 y = random.randint(1,10)
 num = print ("Your number: %d" % x )
 z = print ("Random number is: %d" % y )
 if x == y:
    print ("Correct")
    sc += 1
 else:
    print ("Wrong")
    sc = 0
 print ("score : %d" % sc)
 time.sleep(3)
 print ("")
