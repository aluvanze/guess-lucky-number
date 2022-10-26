from random import randint
secret=randint(1,10)
for i in range(5):
     guess=int(input("enter your guess\n"))
     if guess==secret:
         print("you got it")
         break
     print("secret" ,secret )