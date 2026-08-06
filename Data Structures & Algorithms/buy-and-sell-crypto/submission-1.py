class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 1
        buy = 0
        max_profit = 0
        while sell < len(prices):
            max_profit = max(max_profit, prices[sell] - prices[buy])
            if prices[sell] < prices[buy]:
                buy = sell #
            sell += 1
        return max_profit
