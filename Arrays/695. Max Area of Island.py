class Solution(object):
    def maxAreaOfIsland(self, grid):


        # Это решение не правильное. Оно для другого случая, оно считает максимальную площадь квадратов.
        # Идем по строкам, и сохраняем результат в одну общую строку(column). Если встречаем 1, прибавляем. Если 0, возвращаем 0 обратно.
        max_area = 0
        column = [0] * len(grid[0])

        for k in range(len(grid)):
            area = 0

            for i in range(len(grid[0])):
                if grid[k][i] == 1:
                    column[i] += 1
                else:
                    column[i] = 0

                if column[i] == 0:
                    max_area = max(max_area, area)
                    area = 0
                else:
                    area += column[i]

            max_area = max(max_area, area)

        return max_area

# T -O(R*C)
# S - O(R*C)

    # Правильное решение. Идем по строкам и просматриваем сразу все варианты, вверх вниз, влево, и вправо. Если там единица, идем дальше.
    def maxAreaOfIsland2(self, grid):

        max_area = 0
        for k in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[k][i] == 1:
                    max_area = max(max_area, self.AreaOfIsland(grid, k, i))

        return max_area


    def AreaOfIsland(self, grid, k ,i):

        # Базовые условия чтобы не выйти за границы, и если ячейка равна 1
        if k >= 0 and k < len(grid) and i >= 0 and i < len(grid[0]) and grid[k][i] == 1:

            # Модофицируем ячейку, чтобы больше не вызвать рекурсивную функцию
            grid[k][i] = -1

            # Возвращаем все варианты вверх вниз влево вправо и прибавляем единицу к сумме площади
            return 1 + self.AreaOfIsland(grid, k - 1, i) + self.AreaOfIsland(grid, k + 1, i) + self.AreaOfIsland(grid, k, i - 1) + self.AreaOfIsland(grid, k, i + 1)

        return 0

# T -O(R*C) - тут есть вопросы. Если он счетчик верхней функции прогонит O(R*C) в любом случае. В худщшем случае(когда все 1), рекурсия прогонится только для одного, но по всем, что есть R*C.
# Дальше в рекурсию он просто не будет заходить, но верхнюю фонкцию то все равно прогонит, хоть и не будет ничего делать с ней.
# Худший случай. Рекурсия для первого элемента - 1 * R*C. А так же прогнать вхолостую первую функцию - R*C. Получается 1 * R*C + R*C = R*C
# Возможно R*C + R*C = O(R*C)
# S - O(R*C) - передаем в стек рекурсии сетку.


sol = Solution()
candidates = [[1,1],
              [0,1]]



print(sol.maxAreaOfIsland2(candidates))
