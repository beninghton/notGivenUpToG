class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')


#The run time depends on the number of bits in n.
        # Обычно, не больше 32 бит (тогда сложность O(1)). Но это питон, тут можно хранить сколь угодно большие числа, поэтому O(N) - где N - количество битов в исходном числе.(нам надо пройти все чтобы посчитать сколько единиц)
#The space complexity is O(1), since no additional space is allocated.


    # Классчи решение для 32 битов. Сдвигаем маску постоянно (в маске 1, сначала 1, затем 10, затем 100 и т.д.) И сравниваем каждый бит по отдельности до 32.
    # Если бит совпал - значит единичка там, и прибавляем count. Иначе сдвигаем дальше.
    def hammingWeight2(self, n):
        """
        :type n: int
        :rtype: int
        """
        mask = 1
        count = 0

        for i in range(32):
            if n & mask != 0:
                count += 1
            mask = mask << 1
            print(mask)

        return count

# Вот тут O(1), O(1)

sol = Solution()
print(sol.hammingWeight2(11))
print(1 << 5)