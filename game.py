# welcome to game v2.0 by bobtie658
# currently functional, will add comments later
# 2.0 log: added multiple rounds, potions and prevented the same animal from coming up across different rounds


print("welcome to game, enjoy your stay")

i1 = input("what is your first item ")

i2 = input("what is your second item ")

print("")
print("")

import random

du=False
ca=False
fo=False
sn=False
hw=False
ele=False
rh=False
ho=False
sh=False
rsh=False

i3 = ""

i3d = 0

h = 150

p = 5

r = 5

rn = 1

x = 0

i1d = random.randint(1,20)

i2d = random.randint(1,20)

while not (h<=0) or not (r==0):

    while not x == rn:

        mid = random.randint(1,10)

        if (mid == 1) and not du == True:
            m = "duck"
            mh = 30
            dm = 1
            dx = 10
            x=x+1
            du = True

        elif (mid == 2) and not ca == True:
            m = "cat"
            mh = 40
            dm = 5
            dx = 10
            x=x+1
            ca = True

        elif (mid == 3) and not fo == True:
            m = "fox"
            mh = 50
            dm = 7
            dx = 15
            x=x+1
            fo = True

        elif (mid == 4) and not sn == True:
            m = "snake"
            mh = 60
            dm = 9
            dx = 15
            x=x+1
            sn = True

        elif (mid == 5) and not hw == True:
            m = "hawk"
            mh = 70
            dm = 10
            dx = 15
            x=x+1
            hw = True

        elif (mid == 6) and not ele == True:
            m = "elephant"
            mh = 80
            dm = 15
            dx = 17
            x=x+1
            ele = True

        elif (mid == 7) and not rh == True:
            m = "rhino"
            mh = 90
            dm = 15
            dx = 17
            x=x+1
            rh = True

        elif (mid == 8) and not ho == True:
            m = "hippo"
            mh = 100
            dm = 17
            dx = 20
            x=x+1
            ho = True

        elif (mid == 9) and not sh == True:
            m = "shark"
            mh = 110
            dm = 15
            dx = 22
            x=x+1
            sh = True

        elif (mid == 10) and not rsh == True:
            m = "really big shark"
            mh = 120
            dm = 20
            dx = 25
            x=x+1
            rsh = True

    mho = mh
    
    print("round "+str(rn))
    print("you will fight a "+m+" with "+str(mh)+" health")
    print("to attack the "+m+" type 'a', to switch items, press 's' and to use a potion, press 'p'")

    while not (mh <= 0) or not (h <= 0):
        print("")
        print("")
        print("you are currently attacking with a "+i1)
        print("your health: "+str(h))
        print(m+" health: "+str(mh))
        print("you have "+str(p)+" potions remaining")
    
        i = input()
        print("")
    
        if i == "a":
        
            c = random.randint(1,10)
        
            if c == 1:
               print("you miss")
        
            elif c == 10:
                print ("critical hit")
                mh = (mh-(2*i1d))
            
            else:
                mh = (mh-i1d)
            
        if i == "s":
            i3 = i1
            i1 = i2
            i2 = i3
        
            i3d = i1d
            i1d = i2d
            i2d = i3d
        
        if i == "p" and p>0 and h<150:
            oh = h
            h = h+75
            p = p-1
            
            if h>150:
                h = 150
            print("you used a potion and restored "+str(h-oh)+" health")
        
        h = (h-random.randint(dm,dx))
    
        if mh <= 0:
            print("you won the fight")
            break
        
        elif h <= 0:
            print("you lost")
            break
    
    if h<=0:
        break
    
    if h>0 and r>0:
        r = r-1    
        rn = rn+1
        print("")
        print("you have "+str(h)+" health remaining and "+str(p)+" potions remaining, how many would you like to use?")
        up = int(input(""))
        oh = h
        
        if (up<p):
            h = (h+(75*up))
            p=p-up
        else:
            h = h+(75*p)
            p=0
    
        if h>150:
            h = 150
    
        print("you restored "+str(h-oh)+" health")
    
if r==0:
    print("")
    print("congratulations, you won!")
input()
