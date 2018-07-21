class Solution:
    # @return a boolean
    def isValid(self, s):

        # Используем стек. И создаем словарь, где закрывающиеся скобки будут ключем, а открывающиеся - значением.
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}

        # Base case
        if not s:
            return True

        # Base Case. Если строка начинается с открытых скобок или число скобок нечетное - сразу False. Иначе добавляем в стек 1-й элемент.
        if s[0] in dict or len(s) % 2 != 0:
            return False
        else:
            stack.append(s[0])

        # Далее идем по строке, начиная с первого индекса (второго эл-та)
        for i in range(1, len(s)):

            # Если элемент в словаре, а это значит что приходит закрывающаяся скобка, и надо далее проверить равна ли она предудыщему эл-ту стека.
            # То есть равна ли она открывающейся, если нет - то будем продолжать добавлять в стек, и он в итоге окажется не пустой.
            if s[i] in dict and dict[s[i]] == stack[-1]:
                stack.pop()
            # Ну или если закрывающаяся скобка еще не пришла, продолжаем добавлять в стек открывающиеся.
            else:
                stack.append(s[i])

        # Если в стеке что то осталось, значит False.
        return stack == []


# В худшем случае O(N), т.к проходим всю строку 1 раз.
# Space O(N), для листа. Хотя вообще N/2, но в таком случае N.




sol = Solution()

#print (sol.longestCommonPrefix("pwwkew"))
#print (sol.longestCommonPrefix("bbbb"))
#print (sol.longestCommonPrefix("abcabcbb"))
print (sol.isValid("()"))