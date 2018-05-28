class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        res = []
        res2 = []
        x = c
        i = 0

        if c * r != len(nums) * len(nums[0]):
            return nums

        for el in nums:
            res += el

        while x <= len(res):    # how many columns
            res2.append(res[i:x]) # number of elements in a raw
            i = x
            x += c



        return res2





sol = Solution()

nums = [[1,2],
        [3,4]]
print (sol.matrixReshape(nums,3,2))


