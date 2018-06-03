# -*- coding: utf-8 -*-

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowel_list = set(list("aeiouAEIOU"))

        left = 0
        right = len(s) - 1
        l = list(s)

        while left < right:

            if l[left] in vowel_list:
                if l[right] in vowel_list:
                    l[right], l[left] = l[left], l[right]
                    left += 1
                    right -=1
                else:
                    right -=1
            else:
                left +=1




        return ''.join(l)




sol = Solution()

a = "hello"

print (sol.reverseVowels(a))

# Сложность O(N), N - кол-во символов в строке. Space так же O(N)
# Алгоритм: начинаем идти слева, когда доходим до гласной, начинаем смотреть правый индекс. Если он еще не гласная -
# начинаем уменьшать справа. Когда оба гласные - меняем.


