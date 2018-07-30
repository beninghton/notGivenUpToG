# -*- coding: utf-8 -*-

from collections import defaultdict

class Solution(object):

    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        # Идем через 2 индекса, стартовый и конечный.
        st, end, res = 0, 1, 0


        # Пока конечный индекс не достиг длины
        while end < len(s):
            # Смотрим есть ли символ от конечного индекса в предыдущей строке
            # Если есть, тогда фиксируем res - как максимум длины строки до end.
            # И дальше двигаем старт, пока символ [end] не перестанет быть в старте
            # Рез уже не меняется т.к. максимум был зафиксирован в первом "непопадании"
            if s[end] in s[st:end]:
                res = max(res, len(s[st:end]))
                # Двигаем старт по одному, пока символ перестанет попадать в range.
                st += 1
            # Если символа нет, просто двигаем end.
            else:
                end += 1

        return max(res, len(s[st:end]))

# O(N*N), проходим каждый символ, и строим дальше строку до этого символа. В худшем случае когда все символы разные - сложность N^2.
# Complexity N(^2) так же, т.к. строим новую строку все время.


    # Мое старое решение
    def lengthOfLongestSubstring2(self, s):
        if not s:
            return 0

        start = maxLength = 0
        # Определяем словарь. Ключи - буквы, значения - позиция в слове.
        usedChar = dict()

        # Идем по строке.
        for i in range(len(s)):
            # Если элемент в словаре И стартовый индекс меньше позиции элемента в словаре
            if s[i] in usedChar and start <= usedChar[s[i]]:
                # Старт позицию двигаем сразу на следующую после повторяющегося элемента.
                start = usedChar[s[i]] + 1
            else:
                # Иначе макс длина равна максимальной длине позиции минус старт-позицию
                maxLength = max(maxLength, i - start + 1)

            # Добавляем в словарь позицию буквы в строке
            usedChar[s[i]] = i

        return maxLength

# T - O(N), проходим строку один раз
# S - O(1), по сути, в словаре не может оказаться больше символов чем букв в алфавите(26 больших + 26 маленьких)
# Хотя leetcode говорит, что SPACE равен не O(1), a O(min(n, m):
#Space complexity :  O(min(n, m) = O(K).
# We need O(K) space for checking a substring has no duplicate characters, where K is the size of the Dict.
# The size of the Dict is upper bounded by the size of the string n and the size of the charset/alphabet m.
# То есть, если в строке представлены все символы алфавита то O(m) а если не все, тогда O(n), где n - все равно уникальные символы.




input = "ababccd"
sol = Solution()
print(sol.lengthOfLongestSubstring2(input))
