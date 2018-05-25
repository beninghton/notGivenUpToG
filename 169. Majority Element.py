class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        nums.sort()

        i = 1
        cnt = 1

        while i < len(nums):

            if nums[i] != nums[i-1]:
                if cnt > len(nums)/2:
                    return nums[i-1]
                else:
                    cnt = 1

            cnt += 1
            i += 1

        return nums[-1]



sol = Solution()


print (sol.majorityElement([2,1,1,1,2,2,2]))
