# -*- coding: utf-8 -*-

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True

        for i in range(len(s)):
            temp = s[:i] + s[i+1:]
            if temp == temp[::-1]:
                return True

        return False


    def validPalindrome_2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True

        le = 0
        ri = len(s) -1

        while le < ri:
            if s[le] == s[ri]:
                le +=1
                ri -= 1
            else:
                break

        t_le = s[:le] + s[le+1:]
        t_ri = s[:ri] + s[ri+1:]

        if t_le == t_le[::-1] or t_ri == t_ri[::-1]:
            return True
        else:
            return False

sol = Solution()

print(sol.validPalindrome_2("abca"))


### 1
#Time Complexity: O(N^2)
#where N is the length of the string. We do the following N times: create a string of length N and iterate over it.
#Space Complexity: O(N), the space used by our candidate answer.

### 2
# Оптимальное решение. O(N), O(N). Проходим строку 1 раз с двух концов. Т.к. у нас можно удалить лишь один элемент, как только мы находим несоответствие правого-левому,
#  мы фиксируем оба индекса и смотрим что будет если удалить один из них. Если это не приводит к успеху, значит палиндром мы сделать не сможем. Если успех - возвращаем тру.