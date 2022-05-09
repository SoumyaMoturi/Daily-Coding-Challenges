def mul(n,x):
    c=0
    arr=[]
    r=[]
    print("\nArray elements are : \n ------------------------")
    for i in range(n):
        for j in range(n):
            print((i+1)*(j+1),end = " ")
            if x == (i+1)*(j+1):
                c+=1
        print()
    print("-------------------------")
    return c
n=int(input())
x=int(input())
print(x,"is displayed ",mul(n,x)," times in the array.")