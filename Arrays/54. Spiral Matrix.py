class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """


        if matrix == []:
            return []

        if len(matrix) < 2:
            return matrix[0]

        # Опрделеяем стартовые и конечные горизонтальный и вертикальный индекс.
        hor_st, ver_st = 0, 0
        hor_end, ver_end = len(matrix[0]) - 1, len(matrix) - 1
        ans = []

        # Сначала идем вправо, затем вниз, влево и вверх.
        while hor_end >= hor_st and ver_end >= ver_st:
            for i in range(hor_st, hor_end + 1):
                ans.append(matrix[ver_st][i])

            for i in range(ver_st + 1, ver_end + 1):
                ans.append(matrix[i][hor_end])

            for i in range(hor_end - 1, hor_st - 1, -1):
                # Если у нас стартовый индекс равен конечному, то тогда обратно не идем. Иначе идем.
                if ver_st != ver_end:
                    ans.append(matrix[ver_end][i])

            for i in range(ver_end - 1, ver_st, -1):
                # Если у нас стартовый индекс равен конечному, то тогда обратно не идем. Иначе идем.
                if hor_st != hor_end:
                    ans.append(matrix[i][hor_st])



            hor_st += 1
            hor_end -= 1
            ver_st += 1
            ver_end -= 1

        return ans


# T - O(R*C)
# S - O(R*C)

sol = Solution()

candidates = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]]


print(sol.spiralOrder(candidates))
