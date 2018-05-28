class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        cnt = 0
        l = set()


        for i in range(len(nums)-1):
            for n in range(i+1,len(nums)):
                if abs(nums[i] - nums[n]) == k:
                    if nums[i] not in l or nums[n] not in l:
                        cnt += 1
                        l.add(nums[i])
                        l.add(nums[n])
        return cnt

    def findPairs2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        comp = {}
        last_pair, pairs = None, 0
        for num in nums:
            if num in comp:
                if (comp[num], num) != last_pair:
                    pairs += 1
                    last_pair = (comp[num], num)
            comp[num+k] = num
        return pairs

    def findPairs3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import collections
        ct = collections.Counter(nums)
        if k < 0:
            return 0
        if k == 0:
            return sum(ct[i] > 1 for i in ct)
        if k > 0:
            return sum(i+k in ct for i in ct)

sol = Solution()

nums = [3,2,3,2]
#print (sol.findPairs(nums,1))
#print (sol.findPairs2(nums,1))
print (sol.findPairs3(nums,1))