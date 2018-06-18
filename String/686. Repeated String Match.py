class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        start_len_a = len(A)
        origin_a = A
        br = False

        while B not in A:
            if len(A) > len(B) * 2 and len(A) >= start_len_a * 2:
                br = True
                break
            else:
                A += origin_a

        if br:
            return -1
        else:
            return int(len(A)/start_len_a)

    def repeatedStringMatch_opt(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        cur = A
        num = 1
        while len(cur) <= len(B):   # Догнал его по длине
            if B in cur:
                return num
            cur += A                # если все еще нет, еще раз прибавляем A
            num += 1

        if B in cur:                # если B в A, возвращаем
            return num
        elif B in cur + A:          # это если у нас она в цикл while не попала, т.к. длина А уже больше длины B
            return num + 1
        else:                       # ничего не помогло, возвращаем -1
            return -1

    def repeatedStringMatch_leetcode(self, A, B):
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q+i): return q+i
        return -1


    def repeatedStringMatch_rabin_karp(self, A, B):
        def check(index):
            return all(A[(i + index) % len(A)] == x
                       for i, x in enumerate(B))

        q = (len(B) - 1) // len(A) + 1

        p, MOD = 113, 10**9 + 7
        p_inv = pow(p, MOD-2, MOD)
        power = 1

        b_hash = 0
        for x in map(ord, B):
            b_hash += power * x
            b_hash %= MOD
            power = (power * p) % MOD

        a_hash = 0
        power = 1
        for i in xrange(len(B)):
            a_hash += power * ord(A[i % len(A)])
            a_hash %= MOD
            power = (power * p) % MOD

        if a_hash == b_hash and check(0): return q

        power = (power * p_inv) % MOD
        for i in xrange(len(B), (q+1) * len(A)):
            a_hash = (a_hash - ord(A[(i - len(B)) % len(A)])) * p_inv
            a_hash += power * ord(A[i % len(A)])
            a_hash %= MOD
            if a_hash == b_hash and check(i - len(B) + 1):
                return q if i < q * len(A) else q+1

        return -1

sol = Solution()

#Complexity Analysis

#Time Complexity: O(N*(N+M)), where M,N are the lengths of strings A, B. We create two strings A * q, A * (q+1) which have length at most O(M+N).
#  When checking whether B is a substring of A, this check takes naively the product of their lengths.
#Space complexity: As justified above, we created strings that used O(M+N) space.

# B * A = B * (A+B), т.к. A в худшем случае равно (A+B)