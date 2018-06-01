class Solution(object):

    def reverse(self, s):
        return s[::-1]

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        if k >= len(s):
            return s

        res = ""

        main = s[:k*k]



        for i in range(0,len(main),k):


            res += self.reverse(s[i:i+k])

        rest = s[k*k:]

        if len(rest) < k:
            res += rest[::-1]

        elif k <= len(rest) < 2*k:
            res += rest[:k][::-1]
            res += rest[k:]

        return res

    def reverseStrOpt(self, s, k):
        a = list(s)
        for i in xrange(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)









sol = Solution()

s = "ababababababababa"
k = 2

print sol.reverseStr(s,k)
print sol.reverseStrOpt(s,k)