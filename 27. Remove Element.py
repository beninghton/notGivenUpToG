class Solution(object):
    def removeElement(self, nums, val):
        i = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

    def removeElementOpt(self, nums, val):

        if nums == []:
            return 0


        i = 0

        k = len(nums)

        while i < k:
            if nums[i] == val:
                nums[i], nums[k-1] = nums[k-1], nums[i]
                k -= 1
            else:
                i += 1

        return i

# Solution
#
# 1. Swap each element if equal to val, swap between. If not - swap anyway (but they're the same i = j). 2 counters solution
# 2. Swap with last if equal to val. Swap with last until not equal. Move last backward(-1)







sol = Solution()

#nums=[0,1,2,2,3,0,4,2]
nums=[3,2,2,3]
#nums=[2]
lenght = sol.removeElementOpt(nums,3)



for i in range(lenght):
    print nums[i]