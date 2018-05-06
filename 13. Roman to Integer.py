class Solution(object):
    def romanToInt(self, s):


        romans = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}



        if not s:
            return None

        prev_value = 0
        res = 0

        for i in range(len(s)-1, -1, -1):
            if romans[s[i]] >= prev_value:
                res += romans[s[i]]
                prev_value = romans[s[i]]
            else:
                res -= romans[s[i]]
                prev_value = romans[s[i]]


        return res




sol = Solution()

#print (sol.longestCommonPrefix("pwwkew"))
#print (sol.longestCommonPrefix("bbbb"))
#print (sol.longestCommonPrefix("abcabcbb"))
print (sol.romanToInt("MCMXCIV"))