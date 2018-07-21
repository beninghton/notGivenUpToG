# -*- coding: utf-8 -*-

from itertools import zip_longest

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        # Инициализируем переменные для результата
        res_S, res_T, carry = [], [], 0

        # Идем по первой строке в обратном направлении.
        for i in range(len(S) -1, -1, -1):
            # Если символ удаления - увеличиваем счетчик удаления.
            if S[i] == '#':
                carry += 1
            # Иначе - если обычный символ.
            else:
                # Если счетчик удалений еще остался, уменьшаем его. Соответственно пропускаем символ.
                if carry > 0:
                    carry -= 1
                # Иначе - символ не надо пропускать, и добавляем его в результирующий список.
                else:
                    res_S.append(S[i])

        # Делаем тоже самое для второй строки.
        carry = 0
        for i in range(len(T) - 1, -1, -1):

            if T[i] == '#':
                carry += 1

            else:
                if carry > 0:
                    carry -= 1
                else:
                    res_T.append(T[i])

        # Превращаем результ. списки обратно в строки и сравниваем.
        res_s = ''.join(res_S)
        res_t = ''.join(res_T)
        return res_s == res_t


    # Для O(1).
    def backspaceCompare_leetCode(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        # Т.к. yield - дополнительную память мы не используем.
        # Применяем функцию zip_longest по очереди к каждому элементу, смысл тот же что и выше. Затем смотрим есть ли в списке какой нибудь false, через функцию all.
        return all([x == y for x, y in zip_longest(F(S), F(T))])



# 1. O(T + S), O(T + S)
# 2. O(T + S), O(1). Засчет yield - память не используем.

S = "abaaa##"
T = "abaaa#"

sol = Solution()

print(sol.backspaceCompare_leetCode(S, T))



