n=input("enter the string:")
if n[-3:]=='ing':
    n=n+'ly'
else:
    n=n+'ing'
print(n)
