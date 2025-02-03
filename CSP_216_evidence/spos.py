import random
pw=[]
commonpw=[[1,2], [3,4]]

def create():
    for i in range (0,2):
        digit = random.randint(0,2)
        pw.append(digit)
    print (pw)

if pw not in commonpw:
    create()
else:
    print ("nuh uh")