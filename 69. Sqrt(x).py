class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        i = 1

        while i <= x / 2:

            if i * i > x:
                return i-1
            elif i * i == x:
                return i

            i += 1

    def mySqrtTimeLimit(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 1:
            return 1

        i = 0

        while i <= x / 2:

            if i * i > x:
                return i-1
            elif i * i == x:
                return i

            i += 1
        return i-1


sol = Solution()


print (sol.mySqrt(11))
