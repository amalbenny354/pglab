a=int(input("enter a:"))
b=int(input("enter b:"))
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")
while True:
    c=int(input("enter your choice:"))
    if(c==1):
        d=a+b
        print("sum is {}:".format(d))
    elif(c==2):
        d=a-b
        print("difference is {}:".format(d))
    elif(c==3):
        d=a*b
        print("mul is {}:".format(d))
    elif(c==4):
        d=a/b
        print("div si {}:".format(d))
    else:
        print("wrong choice ")
