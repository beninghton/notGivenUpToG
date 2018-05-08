class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1



sol = Solution()


nums = [1,1,1,2,2,3,3]
lenght = sol.removeDuplicates(nums)
print lenght
l = []
for i in range(lenght):
    l.append(nums[i])
print l