class Solution(object):

    def factorial(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if nums == 0:
            return 1
        elif nums == 1:
            return 1

        else:
            return self.factorial(nums-1) * nums


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        # Начинаем с первого индекса. Сначала берем индекс 1, и вызываем helper, чтобы получить все возможные
        # permutations после него, затем меняем его с индексом 2, и опять вызываем.
        # [1,2,3]
        # [1,3,2]
        # [2,1,3]
        # [2,3,1]
        # [3,2,1]
        # [3,1,2]

        def helper(nums, start, res):
            if start >= len(nums):
                # Добавляем копию чтобы были не ссылки на оригинальный лист, а именно новые массивы
                res.append(nums.copy())

            else:
                # Идем от стартового индекса до конца.
                for i in range(start, len(nums)):
                    # Тут меняем индексы. Если это первый раз - индекс меняется сам с собой. Т.е. в 1 раз не меняется ничего.
                    nums[start], nums[i] = nums[i], nums[start]
                    # Вызываем функцию теперь
                    helper(nums, start + 1, res)
                    # Меняем снова обратно, чтобы лист не запутался.
                    nums[start], nums[i] = nums[i], nums[start]


        helper(nums, 0, res)
        return res




sol = Solution()


print(sol.permute([1,2,3, 4]))
