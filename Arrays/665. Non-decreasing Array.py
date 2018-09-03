class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if nums == []:
            return False
        if len(nums) == 1:
            return True

        # Делаем копии массивов. Решение тут https://www.youtube.com/watch?v=CcDZOJ2Pt2E
        a = nums.copy()
        b = nums.copy()

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                a[i] = nums[i+1]
                b[i+1] = nums[i]
                break


        return nums == sorted(a) or nums == sorted(b)

# T - N*LogN - сортировка.
# S - O(N) - 2 массива.



    def checkPossibility2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mod = False

        for i in range(len(nums) - 1):
            # Если след больше предыдущего, и это первый раз
            if nums[i] > nums[i + 1]:
                if mod:
                    return False
                else:
                    # Если это первый элемент, или предыдущий меньше следующего. То меняем этот элемент.
                    if i < 1 or nums[i - 1] <= nums[i + 1]:
                        # Присваеваем этому элементу значение следующего.
                        nums[i] = nums[i + 1]
                    else:
                        # Иначе, меняем следующий элемент.
                        # Присваеваем следующему элементу значение этого.
                        nums[i+1] = nums[i]
                mod = True

        return True

# T - O(N)
# S - O(1)
# Так же https://leetcode.com/problems/non-decreasing-array/discuss/106826/JavaC++-Simple-greedy-like-solution-with-explanation

sol = Solution()

candidates = [3, 4,2,3]


print(sol.checkPossibility2(candidates))
