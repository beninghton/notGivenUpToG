class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Идем по массиву слева, прибавляем к максимальной сумме только если след индекс больше предыдущего.
        # таким образом получим в итоге максимальную прибыль.
        # Какая то элементарщина. Не смог решить сам.

        res = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]

        return res


#Time complexity : O(n). Single pass.

#Space complexity: O(1). Constant space needed.







sol = Solution()




print(sol.maxProfit([2,1,2,1,1]))



