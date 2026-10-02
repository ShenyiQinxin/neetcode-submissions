class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_prof = 0
        for sell in prices[1:]:
            if sell > buy:
                max_prof = max(max_prof, sell - buy)
            else:
                buy = sell
        return max_prof



        