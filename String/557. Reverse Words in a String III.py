class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        l = s.strip().split()

        for i in range(len(l)):
            l[i] = l[i][::-1]

        return ' '.join(l)



sol = Solution()



# O(N), O(N)
#