from collections import Counter

class Solution:

    # Brute-Force Solution.
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == []:
            return 0
        if len(nums) == 1:
            return 1

        # Сначала определяем degree исходного массива
        degree = 0
        for n in nums:
            degree = max(degree, nums.count(n))

        min_len = float('inf')

        # Идем по листу и для каждого элемента считаем его count. Если он совпадает с degree - считаем минимальную разницу между индексами.
        # И так для каждого элемента.
        for i in range(len(nums)):
            count = 1
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
                    if count == degree:
                        min_len = min(min_len, j - i + 1)
                        count = 1

        return min(min_len, len(nums))

# T - O(N^2)
# S - O(1)


    def findShortestSubArray2(self, nums):
        if nums == []:
            return 0

        # Идея такая. Заводим 3 словаря, чтобы хранить
        # 1. Количество появлений элемента
        # 2. Стартовый индекс
        # 3. Конечный индекс
        # Дальше вычисляем Degree. И смотрим разницу старт и конеч индексов для элементов, у которых этот degree(кол-во появлений)

        st, end, count = {}, {}, {}

        for i, n in enumerate(nums):
            if n not in st:
                st[n] = i

            count[n] = count.get(n, 0) + 1
            # Правый индекс двигаем
            end[n] = i

        # Находим Degree, это макс значение в словаре count
        degree = max(count.values())
        min_len = float('inf')

        for key, val in count.items():
            if val == degree:
                min_len = min(min_len, end[key] - st[key] + 1)


        return min_len


# T - O(N)
# S - O(N)






sol = Solution()
candidates = [1,2,2,3,1]

print(sol.findShortestSubArray2(candidates))
