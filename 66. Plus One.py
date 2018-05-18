class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ""

        for i in digits:
            s+= str(i)

        d = int(s) + 1

        s = str(d)

        return [int(x) for x in s]


    def plusOneOpt(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            last = digits.pop()
            digits.append(last+1)
            return digits


        for i in range(len(digits)-1, -1, -1):

            if digits[i] + 1 == 10:
                digits[i] = 0

            else:
                digits[i] = digits[i] + 1
                return digits

            if i == 0:
                digits.append(1)

        return digits[::-1]

    def plusOneCool(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        plus =1
        for i in range (len(digits)-1,-1,-1):

            if digits[i]<=8:
                digits[i] = digits[i]+1
                return digits
            else:
                digits[i] = 0

        digits.insert (0,1)
        return digits




sol = Solution()
import time


print(sol.plusOneCool([9,9,9,9]))

