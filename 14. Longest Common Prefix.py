class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        prefix = strs[0]

        for word in strs:

            while word.find(prefix) != 0:
                prefix = prefix[0:len(prefix)-1]
                if not prefix:
                    return ""

        return prefix







sol = Solution()

print (sol.longestCommonPrefix(["flow","flight","flower"]))
#print (sol.longestCommonPrefix(["racecar","car"]))
#print (sol.longestCommonPrefix("abcabcbb"))
#print (sol.longestCommonPrefix("dvdf"))