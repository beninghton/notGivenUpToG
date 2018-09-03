class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        # Base cases
        if n <= 0:
            return True

        if len(flowerbed) == 1:
            if n == 1 and flowerbed[0] == 0:
                return True
            else:
                return False

        if len(flowerbed) == 2:
            if n == 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
                return True
            else:
                return False

        # If len(flowerbed) > 3

        for i in range(1, len(flowerbed) -1):

            # First case. Если у нас ситуация [0,0,1], кароче два нуля вначале. Нам надо проверить что текущий и предыдущий == 0, и посадить цветок в первый.
            if i == 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i - 1] = 1
                n -= 1

            # Second case. Ситуация обратная выше. [1,0,0], кароче два нуля вконце. Нам надо проверить что текущий и следующий == 0, и посадить цветок в последний.
            if i == len(flowerbed)-2 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i + 1] = 1
                n -= 1

            # Обычная ситуация, когда цветок не первый и не последний, а мы в середине.
            # Не сработает, если сработали первые два, т.к. цветок уже посажен в текущий i.
            # Смотрим если слева и справа цветов нет, тогда садим.
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1

        # n - может быть меньше нуля, если мы садим цветков меньше, чем проходим по массиву. Там то мы n постоянно отнимаем.
        return n <= 0


# T - O(N) - проходим все цветки.
# S - O(1) - не исп доп места кроме того что меняем исходный массив.


    # Тот же алгоритм, просто выходим раньше если n уже равно 0.
    def canPlaceFlowers2(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        # Base cases
        if n <= 0:
            return True

        if len(flowerbed) == 1:
            if n == 1 and flowerbed[0] == 0:
                return True
            else:
                return False

        if len(flowerbed) == 2:
            if n == 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
                return True
            else:
                return False

        # If len(flowerbed) > 3

        for i in range(1, len(flowerbed) -1):

            # First case. Если у нас ситуация [0,0,1], кароче два нуля вначале. Нам надо проверить что текущий и предыдущий == 0, и посадить цветок в первый.
            if i == 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i - 1] = 1
                n -= 1

            # Second case. Ситуация обратная выше. [1,0,0], кароче два нуля вконце. Нам надо проверить что текущий и следующий == 0, и посадить цветок в последний.
            if i == len(flowerbed)-2 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i + 1] = 1
                n -= 1

            # Обычная ситуация, когда цветок не первый и не последний, а мы в середине.
            # Не сработает, если сработали первые два, т.к. цветок уже посажен в текущий i.
            # Смотрим если слева и справа цветов нет, тогда садим.
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1

            if n == 0:
                return True

        # n - может быть меньше нуля, если мы садим цветков меньше, чем проходим по массиву. Там то мы n постоянно отнимаем.
        return n <= 0


    # From leetcode
    def canPlaceFlowers3(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True

        count = 1
        result =0
        for i in flowerbed:
            if i ==0:
                count +=1

            else:
                result += (count-1)//2
                count =0
        if count !=0:
            result += count//2

        if n <= result:
            return True
        else:
            return False

sol = Solution()
#candidates = [2, 6, 4, 8, 10, 9, 15]
flowers = [1,0,0,1]

print(sol.canPlaceFlowers3(flowers, 1))
