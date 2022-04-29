'''
This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.

'''
from random import randint
def Shuffle(cards):
    n=len(cards)
    for i in range(n):
        j= randint(1,n)-1
        cards[i],cards[j] = cards[j],cards[i]
    return cards
  

cards = [cards for cards in range(1, 53)]
print(Shuffle(cards))