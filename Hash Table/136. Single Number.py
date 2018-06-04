class Solution(object):                 # O(N), O(N)
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """



        for el in nums:
            if el in map:
                map[el] += 1
            else:
                map[el] = 1


        for el in map:
            if map[el] < 2:
                return el



    def singleNumber2(self, nums):  # O(N), O(1). XOR
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i

        return a



sol = Solution()


print (sol.singleNumber2([2,1,5,2,5,8]))




