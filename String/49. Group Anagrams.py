# -*- coding: utf-8 -*-

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # Time limit exceeded (((
        def isAnagram(a, b):
            d = defaultdict(int)

            for ch in a:
                d[ch] += 1
            for ch in b:
                d[ch] -= 1

            for val in d.values():
                if val != 0:
                    return False

            return True


        res_dict = defaultdict(list)
        res_list = []

        while strs:
            example = strs[0]
            temp = set()

            for i in range(0, len(strs)):
                if isAnagram(example, strs[i]):
                    res_dict[example].append(strs[i])
                    temp.add(strs[i])

            strs = [word for word in strs if word not in temp]


        for val in res_dict.values():
            res_list.append(val)

        return res_list

# Сложность пиздец. Анаграмма - O(N). А главная функция - O(N), итого O(N^2).
# Space - O(N)



    def groupAnagrams_leetcode(self, strs):
        ans = defaultdict(list)
        res_list = []

        # Очень простое решение. Сортируем каждое слово и делаем его ключем в словаре как tuple (состоящий из сортированных букв в этом слове).
        # Соответственно если слово - анаграмма, то его сортированные тьюплы будут совпадать. И мы будем добавлять туда куда надо.
        for s in strs:
            ans[tuple(sorted(s))].append(s)


        for val in ans.values():
            res_list.append(val)

        return res_list

# Time complexity - O(N*K*logK).  where N is the length of strs, and K is the maximum length of a string in strs.
# The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(K*logK) time.
# Space Complexity: O(N*K), the total information content stored in ans.
# N - ключи, K - значения



# https://leetcode.com/problems/group-anagrams/solution/ номер 2
    # По простому - кодируем строку из алфавит символов в лист с их количеством появлений.
    # Например, aabc становится [2,1,1,0,0,0,....] и т.д.
    def groupAnagrams_leetcode2(self, strs):
        ans = defaultdict(list)
        res_list = []

        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch) - ord('a')] += 1

            ans[tuple(count)].append(word)



        for val in ans.values():
            res_list.append(val)

        return res_list


#Complexity Analysis

# Time Complexity: O(N*K), where N is the length of strs, and K is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.
# Space Complexity: O(N*K), the total information content stored in ans.
# Пишут что K - максимальная(!) длина строки в strs. Не средняя, и не сумма.



input = ["",""]
sol = Solution()
print(sol.groupAnagrams_leetcode2(input))
