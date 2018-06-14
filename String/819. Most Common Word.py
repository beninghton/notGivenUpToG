class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import string

        punct_set = set(string.punctuation)
        banned = set(banned)

        paragraph = ''.join(ch for ch in paragraph if ch not in punct_set)

        list_p = paragraph.lower().split()


        d = {}

        for el in list_p:
            if el in d:
                d[el] += 1
            else:
                if el not in banned:
                    d[el] = 1

        max_val = max(d.values())

        for key in d.keys():
            if d[key] == max_val:
                return key



sol = Solution()

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

#print sol.checkRecord(s1)
print sol.mostCommonWord(paragraph, banned)

# Time O(P+B), where P is the size of paragraph and B is the size of banned.
# Space  O(P+B), to store the count and the banned set.