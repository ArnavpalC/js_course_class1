n=int(input("enter the number to be checked: "))
flag=False
if n>1:
    for i in range(2,n):
        if (n %i)==0:
            flag=True
            break




if flag:
    print(n,"it is not a prim number")

else :
    print(n,"it is a prime number")
