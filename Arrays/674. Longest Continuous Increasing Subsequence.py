class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Base case
        if nums == []:
            return 0

        max_len, loc_len = 1, 1

        # Идем и считаем длину, если она превышает. Если след элемент меньше - все сбрасываем и считаем по новой.
        for i in range(0, len(nums) - 1):

            if nums[i] < nums[i+1]:
                loc_len += 1
            else:
                if loc_len > max_len:
                    max_len = loc_len

                loc_len = 1

        # В конце возвращаем максимум, это для последней итерации, или если все возрастающие (не попадает в else)
        return max(max_len, loc_len)


# T - O(N), идем по всему массиву
# S - O(1)






sol = Solution()
candidates = [1,2,3,4,5,4,7,8,9,10]


print(sol.findLengthOfLCIS(candidates))
