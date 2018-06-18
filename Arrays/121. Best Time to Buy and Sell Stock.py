class Solution:
    def maxProfit(self, prices):                        # O(N*2), O(1)
        """
        :type prices: List[int]
        :rtype: int
        """

        if prices == [] or len(prices) == 1:
            return 0


        max_diff = 0

        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > max_diff:
                    max_diff = prices[j] - prices[i]


        return max_diff


    def maxProfit_2(self, prices):              # O(N), O(1)
        """
        :type prices: List[int]
        :rtype: int
        """

        if prices == [] or len(prices) == 1:
            return 0

        min_price = max(prices)
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit
sol = Solution()




print sol.maxProfit_2([2,1,2,0,1])

# Идем по массиву, фиксируем профит. Если след - минимальный, то мин равен ему. Иначе - смотрим профит(разн между текущим эл-ом и текущим минимумом)