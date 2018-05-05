import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        #x = str(x)
        #if x == x[::-1]:
        #    return True
        #else:
        #    return False

        res = 0
        tempX = x
        while tempX > 0:
            res = res * 10
            rest = tempX % 10
            res = res + rest
            tempX = tempX / 10
        if x == res:
            return True
        else:
            return False

sol = Solution()
print (sol.isPalindrome(12121))