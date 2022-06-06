"""
Given an binary array A of size N and a range L,R.now find out the decimal Equivalent of range A[l] to A[R](both inclusive)(let decimal equivalent be X) so you will give x chocolates to Rahul.After recieving X chocolates  from you and the chocolates he already has he will be either Happy or sad and you will have to print it.
odd number of chocolates "happy" else"Sad".

"""

size=int(input())
s=list(input())
n=int(input())
total =0
for i in range(n):
    l,h=map(int,input().split())
    print(l,h)
    if(l == h):
        num = s[l+1]
    else:
        num = s[l-1:h]
    total+=int("".join(num),2)
    if(total%2 == 0):
        print("Sad")
    else:
        print("Happy")


    