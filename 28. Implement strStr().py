class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)):

            if needle[0] == haystack[i]:

                k = 0
                while k < len(needle) and i < len(haystack):

                    if haystack[i] == needle[k]:
                        i += 1
                        k += 1
                    else:
                        break

                if k == len(needle):
                    return i - k

        return -1


    def strStrOpt(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:
            return 0

        ans = haystack.find(needle)
        return ans

    def strStrOpt2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) +1):
            if needle == haystack[i:i + len(needle)]:
                return i
        return -1




sol = Solution()

haystack = "a"
needle = "a"

print sol.strStrOpt2(haystack, needle)