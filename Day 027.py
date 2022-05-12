'''
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.

'''
def balancedParanthesis(s):
    stack=[]
    for i in s:
        if i in '({[':
            stack.append(i)
            continue
        elif i in '})]': 
            if i == '}' and stack[-1] != '{':
                return False
            elif i == ']' and stack[-1] != '[':
                return False
            elif i == ')' and stack[-1] != '(':
                return False
            stack.remove(stack[-1])
    return stack == []
            
s=input()
if balancedParanthesis(s):
    print("Balanced")
else:
    print("Not Balanced")