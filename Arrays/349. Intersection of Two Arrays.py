class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ans = []

        # To have unique values, convert both to set, and one list back to list, to have iteration possibility

        nums1 = set(nums1)
        nums2 = set(nums2)

        # Which list is longer, will be iterative and which is shorter - will be set to perform quick lookups in it.
        if len(nums1) >= len(nums2):
            nums1 = list(nums1)
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    ans.append(nums1[i])

        else:
            nums2 = list(nums2)
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    ans.append(nums2[i])

        # Return list with unique items. Order does not matter.
        return ans


# T - O(N + M)), где N - длина nums1, M - nums2. Когде конвертируем в сеты это O(N)
# S - O(N + M), используем сеты и листы чтобы хранить оба списка. В худшем случае если они уникальны - будет так.

    # Upd - не важно кто из них длиннее. Важно сделать 1 сетом и итерировать по другому.
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        res_set = set([num for num in nums2 if num in nums1_set])
        return list(res_set)

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=set(nums1)
        nums2=set(nums2)
        return list(nums1&nums2)


    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 is None: return []
        if nums2 is None: return []

        return list(set(nums1).intersection(nums2))