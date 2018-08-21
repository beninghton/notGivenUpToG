class Solution(object):
    # O(N), O(N)
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """

        if not str:
            return

        res = []
        for ch in str:
            res.append(ch.lower())

        return ''.join(res)


    # O(N), O(1)
    def toLowerCase2(self, str):
        return str.lower()