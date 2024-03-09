class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        pos1 = 0
        pos2 = 0
        current_min = prices[pos1]
        current_max = prices[pos2]
        while pos2 < len(prices):
            if prices[pos2] < current_min:
                current_min = prices[pos2]
                current_max = prices[pos2]
                pos1 = pos2
            elif prices[pos2] > current_max:
                current_max = prices[pos2]
            max_profit = max(max_profit, current_max - current_min)
            pos2 += 1
        return max_profit