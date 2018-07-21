class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        if guess(1) == 0:
            return 1
        elif guess(n) == 0:
            return n

        left = 1
        right = n
        while True:
            m = (left + right)/2
            res = guess(m)
            if res == -1:
                right = m
            elif res == 1:
                left = m
            else:
                return m



# O(Log(n)), O(1)
# Classic binary search
# Divide by 2, if less then assign middle to the right side, if more then assign middle to thee left side
# + Base cases if 1 or n.