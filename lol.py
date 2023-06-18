import random
passer = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long = int(input("какая длинна пароля???"))
pasword =""
for i in range(long):
    pasword += random.choice(passer)
print (pasword)