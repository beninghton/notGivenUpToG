class Solution(object):
    def climbStairs(self, n):
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def climbRec(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        return self.climbRec(i + 1, n) + self.climbRec(i + 2, n)

    def climbStairsRec(self,n):
        return self.climbRec(0,n)



sol = Solution()


print (sol.climbStairsRec(3))
