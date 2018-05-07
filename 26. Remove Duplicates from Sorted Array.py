class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0

        i = 1
        while len(nums) > 0:
            if nums[i] == nums[i-1]:
                nums.pop(i-1)
                if i > len(nums)-1:
                    break
            else:
                if i == len(nums)-1:
                    break
                i += 1

        return len(nums)



    def removeDuplicatesOpt(self, nums):
        ind = 0
        if nums == []:
            return 0
        for i in range(len(nums)):
            if nums[ind] != nums[i]:
                ind += 1
                nums[ind], nums[i] = nums[i], nums[ind]
        return ind + 1




sol = Solution()


nums = [1,1]
lenght = sol.removeDuplicatesOpt(nums)
#print lenght
l = []
for i in range(lenght):
    l.append(nums[i])
print l