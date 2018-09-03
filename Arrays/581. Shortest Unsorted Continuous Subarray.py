class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Идея такая - при отсортированном массиве индексы не будут совпадать, и с первого несовпадающего индекса как бы начинается Subarray.
        # И дальше хоть индексы могут и совпадать, нам надо искать где закончится "несовпадение". Это будет концом Subarray.
        # Он будет всегда минимальный, т.к. даже если нам надо 1 индекс вначале поменять, и 1 в конце - между ними все равно все нужно менять, поэтому общая длина составит:
        #    индекс конца - индекс начала
        #
        # Сначала сортируем исходный массив и получаем эту сортированную копию.
        nums_sorted = sorted(nums)

        # Определяем индексы минимума и максимума, и их ищем. В 1 loop идем сначала, во 2 - с конца. Дальше разница и +1 (из за индексов).
        min_ind, max_ind = 0, 0

        for i in range(len(nums)):
            if nums[i] != nums_sorted[i]:
                min_ind = i
                break

        for i in range(len(nums) -1 , -1, -1):
            if nums[i] != nums_sorted[i]:
                max_ind = i
                break


        if max_ind == 0 and min_ind == 0:
            return 0
        else:
            return max_ind - min_ind + 1


# T - O(N*LogN) + O(N) = O(N*LogN) - из-за сортировки.
# S - O(N), из за сортированного массива.



    # O(N), O(1)
    def findUnsortedSubarray2(self, nums):


        # Base case
        if len(nums) < 2 or nums == []:
            return 0

        # Идем по неотсортированному массиву
        # Находим начальную точку, где наш массив становится "неправильным", слева и справа.
        l, r = 0, len(nums) - 1

        # Ищем левый индекс.
        while l < r and nums[l] <= nums[l+1]:
            l += 1
            # Если расхождений не было и массив отсортирован - возвращаем ноль.
            if l >= r:
                return 0

        # Если не вернулись, ищем правый индекс.
        while r > 0 and nums[r] > nums[r-1]:
            r -= 1

        # Дальше ищем в пределах нашего "неправильного" подмассива минимальное и максимальное значение.
        min_val, max_val = nums[l], nums[r]

        for i in range(l, r+1):
            min_val = min(min_val, nums[i])
            max_val = max(max_val, nums[i])

        # Дальше идем по массиву вновь с двух сторон, и смотрим когда у нас минимальное значение превысится, а максимальное принизится.
        for i in range(len(nums)):
            if nums[i] > min_val:
                l = i
                break

        for i in range(len(nums) -1 , -1, -1):
            if nums[i] < max_val:
                r = i
                break

        return r - l + 1

# T - O(N) - не сортируем, просто ходим по масссиву с разных сторон.
# S - O(1),


sol = Solution()
#candidates = [2, 6, 4, 8, 10, 9, 15]
candidates = [2,1,5,4,7]

print(sol.findUnsortedSubarray2(candidates))
