class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []

        setNums = set(nums)

        for i in range(1,len(nums)+1):
            if i not in setNums:
                res.append(i)

        return res

    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        res = [i+1 for i,x in enumerate(nums) if x > 0]
        return res

    def findDisappearedNumbers3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        nums = [0] + nums
        for i in range(1, len(nums)):
            n = nums[i]
            while n != i and nums[n] != n:
                nums[i], nums[n] = nums[n], nums[i]
                n = nums[i]
        for i, n in enumerate(nums):
            if i != n:
                ret.append(i)
        return ret


sol = Solution()

nums = [3,2,3,4]
print (sol.findDisappearedNumbers3(nums))
