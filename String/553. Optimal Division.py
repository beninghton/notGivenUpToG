class Solution(object):
    # O(N), O(N). Ответ всегда будет = первый делитель, разделить на скобку. Кароче если делить все подряд - всегда наибольший результат, чем делить выборочно.
    def optimalDivision(self, nums):
        if len(nums) == 1:
            return str(nums[0])

        if len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])

        res = str(nums[0]) + '/(' + str(nums[1])

        for i in range(2, len(nums)):
            res += '/' + str(nums[i])

        res += ')'
        return res

#Time complexity : O(n). Single loop to traverse nums array.
#Space complexity : O(n). resres variable is used to store the result.

sol = Solution()
print(sol.optimalDivision2([100,10,5]))

#https://leetcode.com/problems/optimal-division/solution/