class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if 0 not in nums:
            return

        i = 0
        cnt = len(nums)
        while i < cnt:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                cnt -= 1
            else:
                i += 1





sol = Solution()

nums = [0,0,0]
print (sol.moveZeroes(nums))

print nums
