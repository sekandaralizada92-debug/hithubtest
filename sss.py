from random import randint,randrange,sample
x =[]
for i in range(100):
    x.append(randrange(1000000000,10000000000,2))
print(x)
y = sample(x,2)
print("the winer is:",y)

                 /first project/

def user_case (name,age,email):
   print("your name is: ",name,"and your age is: ",age, " and your email is: ",email)
name = input("enter your name: ")
age = int(input("enter your age: "))
email = input("enetr your enail: ")
user_case(name,age,email)

                 /second porject/

def opreation(firstNumber,secondNumber):
    print("the sum is: ",firstNumber+secondNumber)
    print("the munins is: ",firstNumber-secondNumber)
    print("the mul is: ",firstNumber*secondNumber)
    print("the dev is: ",firstNumber/secondNumber)
firstNumber = int(input("inter your first Number: "))
secondNumber = int(input("inter your second Number: "))
print(opreation(firstNumber,secondNumber))

                 /thired project/

list = [1,2,3,4]
def opreationOfList(list):
    jam = 0
    zarb = 1
    manf = 0
    taqsem=0
    for i in list:
        jam += i
        manf -=i
        zarb *=i
        taqsem /= i
    return jam ,zarb,manf,taqsem
print(opreationOfList(list))