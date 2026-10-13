class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1
        max_total = 0

        while right < len(prices):

            if prices[right] > prices[left]:
                total = prices[right] - prices[left]
                max_total = max(total, max_total)


            else:
                left = right
            
            right += 1

        return max_total

        

        
        