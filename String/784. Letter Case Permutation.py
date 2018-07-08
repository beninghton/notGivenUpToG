# -*- coding: utf-8 -*-

import string

class Solution:
    def letterCasePermutation_best(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        res = [""]
        for c in S:
            if c.isdigit():
                for i in range(len(res)):
                    res[i] += c
            else:
                copy = res.copy()
                for i in range(len(res)):
                    res[i] += c.lower()
                for i in range(len(copy)):
                    copy[i] += c.upper()
                res.extend(copy)

        return res


    def letterCasePermutation_dfs(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = []

        def dfs(S, pos, str):
            if pos == len(S):
                ans.append(str)
                return
            else:
                if S[pos].isalpha():
                    letter = S[pos]
                    dfs(S, pos + 1, str + letter.upper())
                    dfs(S, pos + 1, str + letter.lower())
                else:
                    dfs(S, pos + 1, str + S[pos])
        dfs(S, 0, '')
        return ans

sol = Solution()

#S = "a1b2ab"
S = "aaa"

print(sol.letterCasePermutation_best(S))

# 1. Best. O(2^N) - а может и нет, сложно понять, O(2^N). Добавляем в один массив только маленькие, в другой только большие, потом обьединяем в один
# 2. O(2^N),  O(2^N) - dfs, добавляем в лист только листья дерева.