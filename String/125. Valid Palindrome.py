# -*- coding: utf-8 -*-

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        l = [x.lower() for x in s if x.isalnum()]

        s1 = ''.join(l)

        # Reversing implementation
        left = 0
        right = len(l) - 1
        r = l[:]

        while left < right:
            r[left], r[right] = r[right], r[left]
            left += 1
            right -= 1


        return r == l



sol = Solution()

s= "race a car"
print (sol.isPalindrome(s))



# O(N), N - кол-во символов в строке. O(N) - space complexity
# Решение: если альфанумерик - добавляем в лист и уменьшаем, дальше сравниваем с реверсной строкой