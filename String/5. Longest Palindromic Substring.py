class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Time limit exceeded ((
        # Base cases
        if not s:
            return ""

        if len(s) == 1:
            return s

        # Check if is palindrome
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        # Store indicies in list
        indicies = []
        max_lenght = 0

        # Brute force loop. Go through all possible combinations and check if it's a palindrome
        for i in range(0, len(s) - 1):
            for j in range(i + 1, len(s)):
                if isPalindrome(i , j):
                    # If yes, we get the indicies of maximum lenght
                    temp_lenght = max(max_lenght, j - i + 1)
                    if temp_lenght > max_lenght:
                        indicies = [i, j+1]
                        max_lenght = temp_lenght


        # If no indicies found, it means that no valid palindrome and we should return the first index.
        # Because 1 symbol is palindrome itself
        if indicies == []:
            return s[0]

        # Else return the part of string within max indicies
        else:
            return s[indicies[0]:indicies[1]]


# T - O(N^3).
# S - O(1). We store just 2 indices.


    # Optimal solution.
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Идем по строке, выбирая по очереди как бы середину, и смотря от нее влево и вправо, палиндром ли это
        # Но есть ньюанс, для нечетного палиндрома и для четного немного разные индексы нужно использовать, относительно центра.

        # Base case
        if not s:
            return ""

        # Range индексов для вывода палиндрома
        indicies_range = 0
        indexes = []


        # Для четного, например "cbbd", палиндром - bb
        for m in range(len(s)):
            l = m
            r = m + 1

            # Пока центр и его индексы слева и справа равны, это палиндром, продолжаем разводить индексы
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Фиксируем индексы пока палиндром
                if r - l > indicies_range:
                    indexes = [l, r]
                    indicies_range = r - l
                l -= 1
                r += 1


        # Для нечетого, например "cbabad", палиндром - aba
        for m in range(len(s)):
            l = m - 1
            r = m + 1

            # Пока центр и его индексы слева и справа равны, это палиндром, продолжаем разводить индексы
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Фиксируем индексы пока палиндром
                if r - l > indicies_range:
                    indexes = [l, r]
                    indicies_range = r - l
                l -= 1
                r += 1

        # Если индексов не нашлось, значит палиндрома нет, возвращаем первый индекс строки.
        if indexes == []:
            return s[0]
        else:
            return s[indexes[0]:indexes[1] + 1]

# T - O(N^2). Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).
# S - O(1). We store just 2 indices.



    # Manacher's Algorithm - O(N)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        S = ""
        for i in range(0, len(s)):
            S = S + "#" + s[i]
        S += "#"

        lenPalindrome = []
        c = 0
        r = 0
        for i in range(0, len(S)):
            if r > i:
                lenPalindrome.append(min(lenPalindrome[c * 2 - i], r - i))
            else:
                lenPalindrome.append(1)
            while i - lenPalindrome[i] >= 0 and i + lenPalindrome[i] < len(S) and S[i - lenPalindrome[i]] == S[i + lenPalindrome[i]]:
                lenPalindrome[i] += 1
            if i + lenPalindrome[i] > r:
                r = i + lenPalindrome[i]
                c = i

        c = lenPalindrome.index(max(lenPalindrome))
        ansString = ""
        for i in range(c - lenPalindrome[c] + 1, c + lenPalindrome[c]):
            if S[i] != "#":
                ansString += S[i]
        return ansString




s = "abcd"
sol = Solution()
print(sol.longestPalindrome2(s))