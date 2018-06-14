# -*- coding: utf-8 -*-
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        cnt = 0
        tmp = S
        found = True

        for word in words:
            s = tmp
            for ch in word:
                if s.find(ch) == -1:
                    found = False
                    break
                else:
                    index = s.find(ch)
                    s = s[index + 1:]
                    found = True

            if found:
                cnt += 1

        return cnt

    def numMatchingSubseq_2(self, S, words):

        cnt = 0
        found = False

        for word in words:
            i = 0
            k = 0

            while i < len(word) and k < len(S):
                if word[i] == S[k]:

                    if i == len(word) - 1:
                        found = True

                    k += 1
                    i += 1
                else:
                    k += 1
                    found = False

            if found:
                cnt += 1

        return cnt

    def numMatchingSubseq_3(self, S, words):



sol = Solution()

S = "abcd"
words = ["da", "bd", "bc", "cd"]

print sol.numMatchingSubseq(S, words)
print sol.numMatchingSubseq_2(S, words)

'''
1. Brute-force. (Time limit exceeded). O(N*K*S).
N - кол-во слов в массиве
K - длина слова
S - длина исходной строки

'''

