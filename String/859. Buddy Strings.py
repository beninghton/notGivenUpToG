# -*- coding: utf-8 -*-

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        list_A = list(A)

        for i in range(len(A) - 1):

            for k in range(i + 1, len(A)):
                list_A[i], list_A[k] = list_A[k], list_A[i]
                if ''.join(list_A) == B:
                    return True
                else:
                    list_A[i], list_A[k] = list_A[k], list_A[i]

        return False


    def buddyStrings_opt(self, A, B):

        # Different lenghts, base case
        if len(A) != len(B):
            return False

        # Define vars
        res = False
        count = 0
        i = 0

        while i < len(A):
            # First time elements does not equal
            if A[i] != B[i] and count == 0:
                # Rememeber differ element, increment count
                differ_A = A[i]
                differ_B = B[i]
                count += 1

            # It happened second time or more
            elif A[i] != B[i]:
                # If second, then fine. Check if this happens only second time and the element is the needed. Который равен как раз тому, если мы свапнем.
                if B[i] == differ_A and A[i] == differ_B and count == 1:
                    res = True
                    count += 1

                # If more, or element is another, it means that string is different and we can not just swap 2 elements
                else:
                    return False

            # Increment count always
            i += 1

        # Если цикл прошел без проблем, и false не вылетело. Значит строки одинаковые!!!. Но они могут состоять из одного символа, или типа "abab" меняя которые ничего не изменится. Надо вернуть True
        # НО! если строка "abcd" и "abcd" то меняя будет False.
        # Нам надо проверить, есть ли в строке символы, количество которых больше единицы, если да - значит можно вернуть True. Если нет - False.
        # Поможет нам в этом Counter. !! ИЛИ можно использовать для этого SET

        from collections import Counter
        counter = Counter(A)

        # Если цикл прошел гладко и все строки совпали. Например "ab" и "ab" - одинаковы, замен не было. Но если их поменять - будет херня.
        if count == 0:
            for el in counter:
                if counter[el] > 1:
                    return True

        # Если символы были заменены, то возвращаем результат.
        return res

# O(N), O(N)


# Leetcode solution

    def buddyStrings_leetcode(self, A, B):
        if len(A) != len(B): return False

        # Сначала обрабатываем case, где строки изначально равны. Смотрим, есть ли повторяющиеся символы среди них. Если да - значит их можно поменять, значит return True.
        if A == B:
            if len(set(A)) < len(A):
                return True
            else:
                return False
        else:
            # Далее если строки не равны. Добавляем в лист неравные пары значений. ZIP - маппит букву из A к букве из B.
            pairs = []
            for a, b in zip(A, B):
                if a != b:
                    pairs.append((a, b))
                # Если этих пар больше 2, значит строки слишком разные.
                if len(pairs) >= 3:
                    return False
                # Если нет, смотрим что их две (иначе если одна, то менять не на что, и у нас одно различие). И, так же, смотрим, равны ли пары если их перевернуть. Если равны - значит они одинаковы, гуд!
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]


#Complexity Analysis
#Time Complexity: O(N), where NN is the length of A and B.
#Space Complexity: O(1).

sol = Solution()

A = "ab"
B = "ca"
print(sol.buddyStrings_leetcode(A, B))


# Brute-Force, go and change every letter
# O(N^3), N - кол-во символов в строке. O(N) - space complexity
