from random import randint,randrange,sample
x =[]
for i in range(100):
    x.append(randrange(1000000000,10000000000,2))

print(x)

   

y = sample(x,2)
print("the winer is:",y)