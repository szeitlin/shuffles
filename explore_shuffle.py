__author__ = 'szeitlin'

from shuffle import make_deck, shuffle_iterative
from collections import defaultdict
import pandas as pd

def explore_cases(deck_max_size):
    """
    Make some decks, shuffle and count to look for which ones are failing.
    :return: print deck size and shuffle counts
    """
    shuffle_count = 0

    for i in range(3, deck_max_size):
        cards = make_deck(i)
        for i in range(3, len(cards)-2):
            shuffle_count = shuffle_iterative(cards, i)
            print("deck_size {}, cut_size {}, shuffle_count {}".format(len(cards), i, shuffle_count))

def plot_cases(deck_max_size):
    """
    Make plottable results and look for patterns.
    :param deck_max_size:
    :return: pandas dataframe to plot
    """
    result_dict = {'deck_size':[], 'cut_size':[], 'shuffle_count':[]}

    for i in range(3, deck_max_size):
        cards = make_deck(i)
        for i in range(3, len(cards)-2):
            shuffle_count = shuffle_iterative(cards, i)
            result_dict['deck_size'].append(len(cards))
            result_dict['cut_size'].append(i)
            result_dict['shuffle_count'].append(shuffle_count)

    df = pd.DataFrame(result_dict)

    print(df.head())
    return df

if __name__=='__main__':
    plot_cases(20)
