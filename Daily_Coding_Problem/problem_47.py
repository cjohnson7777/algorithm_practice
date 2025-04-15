# [EASY] Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.


def stock_prices(prices):
    maxProfit = 0
    l = 0
    r = l + 1

    while r < len(prices):
        if prices[r] < prices[l]:
            l = r
            r += 1
        else:
            profit = prices[r] - prices[l]
            maxProfit = max(profit, maxProfit)
            r += 1

    return maxProfit

prices = [9, 11, 8, 5, 7, 10]
print(stock_prices(prices))