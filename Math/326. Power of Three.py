class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #Base case

        if n < 1 or n % 3 != 0:
            return False

        while n >= 3 and n % 3 == 0:
            if n == 3:
                return True
            n = n // 3

        return False


# T - O(Log(n)) - потому что каждый раз результат уменьшается на 3
# S - O(1). Не храним ничего кроме переменных

sol = Solution()



print(sol.isUgly(0))
