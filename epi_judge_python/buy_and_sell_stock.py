from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price_so_far = float('inf')
    max_profit = 0

    for price in prices:
        max_profit_today = price - min_price_so_far
        min_price_so_far = min(price, min_price_so_far)
        max_profit = max(max_profit, max_profit_today)

    return max_profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
