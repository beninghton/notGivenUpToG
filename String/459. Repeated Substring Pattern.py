class Solution(object):
    def repeatedSubstringPattern(self, s):          # O(N*N)
        """
        :type s: str
        :rtype: bool
        """

        for i in range(0,len(s)/2):
            if s[:i+1]*(len(s)/len(s[:i+1])) == s:
                return True

        return False



sol = Solution()

s = "aba"
print (sol.repeatedSubstringPattern(s))

