class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """


        #Base cases
        if not pattern or not str:
            return False

        # Convert str to the list
        str = str.split()

        # Then compare the lenghts, if not equal return False
        if len(pattern) != len(str):
            return False

        # Map to compare matches words to the pattern. Key - pattern, word - value
        patternmap = dict()
        patternset = set()

        for i in range(len(str)):
            # IF not in dict, then add
            if pattern[i] not in patternmap:
                # If value is not in set. Because if it is - it means that it was registered with another key-pattern. Return False
                if str[i] not in patternset:
                    patternmap[pattern[i]] = str[i]
                    patternset.add(str[i])
                else:
                    return False

            else:
                # Compare words. Should be the same
                if patternmap[pattern[i]] != str[i]:
                    return False

        return True


# T - O(N), N - count letters in the pattern. (if count words and count letters are not equal we even don't go into the loop)
# S - O(N + M) - store results in dict and map, N - count letters in the pattern, M - count words in str.

sol = Solution()
print(sol.wordPattern("abba", "dog dog dog dog"))