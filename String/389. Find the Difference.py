# -*- coding: utf-8 -*-

import collections

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        # Base cases
        if not s and not t:
            return None
        if len(s) > len(t):
            return None
        if not s and t:
            return t

        # Define dicts, that will count number of symbols
        s_dict = dict()
        t_dict = dict()

        # Iterate and get symbols count for s
        for ch in s:
            if ch in s_dict:
                s_dict[ch] += 1
            else:
                s_dict[ch] = 1

        # Iterate and get symbols count for s
        for ch in t:
            if ch in t_dict:
                t_dict[ch] += 1
            else:
                t_dict[ch] = 1

        # Compare symbols count, iterate through t_dict
        for key, val in t_dict.items():
            # If key from S is in T, we need to compare counts. If not - None is returned from "get" and this "if" statement will not work
            if s_dict.get(key, None):
                # If the values of counts are not equal, it means that this symbol was added. Return it.
                if s_dict[key] != t_dict[key]:
                    return key
            # Key was not found, it means that it's unique and it was added. Return it.
            else:
                return key

    # Solution for leetcode. O(N^2), O(1). Brute-force.
    def findTheDifference_Leetcode(self, s, t):
        for i in t:
            if t.count(i) != s.count(i):
                return i

    # O(N). Самое интересное решение. Если делать XOR(^) между двумя одинаковыми числами(представляющими одну и ту же букву), то будет 0.
    # В итоге останется число той самой буквы, которая лишняя. Например "ab" и "cba". Получается: 97 ^ 98 и 99 ^ 98 ^ 97.
    # От перемены мест множетелей как бы сумма не меняется. Выходит 97 ^ 97 ^ 98 ^ 98 ^ 99 = 99 == "c"
    def findTheDifference_Leetcode2(self, s, t):
        res = 0
        for char in s+t:
            res ^= ord(char)
        return chr(res)

    # Вычитаем counter, в результате получаем Counter объект. Преобразуем в лист и возвращаем ключ. List - возвращает ключи из Counter.
    def findTheDifference_Leetcode3(self, s, t):
        return list((collections.Counter(t) - collections.Counter(s)))[0]

s = "abcde"
t = "пabcde"
sol = Solution()

print(sol.findTheDifference_Leetcode3(s, t))

# O(N), O(1). Фиксированные словари. N - количество символов в любой строке. Строки раз. всего на 1 символ.
