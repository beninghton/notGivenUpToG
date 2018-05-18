class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.strip(' ')
        if not s:
            return 0

        if s == ' ':
            return 0

        for i in range(len(s)):

            cnt = 0

            if s[i] == ' ':

                while s[i+1] != ' ':

                    cnt += 1
                    i += 1

                    if i == len(s)-1:
                        return cnt

        return i+1


    def lengthOfLastWordOpt(self, s):

        b = s.split()

        if b == []:
            return 0
        else:
            return len(b[-1])



sol = Solution()

print sol.lengthOfLastWordOpt("    ")




