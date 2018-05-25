class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1:
            return

        if k >= len(nums):
            if k % len(nums) == 0:
                return
            else:
                k = k % len(nums)
                shift = len(nums) - k
        else:
            shift = len(nums) - k

        nums[:] = nums[shift:] + nums[:shift]

    def rotateOpt(self, nums, k):

        k = k % len(nums)

        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)


    def reverse(self,nums,start,end):

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

sol = Solution()


nums = [1,2,3,4,5]

res = sol.rotate(nums,2)
print nums

nums = [1,2,3,4,5]
sol.rotateOpt(nums,2)

print nums
