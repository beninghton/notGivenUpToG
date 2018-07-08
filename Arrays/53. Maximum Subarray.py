class Solution:
    def maxSubArray_brute_force(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0

        max_sum = nums[0]

        for i in range(len(nums)-1):
            loc_sum = nums[i]
            for k in range(i+1, len(nums)):
                if nums[k] > max_sum:
                    max_sum = nums[k]
                loc_sum += nums[k]
                if loc_sum > max_sum:
                    max_sum = loc_sum

        return max_sum


    def maxSubArray_kadane(self, nums):

        if nums == []: return 0
        loc_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            loc_sum = max(nums[i], nums[i]+loc_sum)
            if loc_sum > max_sum:
                max_sum = loc_sum

        return max_sum

    def maxSubArray_leetcode(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if all(n < 0 for n in nums):
            return max(nums)
        i = 0
        a = 0
        maxsum = 0
        while i < len(nums):
            b = c = 0
            while i < len(nums) and nums[i] <= 0:
                b += nums[i]
                i += 1
            while i < len(nums) and nums[i] >= 0:
                c += nums[i]
                i += 1
            a = max(a + b + c, c)
            maxsum = max(maxsum, a)
        return maxsum

#nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,-3,4,1]
sol = Solution()
print(sol.maxSubArray_leetcode(nums))

# 1. O(N^2), O(1). Simply loop through all elements and find max subarray
# 2. O(N), O(1). Kadane's algorithm. Go through the array 1 time, and find max between previous subarray and current element.


