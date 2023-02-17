def recur_fact(n):
    if(n==1):
        return n
    else:
        return n*recur_fact(n-1)
n=int(input("enter num:"))
if(n<0):
     print("not possible")
elif(n==0):
    print("1")
else:
    print("factorail is ",recur_fact(n))
