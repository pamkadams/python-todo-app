import random

def generateRandom(upper):
    r = random.randint(1, upper)
    return r

hello = 7 #todo change this
print(hello)
print(hello)
print(hello)
run = True
num1 = generateRandom(10)
num2 = generateRandom(10)
result = num1 + num2
while run:
    print(hello)
    print(hello)
    ans = input("What is  " + str(num1) + "x " + str(num2) + " ?")

    if ans.isdigit():
        if int(ans) == result:
            print("Correct")
            run = False
        else:
            print("incorrect. Try again")
    else:
        print("Answer must be a positive number")