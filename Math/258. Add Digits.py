"""
Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        # Turn it into list, summarize it, then convert back and repeat all that until single number is a result.

        # Until number is 2-digits minimum
        while num >= 10:
            # Convert to the list with int
            list_num = list(str(num))
            list_num = [int(x) for x in list_num]
            num = sum(list_num)

        # Если вышли из цикла, значит num стал меньше 10, возвращаем его
        return num


# T - O(N), N - количество символов в числе. Альтернативное мнение - You can argue that its O(1) because an integer is never more than 32 bits.
# Но хз, т.к. время выполнения то точно возрастает c увеличением числа.
# Так же, возможно это O(log(n)), т.к. с каждым разом кол-во символов сокращается, и значительно я думаю.
# S - O(N) - используем лист для хранения


    def addDigits_leetcode(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Until number is 2-digits minimum
        while(num >= 10):
            remainder = 0
            while(num > 0):
                # Вычисляем остаток и прибавляем его постоянно
                remainder += num % 10
                # Затем делим само число, получаем целое
                num //= 10
            # Как только число превратилось в ноль, присваем ему сумму остатков, т.е. чисел, из которых он состоял
            num = remainder
        return num

# T - O(N), N - количество символов в числе
# S - O(1)


# https://leetcode.com/problems/add-digits/discuss/68638/Python-constant-time-with-explanation
# "This gives us the hint that, in fact, we can take away as many 9's from a number as possible, without affecting the sum of its digits!"
# T - O(1), S - O(1)

    def addDigits_optimal(self, num):
        return num if not num else num % 9 if num % 9 else 9

sol = Solution()
res = ""

for n in range(1,100000):
    res += str(n)

print(sol.addDigits_optimal(int(res)))
