class Solution(object):
    def findMin(self, nums):            # O(N)
        """
        :type nums: List[int]
        :rtype: int
        """

        min = nums[0]

        for d in nums:
            if d < min:
                min = d
        return min


    def findMinOpt(self,nums):          # O(Log(N))

        left = 0
        right = len(nums) - 1

        while left < right:

            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right)/2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


sol = Solution()

print sol.findMinOpt([4,5,6,7,0,1,2])