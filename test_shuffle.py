__author__ = 'szeitlin'

import unittest
from shuffle import shuffle_until, shuffle_recursive, make_deck, shuffle_iterative
from collections import deque

class TestShuffle(unittest.TestCase):

    def setUp(cls):
        cls.smalldeck = [1,2,3,4,5]

    def test_get_bottom_card_from_bottom(self):
        self.assertEqual(self.smalldeck[-1], 5)

    def test_bottom_card_from_top_portion(self):
        self.assertEqual(self.smalldeck[2], 3)

    def test_shuffle_once(self):
        self.assertEqual(([1,3,5,2,4],1),shuffle_until(5,3,1))
        self.assertEqual(([3,6,2,5,1,4],1), shuffle_until(6,3,1))

    def test_shuffle_twice(self):
        self.assertEqual(([1,5,4,3,2],2),shuffle_until(5,3,2))


class TestShuffleRecursive(unittest.TestCase):

    def setUp(cls):
        cls.smalldeck = [1,2,3,4,5]
        cls.ten = make_deck(10)
        cls.twenty = make_deck(20)
        cls.fifty = make_deck(50)
        cls.hundred = make_deck(100)
        cls.fivehundred = make_deck(500)
        cls.big = make_deck(1002)

    def test_stopping(self):
        self.assertEqual(self.smalldeck, list(deque(self.smalldeck)))

    def test_smalldeck(self):
        shuffle_count = 0
        self.assertEqual(4, shuffle_recursive(self.smalldeck, 3, shuffle_count))

    def test_ten(self):
        self.assertEqual(14, shuffle_recursive(self.ten, 3, 0))

    def test_half_of_ten(self):
        self.assertEqual(5, shuffle_recursive(self.ten, 5, 0))

    def test_tenth_of_ten(self):
        self.assertEqual(2, shuffle_recursive(self.ten, 1, 0))

    def test_twenty(self):
        self.assertEqual(6, shuffle_recursive(self.twenty, 10, 0))

    def test_fifty(self):
        self.assertEqual(86, shuffle_recursive(self.fifty, 15, 0))

    def test_hundred(self):
        self.assertEqual(198, shuffle_recursive(self.hundred, 11, 0))


class TestShuffleIterative(unittest.TestCase):

    def setUp(cls):
        cls.smalldeck = [1,2,3,4,5]
        cls.hundred = make_deck(100)
        cls.fivehundred = make_deck(500)
        cls.big = make_deck(1002)

    def test_smalldeck(self):
        shuffle_count = 0
        self.assertEqual(4, shuffle_iterative(self.smalldeck, 3, shuffle_count))

    def test_hundred(self):
        self.assertEqual(198, shuffle_iterative(self.hundred, 11, 0))

    def test_fivehundred(self):
        self.assertEqual(358, shuffle_iterative(self.fivehundred, 321, 0))

    @unittest.skip
    def test_fivehundred_one(self):
        """
        This case is many many iterations long
        :return:
        """
        self.assertEqual(1890, shuffle_iterative(self.fivehundred,101, 0))

    def test_fivehundred_two(self):
        self.assertEqual(1890, shuffle_iterative(self.fivehundred,102, 0))

    @unittest.skip
    def test_fivehundred_three(self):
        """
        This case is many many iterations long.
        :return:
        """
        self.assertEqual(2500, shuffle_iterative(self.fivehundred, 103, 0))

    def test_fivehundred_four(self):
        self.assertEqual(15006, shuffle_iterative(self.fivehundred, 104, 0))

    def test_fivehundred_five(self):
        self.assertEqual(626, shuffle_iterative(self.fivehundred, 105, 0))

    def test_big(self):
        self.assertEqual(91080, shuffle_iterative(self.big, 101, 0))


if __name__=='__main__':
    unittest.main()
