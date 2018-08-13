from collections import defaultdict
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """

        # Base Case
        if not S or not T:
            return S or T

        t = list(T)
        s_dict = dict()

        # Определяем индексы используемых элементов, это те что есть в строке S
        for i, x in enumerate(S):
            s_dict[x] = i

        # Лист для неисп и используемых символов
        unused = []
        used = []

        # Распределяем символы
        for ch in t:
            if ch in s_dict:
                used.append(ch)
            else:
                unused.append(ch)

        # Поехали менять. Если индекс предыдущего символа больше чем индекс текущего - меняем их, меняем пока локальный индекс x > 0.
        i = 1

        while i < len(used):
            x = i
            while x > 0 and s_dict[used[x]] < s_dict[used[x - 1]]:
                used[x], used[x - 1] = used[x - 1], used[x]
                x -= 1

            # После того как поменяли элемент до конца, переходим на след элемент (переставляем i) и снова сравниваем.
            i = x + 1

        return ''.join(used) + ''.join(unused)

# T - O(N^2) - в худшем случае. Когда у нас нужная строка полностью противоположна исходному алфавиту, и все буквы в алфавите присутствуют.
#  Нужно все символы переставлять. N - кол-во символов в t.
# S - O(N + M) = O(N), N - кол-во символов в t. Т.к. в S - фиксированный алфавит или менее.



    # Решение наоборот. Формируем сначала лист из тех что в S затем добавляем те которых нет в S.
    # O(N), O(N)
    def customSortString2(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        l = []
        for i in S: # O(1) - фикс. количество
            l.append(i*T.count(i)) # O(N*S), но т.к. S - фикс. количество, то можно сказать O(N)
        for i in T:
            if i not in S: # Можно считать O(1), т.к. 26 букв
                l.append(i)
        return ''.join(l)


    # T - O(N), N - длина T.
    # S - O(N) - рез-й лист.
    def customSortString3(self, S, T):

        ans = []
        letterCount = defaultdict(int)
        #  Считаем count каждого символа
        for c in T:
            letterCount[c] += 1

        for c in S:
            # Если его нет в T, идем дальше.
            if c not in letterCount:
                continue
            # Идем по символам и аппендим количество из T.
            for i in range(letterCount[c]):
                ans.append(c)
            # Удаляем ключ в конце
            del letterCount[c]

        # deal with the leftover letters
        for c in letterCount:
            # Дальше добавляем все те кто остался в словаре ( те что есть уже удалили)
            for i in range(letterCount[c]):
                ans.append(c)

        return ''.join(ans)

sol = Solution()
print(sol.customSortString("abcdre", "gcaasdfsfsd"))


