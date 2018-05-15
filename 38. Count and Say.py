class Solution(object):
    def countAndSay(self, n):
        s = "1"
        i = 0
        if n == "1":
            return n


        while i < int(n) - 1:
            count = 1
            res = ""

            for i in range(len(s) -1):
                if s[i] == s[i+1]:
                    count += 1
                else:
                    res += str(count) + s[i]
                    count = 1

            s = res
            i += 1

            res += str(count) + s[i]
        return res









sol = Solution()



print sol.countAndSay("2")
