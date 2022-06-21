'''
This problem was asked by Cisco.

Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

'''
def swapEvenAndOdd(n):
    s="".join([n[i]+n[i-1] for i in range(1,len(n),2)])
    return s
    
n=int(input())
print("Swapped : "+str(swapEvenAndOdd(str(n))))


# def swapEvenAndOdd(x):
#     return (x & 0b10101010) >> 1 | (x & 0b01010101) << 1
