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

        if len(nums) < 3:
            return []

        if len(nums) == 3 and sum(nums) == 0:
            return [nums]


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
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

sol = Solution()
#print sol.threeSum([-3, 0, -47, 0, 50])
print sol.threeSumOpt([-1,-1,-1,2])

# Two shields from duplicates:
#
# 1. if i > 0 and nums[i] == nums[i-1]:  - Move i if repeats, move past repeats until i is unique
#       continue
#
# 2. while l < r and nums[l] == nums[l+1]:      - Move lefts to right, until left value is unique
#        l += 1
#    while l < r and nums[r] == nums[r-1]:      - Move rights to left, until right value is unique
#        r -= 1
#