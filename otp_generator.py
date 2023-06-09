import random


def otp():
    otp=""
    for i in range(6):
        otp+=str(random.randint(0,9))

    return otp

if __name__=="__main__":
    print(otp())