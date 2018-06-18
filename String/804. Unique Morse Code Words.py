class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        import string

        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alph = list(string.ascii_lowercase)
        morse_map = dict(zip(alph, morse))

        res_set = set()

        for word in words:
            tmp_list = []
            for ch in word:
                tmp_list.append(morse_map[ch])

            res_set.add(''.join(tmp_list))

        return len(res_set)


    def uniqueMorseRepresentations_leetcode(self, words):
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(seen)

    def uniqueMorseRepresentations_2(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        A_Z=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result=set()
        for word in words:
            tem=""
            for char in word:
                tem+=A_Z[ord(char)-ord('a')]
            result.add(tem)
        return len(result)

sol = Solution()

words = ["rwjje","aittjje","auyyn","lqtktn","lmjwn"]


print(sol.uniqueMorseRepresentations(words))

### 1. O(N*K), O(N*K), N word count, K - character count in each word. Или O(S) как ниже.
# Сначала делаем маппинг morse = alph, дальше по нему вычисляем

### 2. Решение аналогичное, но без маппинга. Т.к. лист отсортирован, мы прост оберем элемент по индексу, отнимая из кода текущей буквы код буквы 'a'.
#Time Complexity: O(S), where S is the sum of the lengths of words in words. We iterate through each character of each word in words.
#Space Complexity: O(S).