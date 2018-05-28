class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = cnt = max = 0

        while i < len(nums):
            if nums[i] == 1:
                cnt +=1
                if cnt > max:
                    max = cnt
            else:
                cnt = 0
            i += 1
        return max

sol = Solution()

nums = [1,0,1,1,0,1]
print (sol.findMaxConsecutiveOnes(nums))
