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
        raise Exception ##case: just one stock price 
    else:
        return max_profit
        #print(max_profit)
     

