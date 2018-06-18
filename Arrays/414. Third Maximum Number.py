class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 3

        nums = list(set(nums))

        if len(nums) < 3:
            max_val = nums[0]

            for n in nums:
                if n > max_val:
                    max_val = n
            return max_val


        while k != 0:

            max_val = nums[0]

            for n in nums:
                if n > max_val:
                    max_val = n

            nums.remove(max_val)
            k -= 1

        return max_val


    def thirdMax_2(self, nums):
        m = [float('-inf'), float('-inf'), float('-inf')]

        for n in nums:
            if n not in m:
                if n > m[0]:
                    m = [n, m[0], m[1]]
                elif n > m[1]:
                    m = [m[0], n, m[1]]
                elif n > m[2]:
                    m = [m[0], m[1], n]

        if float('inf') in m:
            return m[0]
        else:
            return m[2]

sol = Solution()




print(sol.thirdMax_2([1,2,2,5,3,5]))


# 1. O(N), O(N)
# Находим максимум, затем убираем этот элемент из массива

# 2. O(N), O(1). Держим в store m - 3 элемента, и смещаем их по мере того как появляется новый максимум.