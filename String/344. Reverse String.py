class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        left = 0
        right = len(s) - 1
        l = list(s)

        for i in range(len(s)/2):
            l[left], l[right] = l[right], l[left]

            left += 1
            right -= 1

        return ''.join(l)




sol = Solution()

a = "Hello"

print (sol.reverseString(a))




