class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Base Case
        # Либо ограбил, либо нет. Ограбил - получил прибыль. Не ограбил - идем дальше по массиву. Time limit.

        def helper_dfs(pos):
            if pos >= len(nums):
                return 0

            # Opt - ограбил и перешел на 2 шага, opt2 - не ограбил, перешел на 1 шаг.
            opt1 = nums[pos] + helper_dfs(pos + 2)
            opt2 = helper_dfs(pos + 1)


            return max(opt1, opt2)

# DFS O(2^n) time complexity
# DFS O(2^n) space complexity

        # Key - position, value - value
        cache = dict()

        def helper_dfs_cache(pos, cache):

            if pos >= len(nums):
                return 0

            if pos in cache:
                return cache[pos]

            # Opt - ограбил и перешел на 2 шага, opt2 - не ограбил, перешел на 1 шаг.
            opt1 = nums[pos] + helper_dfs_cache(pos + 2, cache)
            opt2 = helper_dfs_cache(pos + 1, cache)
            cache[pos] = max(opt1, opt2)

            return cache[pos]

        return helper_dfs_cache(0, cache)

# T - O(N) - идем 1 раз по каждому элементу, т.к. у нас в кэше уже запомненные значения, и второй раз мы уже их просто оттуда забираем.
# S - O(N) - храним значения всех позиций в кеше.


        # Bottom up DP solution
    def rob_dp(self, nums):
        # Define base cases. Если длина нулевая или 1 элемент, мы возвращаем его.
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # Если 2 элемента, то мы возвращаем максимальный из них. Т.к. мы не можем вернуть оба, т.к. они соседи.
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # Далее если элементов больше двух:
        # Инициализируем начальные условия, в отличии от рекурсии, где у нас конечные условия отрабатываются как base cases.
        # Инициализируем новый массив, где будем хранить результаты максимальных элементов, и в итоге вернем последний, как самый максимальный.
        res = [0] * len(nums)
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        # Далее от 3го элемента начинаем пихать максимум в этот массив
        for i in range(2, len(nums)):
            # Сдесь 2 варианта. Либо берем элемент, тогда надо сложить его с пред-предыдушщим. (на 2 меньше)
            # Второй вариант, не берем его, тогда берем предыдущий.
            # И смотрим какой вариант нам выгодней, т.е. какой максимальный.
            opt1 = nums[i] + res[i - 2]
            opt2 = res[i - 1]
            res[i] = max(opt1, opt2)

        # Возвращаем максимальный вариант, который находится в конце списка
        return res[-1]

# T - O(N) - идем 1 раз по каждому элементу
# S - O(N) - храним макс значения в отдельном массиве


    # Можем сделать за O(1) space, т.к. будем запоминать только посл 3 элемента.
    def rob_dp_opt(self, nums):
        # Define base cases. Если длина нулевая или 1 элемент, мы возвращаем его.
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # Если 2 элемента, то мы возвращаем максимальный из них. Т.к. мы не можем вернуть оба, т.к. они соседи.
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # Далее если элементов больше двух:
        # Инициализируем начальные условия, в отличии от рекурсии, где у нас конечные условия отрабатываются как base cases
        # Работем на переменных. Запоминаем предпоследние и пред-пред последние значения.

        prev_prev = nums[0]
        prev = max(nums[0], nums[1])
        # Далее от 3го элемента идем
        for i in range(2, len(nums)):
            # Сдесь 2 варианта. Либо берем элемент, тогда надо сложить его с пред-предыдушщим. (на 2 меньше)
            # Второй вариант, не берем его, тогда берем предыдущий.
            # И смотрим какой вариант нам выгодней, т.е. какой максимальный.
            opt1 = nums[i] + prev_prev
            opt2 = prev
            # Запоминаем только два предыдущих элемента, чтобы не держать весь массив.
            prev_prev = prev
            prev = max(opt1, opt2)


        # Возвращаем максимальный вариант, который находится в конце списка
        return prev


# T - O(N) - идем 1 раз по каждому элементу
# S - O(1) - только переменные

#https://www.youtube.com/watch?v=NqqAhSgYBm4


sol = Solution()
print(sol.rob_dp_opt([1,2,3,1,5,6]))

# https://leetcode.com/problems/house-robber/discuss/55838/DP-O(N)-time-O(1)-space-with-easy-to-understand-explanation