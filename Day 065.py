'''
This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12

'''
def spiral(arr,m,n):
    k=0
    l=0
    while (k < m and l < n):
        for i in range(l, n):
            print(arr[k][i], end = " ")
        k += 1
        for i in range(k, m):    
            print(arr[i][n - 1], end = " ")
        n -= 1
        if ( k < m):
            for i in range(n - 1, (l - 1), -1) :
                print(arr[m -1][i], end = " ")  
            m -= 1
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(arr[i][l], end = " ")
            l += 1
    

m = int(input("Number of rows : "))
n = int(input("Number of columns : "))
arr =[list(map(int,input().split()[:n])) for j in range(m)]

print(arr)
print("Spiral array ")
spiral(arr,m,n)



