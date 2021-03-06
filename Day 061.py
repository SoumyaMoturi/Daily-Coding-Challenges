'''
This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.

'''
def power(x, y):
    if y < 0:
        return power(1 / x, -y)
    elif y == 0:
        return 1
    else:
        return x * power(x, y - 1)

x = int(input("Enter base element : "))
y = int(input("Enter power value : "))
print(power(x,y))