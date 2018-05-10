class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 0:
            return False

        numsS = set(nums)
        if len(nums) > len(numsS):
            return True
        else:
            return False