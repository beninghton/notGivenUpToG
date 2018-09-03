class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Brute-Force. Time limit(
        # Идем по листу, вызываем функцию каждый раз, и ищем каждый раз минимальный сет
        # Затем добавляем эти сеты в ans, и возвращаем длину макисмального сета.
        ans = []
        max_len = 0


        def min_nesting(i):
            s = set()

            while nums[i] not in s:
                s.add(nums[i])
                i = nums[i]

            ans.append(s)


        for n in nums:
            min_nesting(n)

        for s in ans:
            max_len = max(max_len, len(s))

        return max_len


# T - O(N^2) - идем по листу, и для каждого вызываем операцию добавления в сет, а в ней в худшем случае пройдемся по всем.
# S - O(N^2) - лист длиной N, и в нем будут хранится все сеты.

    # Оптимальное решение
    def arrayNesting2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #Basically this problem means find the biggest cycle.
        # One thing we shall notice is once i has been visited in previous different cycle, it must not in current cycle and we can ignore it.

        ans, step, n = 0, 0, len(nums)
        seen = [False] * n
        for i in range(n):
            while not seen[i]:
                seen[i] = True
                i, step = nums[i], step + 1
            ans = max(ans, step)
            step = 0
        return ans


# T - O(N)
# S = O(N)

    # Оптимальное решение
    def arrayNesting3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #Basically this problem means find the biggest cycle.
        # One thing we shall notice is once i has been visited in previous different cycle, it must not in current cycle and we can ignore it.
        # Сдесь тот же смысл, но чтобы было O(1) Space, мы через отрицательные числа обыгрываем.

        ans, step = 0, 0
        for i in range(len(nums)):
            while nums[i] >= 0:
                num_seen = nums[i]
                nums[i] = -1
                i, step = num_seen, step + 1
            ans = max(ans, step)
            step = 0
        return ans


# T - O(N)
# S = O(1)



sol = Solution()

candidates = [5,4,0,3,1,6,2]


print(sol.arrayNesting3(candidates))
