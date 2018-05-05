class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        minus = False
        x = str(x)
        if x.startswith("-"):
            minus = True
            x = x[:0:-1]
        else:
            x = x[::-1]
        if int(x) > (2 ** 31):
            return 0
        return int("-" + x) if minus else int(x)

    def reverseOpt(self, x):
        """
        :type x: int
        :rtype: int
        """
        st = str(abs(x))
        st = st[::-1]
        if x > 0:
            x = int(st)
        else:
            x = -int(st)

        if abs(x) > 2**31:
            return 0
        else:
            return x


sol = Solution()
import time

start_time = time.time() * 100
print(sol.reverse(153423646))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time() * 100
print(sol.reverseOpt(153423646))
print("--- %s seconds ---" % (time.time() - start_time))