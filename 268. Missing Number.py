class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        if nums == [0]:
            return 1
        if nums == [1]:
            return 0

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                return nums[i] - 1

        if nums[0] == 0:
            return nums[i] + 1
        else:
            return 0




sol = Solution()

nums = [0]
print (sol.missingNumber(nums))
