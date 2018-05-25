class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        map = {}

        for i in range(len(numbers)):

            if target - numbers[i] in map:
                ind = map[target - numbers[i]]

                return [ind + 1, i +1]

            map[numbers[i]] = i


sol = Solution()


print (sol.twoSum([2,3,4],6))
