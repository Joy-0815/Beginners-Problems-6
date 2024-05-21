def saygm(name):
    print("Good morning, " + name + "!")
    return saygm

def sayga(name):
    print("Good afternoon, " + name + "!")
    return sayga

def saygn(name):
    print("Good night, " + name + "!")
    return saygn

name = input("What is your name?")
time = int(input("What time is it?"))

if 0 <= time <= 1259:
    saygm(name)
elif 1300 <= time <= 1759:
    sayga(name)
elif 1800 <= time <= 2359:
    saygn(name)