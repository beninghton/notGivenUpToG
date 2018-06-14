class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """


        neutral = set("018")
        valid = set("2569")
        cnt = 0
        res = False

        for digit in range(1, N+1):
            l = 0

            for d in str(digit):
                if d not in neutral and d not in valid:
                    res = False
                    l = 0
                    break
                elif d in neutral:
                    l += 1
                else:
                    res = True

            if res and l < len(str(digit)):
                cnt += 1

        return cnt




sol = Solution()



print sol.rotatedDigits(10)

11, 12, 13, 14, 15, 16, 17, 18, 19, 20

# INDIVIDUALLY

# O(N*K), N - range, K - lenght of digit
# O(N*K) - space complexity
