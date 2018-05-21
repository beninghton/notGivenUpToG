class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a = int(a,2)
        b = int(b,2)

        c = bin(a+b)[2:]
        return c

    def addBinaryHard(self, a, b):

        res = []
        carry = 0

        diff = abs(len(a) - len(b))

        if len(a) < len(b):
            a = "0"*diff + a
        else:
            b = "0"*diff + b

        i = len(b) - 1

        while i >= 0:
            if a[i] == "1" and b[i] == "1":
                res.append(0 + carry)
                carry = 1

            elif a[i] == "0" and b[i] == "0":
                res.append(0 + carry)
                carry = 0

            else:
                if int(a[i]) + int(b[i]) + carry > 1:
                    res.append(0)
                else:
                    res.append(1)
                    carry = 0
            i -= 1

        if carry == 1:
            res.append(1)

        res = [str(x) for x in res[::-1]]

        return ''.join(res)


sol = Solution()


print (sol.addBinary("0111","1100"))
print (sol.addBinaryHard("1","1100"))