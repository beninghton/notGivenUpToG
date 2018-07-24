class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Base cases

        if not s and not t:
            return True
        if not s or not t:
            return False
        if len(s) != len(t):
            return False

        # Dicts to store the results

        s_dict = dict()
        t_dict = dict()

        # Count numbers of appearances of the characters

        for ch in s:
            if ch in s_dict:
                s_dict[ch] += 1
            else:
                s_dict[ch] = 1

        for ch in t:
            if ch in t_dict:
                t_dict[ch] += 1
            else:
                t_dict[ch] = 1


        # Compare the results
        for key, val in t_dict.items():
            # If 1 key not exist in another dict, return False
            if s_dict.get(key, None):
                # Compare the values (counts)
                if s_dict[key] != t_dict[key]:
                    return False
            else:
                return False

        return True

### Complexity
        # O(N) - посчитать нужно каждый элемент, O(1) - количество элементов в словаре фиксировано - алфавит.

    # Решение немного оптимальнее. Использовать 1 словарь и складывать или вычитать значения. Если в конце у значения не 0 появлений - значит False.
    def isAnagram_opt(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import defaultdict

        d = defaultdict(int)

        for char in s:
            d[char]+=1

        for char in t:
            d[char]-=1

        for val in d.values():
            if val != 0:
                return False

        return True

        # Another solution - SORTING
        # Мы можем просто Отсортировать все элементы  и сравнить их.
    def isAnagram_2(self, s, t):
        # Base cases

        if not s and not t:
            return True
        if not s or not t:
            return False
        if len(s) != len(t):
            return False

        s = ''.join(sorted(s))
        t = ''.join(sorted(t))


        for i in range(len(s)):
            if s[i] != t[i]:
                return False

        return True


    ### Complexity
    # O(Nlogn) - сортировка, O(N) - сортируемая строка получается через лист, соответственно равный кол-ву символов в строке.

    # Просто считает количество символов из алфавита и смотрит, все ли они равны. O(N) кажется.
    def isAnagram_leetcode(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return all(s.count(i) == t.count(i) for i in string.ascii_lowercase)

s = "ac"
t = "ca"

sol = Solution()


print(sol.isAnagram_opt(s, t))
