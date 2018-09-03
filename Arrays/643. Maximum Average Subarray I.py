class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        # Brute-Force. Time Limit.
        max_sub = float('-inf')

        for i in range(0, len(nums) - k + 1):
            summ = 0
            for n in range(i, i + k):
                summ += nums[n]

            max_sub = max(max_sub, summ/k)


        return max_sub



# T - O((N-K)* K)
# S - O(1) - доп места не занимаем


    # Оптимальное решение.
    def findMaxAverage2(self, nums, k):

        temp_res = 0

        # Считаем первый раз макисмальный subarray
        for i in range(k):
            temp_res += nums[i]

        max_sub = temp_res / k


        for i in range(1, len(nums) - k + 1):
            # Затем от единицы пошли считать остальные. К временной сумме прибавляем следующий и отнимаем предыдущий.
            temp_res = temp_res - nums[i - 1] + nums[i + k - 1]
            max_sub = max(max_sub, temp_res / k)


        return max_sub

# T - O(N)
# S - O(1)


sol = Solution()
nums = [-1]
k = 1



print(sol.findMaxAverage2(nums, k))
