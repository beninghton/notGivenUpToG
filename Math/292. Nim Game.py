"""
Input: 4
Output: false
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be
             removed by your friend.
"""


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Будет рекурсивное решение.  Берем 1 2 или 3 камня каждый раз и меняем очередь. С DP. Без DP - time limit exceeded.
        # Смотрим будет ли True хоть в одном из этих вариантов.
        # Определяем хелпер функцию и общую переменную "чья очередь". Первый беру я.

        memo = dict()

        def helper(n, my_turn, memo):

            # Проверяем есть ли результат уже в словаре
            if (n, my_turn) in memo:
                return memo[n]

            # Base case. Если моя очередь - выигрываю я. Если нет, мой противник.
            if n <= 3 and my_turn:
                return True
            elif n <= 3 and not my_turn:
                return False

            # Передаем очередь
            my_turn = not my_turn

            # Берем сразу все 3 варианта
            memo[(n, my_turn)] = helper(n - 1, my_turn, memo) or helper(n - 2, my_turn, memo) or helper(n - 3, my_turn, memo)
            return memo[(n, my_turn)]


        return helper(n, True, memo)


# Ппц, вообще не понял задачу. Решение:
    def canWinNim(self, n):
        if n % 4 == 0:
            return False
        else: return True

        # Типа если на 4 делится, тогда мы проиграем, т.к. наш противник играет умно.

sol = Solution()
for n in range(1, 100):
    print(sol.canWinNim(n))
