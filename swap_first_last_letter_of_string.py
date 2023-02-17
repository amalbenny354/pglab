def swap(str1):
    first=str1[0]
    last=str1[-1]
    swapped=last+str1[1:-1]+first
    print(swapped)
string=input("enter string:")
print("swapped string is:")
swap( string)
