class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split()
        return len(l)

    def countSegments_in_place(self, s):  # in_place solution O(1) space complexity

        cnt = 0

        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':       # (if string begins or if the previous is ' ') AND it's not a SPACE
                cnt += 1

        return cnt




sol = Solution()

s = "I hate(love) my job I want to work at Google"
print (sol.countSegments_in_place(s))

