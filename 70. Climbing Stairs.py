class Solution(object):

    def climbStairs_rec(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Classic solution, O(2^N), Space complexity : O(n). The depth of the recursion tree can go up to nn.
        # Шагаем либо по две либо по одной (спускаемся сверху). Результат складываем.
        if n < 0:
            return 0
        elif n == 0:
            return 1

        return self.climbStairs(n-1) + self.climbStairs(n-2)


    # Функция - caller, в ней инициализируется словарь, который она передает
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # В словаре будем хранить значения путей до определенных ступеней
        prev = dict()

        return self.climbStairs_memo(n, prev)


    def climbStairs_memo(self, n, prev):
        """
        :type n: int
        :rtype: int
        """
        # Memoization, запоминаем уже пройденные ступени, сколько путей было до них.
        # Если уже в словаре есть, значит путь проходили - возвращаем значение
        if n in prev:
            return prev[n]

        # Base case
        if n < 0:
            return 0
        elif n == 0:
            return 1

        prev[n] = self.climbStairs_memo(n-1, prev) + self.climbStairs_memo(n-2, prev)
        return prev[n]

#Complexity Analysis

#Time complexity : O(n). Size of recursion tree can go upto n.
#Space complexity : O(n). The depth of recursion tree can go upto n.


    def climbStairs_DP(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Base case
        if n <= 0:
            return 0

        paths = dict()
        paths[1] = 1
        paths[2] = 2

        # ИЗначально зная пути до 1 и до 2, высчитываем 3 и записываем в словарь. Итеративное решение.
        for i in range(3, n+1):
            paths[i] = paths[i-1] + paths[i-2]

        return paths[n]

# Итеративное решениее, DP. Сложность та же, что и в рекурсии. Так же O(N) оба.

# Решение с O(1) space. Time is O(N). Последние 2 варианта запоминаем, не держа весь словарь в памяти, как в рекурсии или DP.
# Меняем ступеньки

    def climbStairs_change(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Base case
        if n <= 0:
            return 0

        paths = dict()
        paths[1] = 1
        paths[2] = 2

        # Не храним в словаре посл. значение. Оно не нужно. Так достигаем O(1) в space complexity.
        for i in range(3, n+1):
            paths[i] = paths[i-1] + paths[i-2]
            del paths[i-2]

        ### Либо. Используя словарь, сдвигаем. ##
        # Создаем словарь из вариантов путей (2 шага или 1)
        paths = dict()
        paths[1] = 1
        paths[2] = 2

        for i in range(3, n+1):
            # Вычисляем count - временное значение для текущего шага.
            # У нас все равно всегда только два возможных варианта. 2 шага или 1.
            count = paths[2] + paths[1]

            # Сдвигаем, чтобы всегда было только 2 последних значения.
            # Значение для 2. - Если начинаем с тройки, след значение (4). Если шаг будет 1, то потребуется 3, Если шаг 2, то 2. И т.д.
            paths[1] = paths[2]

            # Значение для 3. Текущее значение. Если начинаем с тройки, след значение (4). Если шаг будет 1, то потребуется 3, Если шаг 2, то 2. И т.д.
            paths[2] = count


        return paths[2]

sol = Solution()
print(sol.climbStairs_change(5))







def climbStairs(self, n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

def climbRec(self, i, n):
    if i > n:
        return 0
    if i == n:
        return 1
    return self.climbRec(i + 1, n) + self.climbRec(i + 2, n)

def climbStairsRec(self,n):
    return self.climbRec(0,n)
