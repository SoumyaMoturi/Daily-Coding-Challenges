'''
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

'''


def word_search(puzzle, word,r,c):
    word_len = len(word)
    for r in range(r):
        for c in range(c):
            left_right = ''.join([puzzle[r][i] for i in range(c, len(puzzle[0]))])[:word_len]
            up_to_down = ''.join([puzzle[i][c] for i in range(r, len(puzzle))])[:word_len]
            if word in (left_right,up_to_down):
                return True
    return False

r=int(input("Enter row size : "))
c=int(input("Enter column size : "))
puzzle = [list(input().split()[:c]) for i in range(r)]
word= input("Enter the word that need to be searched : ")
print(word_search(puzzle,word,r,c))
