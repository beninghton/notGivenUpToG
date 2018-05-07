class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}

        if not s:
            return True

        if s[0] in dict or len(s) % 2 != 0:
            return False
        else:
            stack.append(s[0])

        for i in range(1, len(s)):
            if s[i] in dict and dict[s[i]] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])

        return stack == []







sol = Solution()

#print (sol.longestCommonPrefix("pwwkew"))
#print (sol.longestCommonPrefix("bbbb"))
#print (sol.longestCommonPrefix("abcabcbb"))
print (sol.isValid("()"))