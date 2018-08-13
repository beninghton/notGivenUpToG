class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Time limit exceeded.
        if n <= 0:
            return False

        ugly_list = []
        ugly = True
        num = 0
        i = 0

        # Формируем лист, пока не дойдем до формирования i-го элемента, который будет равен как раз входному n.
        while len(ugly_list) <= n:
            num += 1
            temp = num
            while temp != 1:
                if temp % 2 == 0:
                    temp = temp // 2
                elif temp % 3 == 0:
                    temp = temp // 3
                elif temp % 5 == 0:
                    temp = temp // 5
                else:
                    ugly = False
                    break

            # Добавляем если ugly
            if ugly:
                ugly_list.append(num)
                i += 1
            else:
                # Иначе снова переворачиваем ugly
                ugly = True

            # Вот тут как раз i-ый элемент равен входному n. Возвращаем его.
            if n == i and ugly:
                print(ugly_list)
                return ugly_list[i - 1]

# T - O(N*Log(N)), where N - is n(длина листа), и логарифм - это поиск ugly или не ugly для каждого N.
# S - O(N), лист в котором храним как раз ugly элементы.

    """
    def nthUglyNumber(self, n):
        # Time limit exceeded.
        if n <= 0:
            return False

        ugly = True
        num = 0
        i = 0

        # Формируем лист, пока не дойдем до формирования i-го элемента, который будет равен как раз входному n.
        while i <= n:
            num += 1
            temp = num
            while temp != 1:
                if temp % 2 == 0:
                    temp = temp // 2
                elif temp % 3 == 0:
                    temp = temp // 3
                elif temp % 5 == 0:
                    temp = temp // 5
                else:
                    ugly = False
                    break

            # Добавляем если ugly
            if ugly:
                i += 1
            else:
                # Иначе снова переворачиваем ugly
                ugly = True

            # Вот тут как раз i-ый элемент равен входному n. Возвращаем его.
            if n == i and ugly:
                return num   


# T - O(N*Log(N)), where N - is n(длина листа), и логарифм - это поиск ugly или не ugly для каждого N.
# S - O(1), листа нет.
    """

    # Оптимальное решение, leetcode
    #https://www.geeksforgeeks.org/ugly-numbers/
    def nthUglyNumber_2(self, n):
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            # Пока индекс * 2 меньше последнего элемнта, увеличиваем i
            while ugly[i2] * 2 <= ugly[-1]: i2 += 1
            while ugly[i3] * 3 <= ugly[-1]: i3 += 1
            while ugly[i5] * 5 <= ugly[-1]: i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]


    # Динамически меняет лист. Берет генерирует 3 листа, мерджит их и по ним идет. С каждой генерацией n уменьшается на единицу.
    def nthUglyNumber_heap(self, n):
        import heapq
        q2, q3, q5 = [2], [3], [5]
        ugly = 1
        for u in heapq.merge(q2, q3, q5):
            print(list(heapq.merge(q2, q3, q5)))
            if n == 1:
                return ugly
            if u > ugly:
                ugly = u
                n -= 1
                q2.append(2*u)
                q3.append(3*u)
                q5.append(5*u)


    # Заполняем массив по мере движения, заранее вычисляя множители (т.к. след число должно делиться только на 2, 3, 5)
    def getNthUglyNo(self, n):

        ugly = [0] * n # To store ugly numbers

        # 1 is the first ugly number
        ugly[0] = 1

        # i2, i3, i5 will indicate indices for 2,3,5 respectively
        i2 = i3 = i5 = 0

        # set initial multiple value
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5

        # start loop to find value from ugly[1] to ugly[n]
        for i in range(1, n):

            # choose the min value of all available multiples
            ugly[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

            # increment the value of index accordingly
            if ugly[i] == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = ugly[i2] * 2

            if ugly[i] == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly[i3] * 3

            if ugly[i] == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = ugly[i5] * 5

        # return ugly[n] value
        return ugly[-1]

#Algorithmic Paradigm: Dynamic Programming
#Time Complexity: O(n)
#Auxiliary Space: O(n)

sol = Solution()

print(sol.getNthUglyNo(10))
