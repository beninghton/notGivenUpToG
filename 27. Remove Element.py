class Solution(object):
    def removeElement(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
        return start







sol = Solution()

nums=[0,1,2,2,3,0,4,2]
nums=[3,2,2,3]
#nums=[2,2,2,2]
lenght = sol.removeElement(nums,3)



for i in range(lenght):
    print nums[i]