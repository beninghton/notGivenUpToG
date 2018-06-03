class Solution(object):
    def detectCapitalUse(self, word):       # O(N), N - len(word), space - O(1)
        """
        :type word: str
        :rtype: bool
        """


        if word.upper() == word:
            return True
        elif word.lower() == word:
            return True
        else:
            if word[0].isupper() and len(word) > 1:
                for i in range(1,len(word)):
                    if word[i].isupper():
                        return False
            else:
                return False

            return True




sol = Solution()

a = "ffffffffffffffffffffF"

print (sol.detectCapitalUse(a))




