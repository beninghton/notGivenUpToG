class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        l = []
        map = {}

        if len(nums) == 0:
            return []

        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]] += 1
            else:
                map[nums[i]] = 1

            if map[nums[i]] == 2:
                l.append(nums[i])

            if map[nums[i]] > 2:
                l.remove(nums[i])

        return l

    def findDuplicatesOpt(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []

        if len(nums) == 0:
            return []

        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                res.append(nums[i])

        return res




        return res

    def removeDuplicates(self, nums):

        l = []

        for i in nums:
            if i not in l:
                l.append(i)
        return l

sol = Solution()


nums = [4,3,2,7,8,2,3,1]

res = sol.findDuplicatesOpt(nums)
print res
