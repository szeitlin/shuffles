__author__ = 'szeitlin'

from collections import deque


def make_deck(n):
    """
    For simplicity, just make a list of sequential cards.
    Could potentially do something fancier here.

    :param n: deck of n unique cards (int)
    :param c: cut the deck c cards from the top (int)
    :return:
    """
    if n is None:
        print("n cannot be none!")

    #inefficient way first: make lists for each
    cards = [x for x in range(1,n+1)]
    return cards

def shuffle(cards, c):
    """
    Cut the cards at given position.
    Put the bottom card from the top portion followed by
    the bottom card from the bottom portion.
    Repeat until one portion is used up.
    Remaining cards go on top.

    :param: cards (list of int)
    :param: c, where to cut the deck (int)
    :return: shuffled cards (list of int)
    """
    top = cards[0:c]
    bottom = cards[c:]

    stopping_criteria = min(len(top), len(bottom))

    newstack = deque()

    for i in range(stopping_criteria):
        newstack.append(top.pop())
        newstack.append(bottom.pop())

    if len(top) > 0:
        newstack.extendleft(top)
    if len(bottom) > 0:
        newstack.extendleft(bottom)

    #print(newstack)
    return newstack

def zip_shuffle(cards, c):
    """
    Alternative implementation, see if this is faster (esp. on bigger lists).

    :param cards: list of int
    :param c: where to cut the deck (int)
    :return: shuffled cards (list of int)
    """
    top = cards[0:c]
    bottom = cards[c:]

    smaller = min(len(top), len(bottom))

    oddeven = lambda x: x % 2

    #idea to create and/or combine the top and bottom directly, rather than pop & append?


def shuffle_until(n, c, times=0):
    """
    shuffle a specific number of times, and count as you go.
    helper function for development & debugging.

    :param cards: (list of int)
    :param times: specify how many times to shuffle (int)
    :return: shuffled deck (list of int), and number of times (int)

    >>> shuffle_until(3, 1, 1)
    ([2, 1, 3], 1)
    >>> shuffle_until(5, 3, 1)
    ([1, 3, 5, 2, 4], 1)
    """
    shuffle_count = 0

    if times != 0:
        for i in range(times):
            newstack = shuffle(n,c)
            shuffle_count += 1
            return list(newstack), shuffle_count #should be equal to times
    else:
        return None

def shuffle_recursive(cards, c, shuffle_count):
    """
    shuffle until the original order is restored, and count as you go.
    assuming for now that original order is sequential and first card is always 1.
    This only works up to the max recursion depth of 999.

    :param n: deck size to pass to shuffle function (int)
    :param c: cut size to pass to shuffle function (int)
    :param newstack: variable to hold the list during shuffling
    :return: (newstack (shuffled list), shuffle_count (int)) as a tuple

    >>> shuffle_recursive([1,2,3,4,5], 3, 0)
    4
    """
    newstack = shuffle(cards,c)
    #print(cards, newstack) #for debugging

    shuffle_count +=1
    #print(shuffle_count)

    if list(newstack) == [x for x in range(1, len(cards)+1)]: #stopping criteria
        return shuffle_count

    else:
        return shuffle_recursive(list(newstack), c, shuffle_count)

def shuffle_iterative(cards, c, shuffle_count):

    original_order = [x for x in range(1, len(cards)+1)]

    for i in range(100000):
        newstack = shuffle(cards, c)
        shuffle_count +=1

        if lists_identical(list(newstack), original_order): #stopping criteria
            break
        else:
            cards = list(newstack)

    return shuffle_count

def lists_identical(lista, listb):
    """
    helper to speed up checking.
    If any item is in the wrong place, break early and return False.
    Otherwise return True.
    :param lista: list of int
    :param listb: list of int
    :return: bool
    """
    flag = True

    for a,b in zip(lista, listb):
        if a!=b:
            flag = False
            break

    return flag


if __name__=='__main__':
    bigdeck = make_deck(1002)
    result = shuffle_iterative(bigdeck, 101, 0)
    print(result)
