class Solution(object):
    def intToRoman(self, num):


        #romans = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}
        romans = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}



        if not num:
            return None

        res = ""

        l = []
        s = str(num)


        for i in range(0, len(s)):
            x = int(s[i] + (len(s)-i-1)*"0")

            if x in romans:
                res += romans[x]
                continue

            if x < 10:
                base = 1
                half = base * 5
            elif 10 < x < 100:
                base = 10
                half = base * 5
            elif 100 < x < 1000:
                base = 100
                half = base * 5
            else:
                base = 1000
                half = base * 5

            if x == base * 9:
                res += romans[base] + romans[10 * base]

            if base * 5 < x <= base * 8:
                res += romans[half] + romans[base] * (int(str(x)[0]) - 5)

            if x == base * 4:
                res += romans[base] + romans[half]

            if x <= base * 3:
                res += romans[base] * int(str(x)[0])



        return res




sol = Solution()

#print (sol.longestCommonPrefix("pwwkew"))
#print (sol.longestCommonPrefix("bbbb"))
#print (sol.longestCommonPrefix("abcabcbb"))
#print (sol.romanToInt("MCMXCIV"))
print (sol.intToRoman(2000))