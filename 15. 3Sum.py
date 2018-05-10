class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
            if len(nums) < 3:
                return []

            if len(nums) == 3 and sum(nums) == 0:
                return [nums]


            nums.sort()
            res = []

            for i in xrange(len(nums) - 2):

                j = i + 1
                k = len(nums) - 1

                while j < k:

                    temp_sum = nums[i] + nums[j] + nums[k]

                    if temp_sum == 0:
                        res.append((nums[i], nums[j], nums[k]))

                    if temp_sum < 0:
                        j += 1
                    else:
                        k -= 1


            return list(set(tuple(res)))


    def threeSumOpt(self, nums):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1
                if s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    #while l < r and nums[l] == nums[l+1]:
                    #    l += 1
                    #while l < r and nums[r] == nums[r-1]:
                    #    r -= 1
                    #l += 1; r -= 1
        return res

sol = Solution()
#print sol.threeSum([-3, 0, -47, 0, 50])
print sol.threeSumOpt([-1, 0, 1, 2, -1, -4])