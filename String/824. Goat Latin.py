class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """


        vowels = set("aeiuo")

        list_s = S.split()

        for i, el in enumerate(list_s):

            if el[0].lower() in vowels:
                list_s[i] = el + "ma" + "a"*(i+1)
            else:
                list_s[i] = el[1:] + el[0] + "ma" + "a"*(i+1)

        return ' '.join(list_s)



sol = Solution()

paragraph = "I speak Goat Latin"



print sol.toGoatLatin(paragraph)

# O(N^2) where N is the length of S. This represents the complexity of rotating the word and adding extra "a" characters.
# Space O(N^2) the space added to the answer by adding extra "a" characters.