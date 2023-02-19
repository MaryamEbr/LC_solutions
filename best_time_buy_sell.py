# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/

class Solution(object):

    # wrong
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # O(nlogn)
        prices_sorted = sorted(prices)

        left = 0
        right = len(prices)-1

        while left < right:
            buy = prices_sorted[left]
            sell = prices_sorted[right]

            if prices.index(buy) < prices.index(sell):
                return sell-buy

            else:
                if sell-prices_sorted[right-1] < prices_sorted[left+1]-buy:
                    right -= 1
                else:
                    left += 1

        return 0

    # brute force O(n^2), correct but time limit exceed
    def maxProfit2(self, prices):

        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]

        return max_profit

    
    # basicaly brute force but a little better
    # still time limit exceed
    def maxProfit3(self, prices):

        min_price = 10000
        max_profit = 0

        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price = prices[i]
                # find max profit for this min price
                for j in range(i+1, len(prices)):
                    if prices[j]-min_price > max_profit:
                        max_profit = prices[j]-min_price
        return max_profit


    # third attempt, from solution, this wasn't easy for me
    # I didn't came up with this myself
    def maxProfit(self, prices):

        min_price = 100000
        max_profit = 0


        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price = prices[i]
            elif prices[i]-min_price>max_profit:
                max_profit = prices[i]-min_price
        return max_profit



sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))