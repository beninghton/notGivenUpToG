class Solution(object):
    def compr(self,s):

        i = 0
        res = ""

        while i < len(s):
            i +=1
            cnt = 1

            while i <len(s) and s[i] == s[i-1]:
                cnt += 1
                i += 1

            res += str(cnt) + s[i-1]

        return res


    def intToStr(self, n):

        res = ""

        isNegative = False
        if n < 0:
            isNegative = True

        if n == 0:
            return str(n)

        while n != 0:
            remainer = abs(n) % 10
            n = abs(n) / 10
            res += str(remainer)

        if isNegative:
            res+= "-"
        res = res[::-1]
        return res



sol = Solution()



print sol.compr("abbb")
#print sol.intToStr(0)