from random import random , uniform , randint,randrange,choice,sample,shuffle


counter = 0
scor1 = 0
scor2 = 0
while scor1  < 19 or scor2  < 19:
    enter = input("enter your key: ")
    if enter == 's':
        scor1 +=  randint(1,6)
        counter +=1
    elif enter == 'a':
        scor2 +=  randint(1,6)
        counter +=1
    else:
        break
    if scor1 > 20 :
         scor1 = 20
    elif scor2 > 20:
         scor2 = 20
         
    
    

    print(scor1)
    print(scor2)
if scor2 < 10 :
        print("scor2 is win her scor is: ",scor2)
elif scor1 < 10:
        print("scor1 is win her scor is: ",scor1)    