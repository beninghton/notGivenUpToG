class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Сортируем, и по сортированному массиву ищем. Долго объяснять почему так, но решить самому возможно.
        # Главное - нарисовать примеры для всех base case и тогда все будет ок.

        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        nums = sorted(nums)

        ans_left = nums[0] * nums[1]
        ans_right = nums[-1] * nums[-2]


        # If both < 0 or both > 0
        if ans_right > 0:
            if nums[-1] < 0 and nums[-2] < 0:
                return ans_right * nums[-3]
            else:
                return max(ans_right * nums[-3], ans_left * nums[-1])

        elif ans_right < 0:
            return ans_left * nums[-1]

        else:
            if nums[-1] == 0:
                return 0
            else:
                return ans_left * nums[-1]


# T - O(N*LogN) - из за сортировки
# S - O(N*LogN) - сортировка тоже отнимает спейс. Получаем же новый массив.

    # Тоже самое in one line
    def maximumProduct2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = sorted(nums)
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])


    # Оптимальное решение за O(N)
    def maximumProduct3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Не будем сортировать. Ищем 2 минимальных элемента и 3 максимальных.
        # И с ними оперируем, как в short примере выше.

        min1, min2 = float('inf'), float('inf')
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')

        for n in nums:
            # Find Maximums
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n

            elif max1 > n > max2:
                max3 = max2
                max2 = n

            elif n > max3:
                max3 = n

            # Find minimums
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n


        return max(max1 * max2 * max3, min1 * min2 * max1)



# T - O(N)
# S - O(1)




sol = Solution()

candidates = [722,634,-504,-379,163,-613,-842,-578,750,951,-158,30,-238,-392,-487,-797,-157,-374,999,-5,-521,-879,-858,382,626,803,-347,903,-205,57,-342,186,-736,17,83,726,-960,343,-984,937,-758,-122,577,-595,-544,-559,903,-183,192,825,368,-674,57,-959,884,29,-681,-339,582,969,-95,-455,-275,205,-548,79,258,35,233,203,20,-936,878,-868,-458,-882,867,-664,-892,-687,322,844,-745,447,-909,-586,69,-88,88,445,-553,-666,130,-640,-918,-7,-420,-368,250,-786]
#candidates = [1,0,-60,60,2]

print(sol.maximumProduct3(candidates))
