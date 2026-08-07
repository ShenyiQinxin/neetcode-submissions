class Solution:
    # single most profitable transation
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0] # buy price

        # look for a max price as a sell price
        for sell in prices[1:]:
            if sell >= min_price:
                curr_profit = sell - min_price
                max_profit = max(max_profit, curr_profit)
            else:
                min_price = sell

        return max_profit


        