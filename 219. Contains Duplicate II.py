class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if len(nums) <= 1:
            return False

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True


        return False

    def containsNearbyDuplicateOpt(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if len(nums) <= 1:
            return False

        m = {}

        for i in range(0, len(nums)):

            if nums[i] in m and abs(i - m[nums[i]]) <= k:
                return True

            m[nums[i]] = i

        return False








sol = Solution()


nums = [1,0,1,1]
print sol.containsNearbyDuplicate(nums, 1)
#print sol.containsNearbyDuplicateOpt(nums, 1)
print sol.containsNearbyDuplicateOpt(nums, 1)