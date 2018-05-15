class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if nums == []:
            return 0

        for i in range(len(nums)):

            if nums[i] == target:
                return i

            if nums[i] > target:

                if i == 0:
                    return 0
                else:
                    return i

        return i + 1


    def searchInsertOpt(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left)/2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left






sol = Solution()

print sol.searchInsertOpt([1,3,5,6], 5)
#print (sol.longestCommonPrefix(["racecar","car"]))
#print (sol.longestCommonPrefix("abcabcbb"))
#print (sol.longestCommonPrefix("dvdf"))