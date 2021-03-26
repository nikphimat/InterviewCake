'''
Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.
No "shorting"—you need to buy before you can sell. Also, you can't buy and sell in the same time step—at least 1 minute has to pass.
'''
def get_max_profit(stock_prices):
    #stock_prices = [9, 9, 7, 4, 1]
    mn = stock_prices[0]
    ln = len(stock_prices)
    profits = []
    max_profit = 0
    for i in range(1,ln):
        new_profit = stock_prices[i] - mn
        #print(new_profit,max_profit)
        #print(mn, stock_prices[i])
        if max_profit == 0:
            max_profit = new_profit ## account for -ve profits
        mn = min(stock_prices[i], mn)
        max_profit = max(new_profit,max_profit)
        #print(new_profit,max_profit)
    if ln == 1:
        raise Exception ##just one stock price 
    else:
        return max_profit
        #print(max_profit)
     
	#return max_profit
    #max_index = i if stock_prices[i] == mx else 0
    #print(max_index)

















# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_big_increase_then_small_increase(self):
        actual = get_max_profit([2, 10, 1, 4])
        expected = 8
        self.assertEqual(actual, expected)                

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)
